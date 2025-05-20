n=[1,2,3,4,5,6,7,8,9,10]
e=filter(lambda x:x %2==0,n)
o=filter(lambda x:x %2!=0,n)
print("Even numbers:",list(e))
print("Odd numbers:",list(o))