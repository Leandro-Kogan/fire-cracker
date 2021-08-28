import hashlib
import optparse
import sys
import time

parser = optparse.OptionParser()
parser.add_option("-f", "--file", dest="filename", help="select file with HASH value, this program does not support MD4")
parser.add_option("-w", "--wordlist", dest="wordlist", help="select wordlist file")
(options, args) = parser.parse_args()

wordlist = options.wordlist
filename = options.filename

print("""                                      (                         )       (     
                         (                       (    )\ )    (        (     ( /(       )\ )  
                         )\ )  (   (      (      )\  (()/(    )\       )\    )\()) (   (()/(  
                        (()/(  )\  )(    ))\   (((_)  /(_))((((_)(   (((_) |((_)\  )\   /(_)) 
                         /(_))((_)(()\  /((_)  )\___ (_))   )\ _ )\  )\___ |_ ((_)((_) (_))   
                        (_) _| (_) ((_)(_))   ((/ __|| _ \  (_)_\(_)((/ __|| |/ / | __|| _ \  
                         |  _| | || '_|/ -_)   | (__ |   /   / _ \   | (__   ' <  | _| |   /  
                         |_|   |_||_|  \___|    \___||_|_\  /_/ \_\   \___| _|\_\ |___||_|_\  
                                                                      
                                                                                           
                                                                           """)


banner = "------------>MD5------------>SHA256------------>SHA1------------>SHA512------------>HASH-CRACKER------------>By Leandro Kogan\n"

for c in banner:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.003)
print
print("https://github.com/Leandro-Kogan\n\n")
start = time.time()

with open(wordlist, "rb") as f:
    content = f.read()
    lines = content.splitlines()

with open(filename, "r") as f:
    content = f.read()
    objective = content.splitlines()

lenght = len(objective[0])
words = len(lines)
if lenght == 32:
    hash_type = "md5"
elif lenght == 64:
    hash_type = "sha256"
elif lenght == 40:
    hash_type = "sha1"
elif lenght == 128:
    hash_type = "sha512"

print("[+]File selected: " + filename)
print("[+]Wordlist selected: " + str(wordlist) + " : amount of words: " + str(words))
print("[+]Hash type selected: " + hash_type)


if lenght == 32:
    try:
        for i in lines:
            hashed = hashlib.md5(i)
            hashed = hashed.hexdigest()
            hashed = str(hashed)
            for x in objective:
                    x = x.lower()
                    if hashed == x:
                        i = i.decode()
                        i = str(i)
                        hashed = str(hashed)
                        print("[+]Password found: "+ i + " for hash: " + hashed)
                        sys.exit()
                    else:
                        continue

    except:
        pass

elif lenght == 64:
    try:
        for i in lines:

            hashed = hashlib.sha256(i)
            hashed = hashed.hexdigest()
            hashed = str(hashed)
            for x in objective:
                    x = x.lower()
                    if hashed == x:
                        i = i.decode()
                        i = str(i)
                        hashed = str(hashed)
                        print("[+]Password found: " + i + " for hash: " + hashed)
                        sys.exit()

                    else:
                        continue

    except:
        pass

elif lenght == 40:
    try:
        for i in lines:

            hashed = hashlib.sha1(i)
            hashed = hashed.hexdigest()
            hashed = str(hashed)
            for x in objective:
                    x = x.lower()
                    if hashed == x:
                        i = i.decode()
                        i = str(i)
                        hashed = str(hashed)
                        print("[+]Password found: " + i + " for hash: " + hashed)
                        sys.exit()


                    else:
                        continue

    except:
        pass

elif lenght == 128:
    try:
        for i in lines:

            hashed = hashlib.sha512(i)
            hashed = hashed.hexdigest()
            hashed = str(hashed)
            for x in objective:
                    x = x.lower()
                    if hashed == x:
                        i = i.decode()
                        i = str(i)
                        hashed = str(hashed)
                        print("[+]Password found: " + i + " for hash: " + hashed)
                        sys.exit()

                    else:
                        continue

    except:
        pass
    
else:
    print("[!!!]GoodBye!!!")
    
finn = time.time()
print("[+]Time elapsed: " + str(finn - start) + " seconds")

print("[+]GoodBye!!!")
print("[+]Thank you for using FIRE-CRACKER")