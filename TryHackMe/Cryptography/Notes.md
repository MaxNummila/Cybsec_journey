# Cryptography
-	Ultimate purpose is to ensure secure communication in the presence of adversaries
-	PCI DSS is the Payment Card Industry Data Security Standard that is used for credit card handling
-	Plaintext is the original readable data or message before encryption
-	Ciphertext is the scrambled unreadable data or message after encryption
-	Cipher is the algorithm or method used for converting plaintext to ciphertext
-	Key is a string of bits the cipher uses to encrypt or decrypt data
-	Encryption is the process of converting plaintext to ciphertext
-	Decryption is the process of converting ciphertext to plaintext

### Caesar Cipher
-	First century BCE
-	Shift each letter by a certain number to encrypt it
-	26 letters so 25 valid keys for encryption
-	Considered insecure
### Symmetric Encryption
-	Uses the same key to encrypt and decrypt the data
-	Key must be secret
-	Also thus called private key cryptography
-	Communicating the key to the intended parties can be challenging
-	Examples of symmetric encryption
o	DES
	56-bit key, broken in less than 24 hours
o	3DES
	168-bit key, though effective security is 112 bits. Deprecated 2019
o	AES
	Key size can be 128, 192 or 256 bits
### Asymmetric Encryption
-	Uses a pair of keys, one to encrypt and one to decrypt
-	Encryption key is public, thus also called public key encryption
-	Examples
o	RSA 
	2048-bit, 3072-bit and 4096-bit keys
o	Diffie-Hellman
	2048-bit, 3072-bit and 4096-bit keys
o	ECC – Elliptic curve cryptography
	Equivalent security with shorter keys
	With a 256-bit key provides a similar level of security to a 3072-bit RSA key
-	Tends to be slower and uses larger keys than symmetric encryption
### XOR Operation
-	Exclusive or
-	Compares two bits and returns 1 if the bits are different and 0 if they are the same
-	Commutative and associative
-	Example
o	Consider the binary values P and K, where P is plaintext, K is secret key, ciphertext is C = K XOR P
o	If we know C and K, we can recover P
o	Start with C XOR K = (P XOR K)
o	We know that (P XOR K) XOR K = P XOR (K XOR K) because XOR is associative
o	Furthermore we know that K XOR K = 0
o	Thus (P XOR K) XOR K = P XOR 0, which gives us P
o	This proves that with C and K one can decipher P
### Modulo operation
-	Commonly written % or mod
-	Is the remainder when x is divided by y (X%Y)

## Public key Cryptography basics
-	Authentication: Verification of identity
-	Authenticity: Verification of whom a message is coming from
-	Integrity: Verification that the data/message has not been tampered with
-	Confidentiality: Only authorized parties can access the data
-	Diffie-Hellman key exchange
o	Establishes a shared secret between two parties
## SSH
-	Uses ED25519 as the public-key algorithm for digital signature generation and verification
-	After public-key, user needs to be authenticated, often using a username and password
-	This however is not the most secure method, and some machines use key authentication instead
-	By default these private keys are RSA keys, but you can choose which algorithm to generate and add a passphrase to encrypt the SSH key
-	Most often used program is ssh-keygen
-	SSH keys are never to be shared
-	The passphrase is only used for decrypting the private key, it never leaves your system
-	Tools like John the Ripper can be used to attack encrypted SSH keys, highlighting the importance of using complex passphrases
-	Only the owner should be able to write or read to the private key
### Digital signatures and Certifications
-	Using asymmetric cryptography, one can prove authenticity by producing a signature with their private key, which can be verified with their public key
-	HTTPS uses certificates to make sure that you are on say the real google.com
-	Lets encrypt for free TLS certificates
### PGP and GPG
-	PGP: Pretty good Privacy
o	Software that implements encryption for encrypting files, digital signings and more
-	GPG: Open-source implementation of the OpenPGP standard
o	Commonly used in email to protect the confidentiality of the messages
-	PGP and GPG private keys can be protected with passphrases like SSH keys.
-	For this one can use John the Ripper or gpg2john
## Hashing basics
-	Hash values can be used to verify that something is what it was intended to be, say a download. Comparing the hash of the file you downloaded and the hash of the file from where it was downloaded proves that they are the same.
-	Hash Value: A fixed-size string that is computed by a hash function. 
-	Hash Function: Takes an input of an arbitrary size and returns an output of fixed length
-	Hash as a verb means the calculation of the value, and hash as a noun means the hash value itself
-	Hash functions are different from encryption:
o	No key
o	Meant to be impossible to go from the output back to the input
o	Takes some input data and creates a summary or digest of that data
-	Hash Collision is when two different inputs give the same output
-	Hash functions are designed to avoid collisions but with infinite inputs and limited outputs it cant be completely avoided
-	Example: if a hash function produces a 4-bit hash value, we only have 16 different hash values.
-	Total number of possible hash values is 2^number_of_bits
-	The pigeonhole effect states that the number of items is more than the number of containers; some containers must hold more than one item
-	MD5 and SHA1 have been attacked and are considered insecure due to not being able to avoid collisions
-	Hashing has many uses but here the focus is on password storage and data integrity
-	Password salt: adding a random value to the password before it is hashed
-	Rainbow table: lookup table of hashes to plaintext
-	Crackstation and hashes.com use massive rainbow tables for hashes without salt
### Recognising password hashes
-	Linux passwords are stored in /etc/shadow, which is normally only readable by root
-	Each lin contains nine fields, separated by colons. The first two fields are the login name and the encrypted password. Info about the other fields can be found with man 5 shadow command
-	Encrypted password field cotains hashed passphrase in this format $prefix$options$salt$hash
-	MS Windows passwords are hashed using NTLM
-	Stored in SAM (Security Accounts Manager)
-	Windows tries to prevent normal users from dumping them, but tools such as mimikatz exist to circumvent MS windows security
### Password cracking
-	GPU:s can be used to crack some hashes faster but algorithms such as bcrypt have made sure that it is no faster than doing it on a CPU
## John the Ripper
-	Using John for:
o	Cracking Windows authentication hashes
o	Cracking /etc/shadow hashes
o	Cracking password-protected Zip files
o	Cracking password-protected RAR files
o	Cracking SSH keys
-	Cracking hashes is hard, but possible if you know the hashing method and have a dictionary of possible passwords to hash
-	Called a Dictionary attack
### Syntax
-	John [options] [file path]
o	John: Invokes the John the Ripper program
o	[options]: Specifies options that one wants to use
o	[file path]: File containing the hash that one is trying to crack
### Automatic Cracking
-	John has built-in features for detecting the type of hash but it can be unreliable
-	John --wordlist=[path to wordlist] [path to file]
o	--wordlist: Specifies using wordlist mode, reading from the file in the path
### Identifying hashes
-	Tools such as hash-identifier can be used for easy hash identification
Format-specific cracking
-	John --format=[format] --wordlist=[path to wordlist] [path to file]
o	--format: Tells John that you are giving it a hash of a specific format and to use it to crack
