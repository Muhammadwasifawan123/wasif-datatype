# sum
a=int(input("enter first:"))
b=int(input("enter second:"))
result=a+b
print("{0}+{1}={2}".format(a,b,result))
# append
x="word"
y="hello"
z=(x+y)
# list
lst=["apple","banana","mango"]
print(lst)
# boolen value
x=bool(input("enter:"))
y=bool(input("enter:"))
result=x>y
print("{0}>{1}={2}".format(x,y,result))
#python program to creat dictionary from user.
n=int(input("enter the total no of key-value pairs you want inside your dictionary:"))
for i in range (n):
    d={}

k=input("name:",)
v=input("wasif:",)
g=input("g:",)
r=input("a:",)
o=input("i:",)
u=input("p:",)

d.update({k:v})

print("my dictionary",d)



