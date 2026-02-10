import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

# Execute function that uses the subprocess library method check_output, which runs a command on the local OS, 
# and returns the output from the command
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd),
                                     stderr = subprocess.STDOUT)
    return output.decode()

# NetCat class that initializes with the arguments from the command line and the buffer and then create the socket object
class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Send function that connects to the target and port, and if there is a buffer, it sends that to the target first
    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)
        
        # Try catch block for manually closing the connection with CTRL + C
        try:
            # Loop for receiving data from target. Once there is no more data it breaks out of loop
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                # Otherwise prints the response data and pauses to get interactive input, sends the input and continues loop
                if response:
                    print(response)
                    buffer = input('> ')
                    buffer += '\n'
                    self.socket.send(buffer.encode())
        # Loop will continue until user interrupts it which closes the socket
        except KeyboardInterrupt:
            print('User terminated.')
            self.socket.close()
            sys.exit()
    
    # Listen method that executes when the program runs as a listener
    def listen(self):
        # Binds to the target and port and starts listening in a loop
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        while True:
            client_socket, _ = self.socket.accept()
            # Passes the connected socket to the handle method
            client_thread = threading.Thread(
                target=self.handle, args=(client_socket,)
            )
            client_thread.start()

    # Handle method that executes the task corresponding to the command line argument it receives:
    # - Execute a command
    # - Upload a file
    # - Start a shell
    def handle(self, client_socket):
        # If a command should be executed the method passes the command to the execute function and sends the output back
        # on the socket
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())

        # If a file should be uploaded, it uses a loop to listen for content on the listening socket and receive data until
        # there is no data coming in. Then writes the accumulated content to a specified file
        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break
            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f'Saved file {self.args.upload}'
            client_socket.send(message.encode())

        # If shell is to be created, sets up loop, sends prompt to the sender, and waits for a command to come back. Then
        # executes the command with the execute function and return the output of the command to the sender
        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'BHP: #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'Server killed {e}')
                    self.socket.close()
                    sys.exit()

    # Entry point for managing the NetCat object, delegates execution to the two methods:
    # If setting up a listener it calls the listen method, and otherwise calls the send method
    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

if __name__ == '__main__':
    # Uses the argparse module to create a command line interface. Then provides arguments so it can be invoked to:
    # Upload a file, execute a command or start a command shell
    parser = argparse.ArgumentParser(
        description='BHP Net Tool/Netcat copy',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        # Provides example usage that the program will display when a user invokes it with --help
        epilog=textwrap.dedent('''Example:
            netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
            netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload to file
            netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\ # Execute command
            echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # Echo text to server port 135
            netcat.py -t 192.168.1.108 -p 5555 # Connect to server
    '''))

# Six arguments for how we want the program to behave
# -c sets up an interactive shell
parser.add_argument('-c', '--command', action='store_true', help='command shell')
# -e executes one specific command
parser.add_argument('-e', '--execute', help='execute specified command')
# -l indicates that a listener should be set up
parser.add_argument('-l', '--listen', action='store_true', help='listen')
# -p specifies the port on which to communicate
parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
# -t specifies the target IP
parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
# -u specifies the name of a file to upload
parser.add_argument('-u', '--upload', help='upload file')
args = parser.parse_args()

# If setting up as listener we incoke the NetCat object with an empty buffer string, otherwise we send the buffer content
# from stdin, finally runs the run method  to start it up
if args.listen:
    buffer = ''
else:
    buffer = sys.stdin.read()

nc = NetCat(args, buffer.encode())
nc.run()
