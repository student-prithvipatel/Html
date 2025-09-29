marks=int(input("Enter marks : "))
if marks>100 or marks<0:
    print("enter makes properly")
elif marks>=80 and marks<100:
    print("Grade A")
elif marks>=60 and marks<80:
    print("grade B")
elif marks>=35 and marks<60:
    print("Grade C")
else:
    print("Fail")



# write a python program to create calculate +,-,*,/,//,% get 2 no. from user also get sign of operation from user
a= int(input("Enter first no : "))
b= int(input("Enter second no : "))
x= input("Enter sign from +,-,*,/,//,% : ")
if x == '+':
    print('Addition = ',a+b)
elif x == '-':
    print('Subtraction = ',a-b)
elif x == '*':
    print('Multiplication = ',a*b)
elif x == '/':
    print('Division = ',a/b)
elif x == '//':
    print('Float Division = ',a//b)
elif x == '%':
    print('Modulo = ',a%b)
else:
    print('Enter proper sign')




# write a python program to get day, month, year from user check the date is valid or not if the date is valid then written incremented date
dd=int(input('Enter day : '))
mm=int(input('Enter month : '))
yy=int(input('Enter year : '))
if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    m=31
elif (mm==4 or mm==6 or mm==9 or mm==11):
    m=30
elif (yy%4==0 and yy%100!=0 or yy%400==0):
    m=29
else:
    m=28
if (mm<1 or mm>12):
    print('Date is invlid')
elif(dd<1 or dd>m):
    print('Date is invalid')
elif (dd==m and mm!=12):
    dd=1
    mm=mm+1
    print('Incremented Date : ',dd,mm,yy)
elif (dd==m and mm==12):
    dd=1
    mm=1
    yy=yy+1
    print('Incremented Date : ',dd,mm,yy)
else:
    dd=dd+1
    print('Incremented Date : ',dd,mm,yy)



# write a python program to calculate parking fees enter hours in 24 hour system if number of hours is grater than three then the parking fees as below
eh=int(input("Enter entry hour : "))
em=int(input("Enter entry min : "))
exh=int(input("Enter exit hour : "))
exm=int(input("Enter exit min : "))
print('Press 1 for truck/bus')
print('Press 2 for car')
print('Press 3 for two wheeler')
v=int(input("Enter type of vehical : "))
if exh<eh:
    exh=+24
pth=exh-eh
ptm=exm-em
if pth<3 or (pth==3 and ptm==0):
    if v==1:
        rate=50
    elif v==2:
        rate=30
    else:
        rate=15
elif pth>3 or(pth==3 and pth>0):
    if v==1:
        rate=100
    elif v==2:
        rate=60
    else:
        rate=30
print('parking_rate = ',rate)


# write a python programm to check the given number is disariam or not
n=int(input("Enter number : "))
temp=n
sum=0
count=1
while temp!=0:
    r=temp%10
    sum=sum+r**count
    temp=temp//10
    count=count+1
if(n==sum):
    print("disorium")
else:
    print("not")


# wap to swap first and last digit of number
x=int(input("Enter number : "))
temp=x
x1=x
c=0
while x1!=0:
    c=c+1
    x1=x1//10
if c>1:
    f_d=x//10**(c-1)
    l_d=x%10
    m_d=(x-(f_d*(10**(c-1))))//10
    swapped_No=l_d*10**(c-1)+m_d*10+f_d # m_d=(x%10**(c-1))//10
    print(swapped_No)
else:
    print(temp)


def name(n):
    print('Hello ',n)


def add_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub


def square(x):
    """ Argument """
    y=x**2
    return y


# Positional Argument
def sub(a,b):
    print(a-b)


# Keyword Argument
def wish(name,msg):
    print('Heloo',name,msg)


def defualt_arg(msg='xyz'):
    print(msg)

def variable_length_arg (*n):
    total=0
    for i in n:
        total+=i
    print(total)

def display(**kwards):
    for k,v in kwards.items():
        print(k,'=',v)

  def f1(n1,*s):
    print(n1)
    print(s)
    for i in s:
        print(i)

    name('Prithvi')
a=add_sub(5,4)
for i in a:
    print(i)
print(square.__doc__)
sub(100,200)
sub(200,100)
wish(name='SHP',msg='GM')
defualt_arg()
defualt_arg('abc')
variable_length_arg(10,20,20,50)
display(m1=100,m2=200,m3=300)
f1(10,20,30,40)


# recursion
def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
print(factorial(5))


# Nested fuction
def outerfunc(text):
#     text=text
    print(text)
    def innerfuc():
        print(text)
    innerfuc()
    
outerfunc('Hello')


def outer(text):
    def innerfunc():
        print(text)
    innerfunc()


def outer():
    t='hello'
    def inner():
        t='Welcome'
        print(t)
    inner()
    print(t)
outer()


def n_1(a):
    def n_2(b):
        return a*b
    return n_2
print(n_1(3)(2))


# wap to encode int number enter by user using user difine func. Note: increment each digit by one if digit = 9 then put 0 or repalce with 0
def encode_number(n):
    p=1
    sum=0
    while n!=0:
        t=n%10
        if t<9:
            t=t+1
        else:
            t=0
        sum=sum+t*p
        n=n//10
        p=p*10
    print(sum)

n=int(input('Enter number : '))
encode_number(n)

# wap to check no is happy no or sad no
def check_no(n):
    while n!=1 and n!=4:
        sum=0
        while n!=0:
            d=n%10
            sum=sum+(d**2)
            n=n//10
        n=sum
    if n==1:
        print('Happy no')
    else:
        print('sad no')

n=int(input('Enter number : '))
check_no(n)


def check_no():
    c=1
    while c!=101:
        n=c
        while n!=1 and n!=4:
            sum=0
            while n!=0:
                d=n%10
                sum=sum+(d**2)
                n=n//10
            n=sum
        if n==1:
            print(c)
        c=c+1

check_no()



def fib(x):
    global n_calls
    n_calls+=1
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
def test_fib(n):
    for i in range(n+1):
        global n_calls
        n_calls=0
        print(i,'=',fib(i))
        print('fib called',n_calls)
test_fib(6)




def g():
    print('Hi')
def g():
    print('Good')
g()
