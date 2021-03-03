"""
fibonacci Sequence=0,1,1,2,3,5,8,13.......
"""
def fib(n):
    if n== 0:
        return 0
    if n==1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))

# print(fib(7))

for i in range(13):
    print(i)