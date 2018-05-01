import sys
import random
import datetime

remarks=['Hava çok guzel degil mi ya!', 
         'Ne var ne yok?',
         'PL odevlerini yapmissındır kesin']
reply=['Hadi canim?', 'Oh wow!', 'tamamdir...','vay arkadas!']

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("Ismin Nedir? ")
    if name == '': name = 'gizemli'
    
hour = datetime.datetime.now().hour

if hour < 12:
    print ("Gunaydin! ", name)
elif hour < 18:
    print ("Oo saati ogle yapmissin", name)
else:
    print ("Iyi Aksamlar", name, "Hocam")

input (random.choice(remarks))
print (random.choice(reply), "Ok abi, sonra gorusuruz!\n")