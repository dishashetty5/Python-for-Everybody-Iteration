""" Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average."""
count=0
total=0
a=[]
while True:
    n=input("enter the number: ")
    try:
        n=int(n)
        count=count+1
        total=total+n
        a.append(n)
    except:
        if n== "done":
            break
        else:
            print("Invalid input")
print(count,total,max(a),min(a))
