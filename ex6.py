def reverse(n):
    if n==0:
        return 0
    else:
        mod=(n%10)
        print(mod)
        return reverse(n//10)
n=int(input())
reverse(n)
