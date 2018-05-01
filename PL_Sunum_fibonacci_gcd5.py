print("En Kucuk Ortak Kat")
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print("GCD is: ")
print(GCD)



#print("Fibonacci Serileri Kısmı")

def fib(n):
    """Fibonacci:
    fib(n) = fib(n - 1) + fib(n - 2) sen > 1
    fib(n) = 1 se n <= 1
    """
    
    # the first two values
    l = [1, 1]
    
    # Calculating the others
    for i in range(2, n + 1):
        l.append(l[i -1] + l[i - 2])
        
    return l[n]

# Show Fibonacci from 1 to 5

num=int(input("Enter an integer:"))

for i in range(0,num):#[1, 2, 3, 4, 5,6,7,8]:
    print (i, '=>', fib(i))