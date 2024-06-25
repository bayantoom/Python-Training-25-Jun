def is_prime(n: int):
    if n > 1:
        if n==2 or n==3:
            return True 
       
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
            else:
                return True 
    else: 
        return False 

def prime_count():
    n = int(input("Please enter a number: "))
    count=0
    
    for i in range(2,n+1):
       if is_prime(i):
           count+=1
    
    print(f"The number of prime numbers that exist up to {n} is {count}") 

prime_count()

