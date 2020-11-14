"""Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number"""
count=0
total=0
avg=0
while True:
    n=input("enter the number: ")
    try:
        n=int(n)
        count=count+1
        total=total+n
        avg=total/count
    except:
        if n== "done":
            break
        else:
            print("Invalid input")
print(count,total,avg)
