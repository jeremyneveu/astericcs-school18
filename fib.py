def fib(N):
    ''' all fibonacci'''
    n0 = 1
    n1 = 1
    for i in range(N-1):
        n1, n0 = n1 + n0
    return n1

if __name__=="__main__":
    for i in range(5):
        print(fib(i))
