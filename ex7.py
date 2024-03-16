#write a recursive function to count the number of digits of a number

def count(n):
    while True:
        if n==0:
            return 
        count=0
        count=count%1
        print(count)
        return count(n//10)
count(123)
