#factorial using recusrion

def fact(n) :##defining function

    if n==0:
        return 1

    return n * fact(n-1)


result=fact(5)

print(result)
