def fib():
    ''' all fibonacci'''
    if N == 0 :
        return 1
    if N== 1 : 
        return 1
    return fib(N-1) + fib(N-2)

if __name__=="__main":
    for i in range(5):
        print(fib(i))
