# fire-cracker

Password Cracker for MD5, SHA216, SHA1 and SHA512 hashes.
It detects the hash type automatically guided by the lenght of the hash, the only thing you will need to define is a text file where the hash you want to crack is and the wordlist you want to use for hash comparing.

It is very simple to use, in the terminal or CMD you do:
"python fire_cracker.py -f <text hash file> -w <wordlist file>"

It works for Linux & Windows, and also runs in python 2 & 3 
