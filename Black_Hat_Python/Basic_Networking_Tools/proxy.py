import sys
import socket
import threading

# HEX_FILTER string that contains ASCII printable characters, if one exists, or a dot if one does not exist.
# The check is done by checking the length of the repr of the character, since printable characters have a length of 3.
HEX_FILTER = ''.join(
    [(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)]
)
# Hexdump function that takes some input as bytes or a string, and prints a hedump to the console. This means that
# it will output the packet details with both their hexadeximal values and ASCII-printable characters.
# This is useful for understanding unknown protocols, finding user credentials in plaintext protocols and much more.
# This function is used for watching communication going through the proxy in real time.

# Make sure we have a string, decoding the bytes if a byte string was passed in.
def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        src = src.decode()
    
    results = list()
    # Then grabs a piece of the string to dump and put it into the word variable
    for i in range(0, len(src), length):
        word = str(src[i:i+length])

        # Uses the translate function to substitute the string representation of each character for the corresponding
        # character in the raw string (printable)
        printable = word.translate(HEX_FILTER)
        # Likewise substitutes the hex representation of the integer value of every character in the raw string (hexa)
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexwidth = length*3
        # Create a new array to hold the strings, result, that contains: 
        # the hex value of the index of the first byte in the word, the hex value of the word and its printable representation.
        results.append(f'{i:04x} {hexa:<{hexwidth}} {printable}')
    if show:
        for line in results:
            print(line)
    else:
        return results
    
# For receiving both local and remote data. Passes in the socket object to be used. Creates an empty byte string called
# buffer, that will accumulate responses from the socket
def receive_from(connection):
    buffer = b""
    # Default five-second time-out, which can be too aggressive if bad connection
    connection.settimeout(5)
    try:
        # Loop to read response data into the buffer until there is no more data or we time out
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except Exception as e:
        pass
    # Returns the buffer byte string to the caller, which could be either local or remote machine
    return buffer
