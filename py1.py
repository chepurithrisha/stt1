"""This code calculates the 
    -Factorial of a number
    -The permutation of n,r
    -The combination of n,r"""
def factorial(n):
    """Calculates the factorial of a non-negative integer number"""
    output=1
    for i in range(1,n+1):
        output=output*i
    return output
def permutation(n,r):
    """Calculates the permutation of non-negative integers n,r"""
    final=(factorial(n))/(factorial(n-r))
    return final
def combination(n,r):
    """Calculates the combination of non-negative integers n,r"""
    result=(factorial(n))/((factorial(n-r))*(factorial(r)))
    return result
def main():
    """Takes the input n and r then prints"""
    n=int(input())
    r=int(input())
    if n<0:
        print("Factorial of this number is undefined")
    else:
        print("The Factorial of this number " ,factorial(n))
    if r<0 or n<r or n<0:
        print("Permutation and Combination both does not exist")
    else:
        print("The Permutation of n and r is",permutation(n,r))
        print("The combination of n and r is",combination(n,r))
if __name__ == "__main__":
    main()
