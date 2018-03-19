import hashlib
import sys
import time




message = input("hexdigest message =")
print( message)

filename = input("enter the name or your wordlist file")

i=0

file = open(filename)
start = time.time()
for word in file:
    word = word[0:len(word)-1]
    sifreleyici_2 = hashlib.md5(word.encode("utf-8"))
    if message == sifreleyici_2.hexdigest():
        print("key found: " + word)
        end = time.time()
        print(str(end - start)+" saniye")
        bekle = input("enter to out")
        
        sys.exit()  
    i = i+1
    if i%1000000 == 0:
        print("forcing.. " + str(i) + ".")


file.close()

#5cd7500de60570f7fec996ab10abfb9a - ahmetcan
