#Task1
n=int(input('Enter a number: '))

def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

f=factorial(n)
print('Factorial of',n,'is:',f)
