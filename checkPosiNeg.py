posNum=negNum=zeronum=0
while True:
    num=int(input("Enter a number= "))
    if num ==-1:
        break
    elif  (num>0):
        print("positive number")
        posNum=posNum+num
    elif (num<0):
        print("Negative number")
        negNum=negNum+num
    else:
        print("Zero has been entered")
        zeronum=zeronum+1
print("Sum of positive numbers:",posNum)
print("Sum of negative numbers:",negNum)
print("Zero entered is:",zeronum)