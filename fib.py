def fib_list(max):
    fib = []
    a,b=0,1
    count =0;
    while count<=max:
        fib.append(a)
        a,b=b,a+b
        count+=1
    return fib

#fib_list(100000) this will take more memory as all the numbers are saved in a list 
#we cant even run fib_list for 1000000 as it takes too much storage
#this is why generators are helpful
def fib_gen(max):
    a,b=0,1
    count = 0
    count =0;
    while count<max:
        a,b=b,a+b
        yield a
        count+=1

for n in fib_gen(1000000):#this will take less memory because we are not saving anything computing and printing
    print(n)
