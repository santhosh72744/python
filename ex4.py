#write a recursive progrm to print digits of numbers in reverse order

def reverse(n):
    if n==0:
        return0
        else:
            mod=(n%10)
            print(mod)
            return reverse(n//10)
n=int(input())
reverse(n)
