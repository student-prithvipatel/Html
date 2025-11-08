t=(1,2,3)
print(type(t))
t1=('hello')
print(type(t1))
t2=('hello',)
print(type(t2))
print(type(t2[0]))
t3=('hello',1,2,5.9)
t4=(1,(1,2,3),4,5,1,4)
t5=(1,2,3,4,5)
print(t5[2])
# print(t5[6])
print(t5[1:])
print(t4[1][1])
print(t3[0][-1])
# print(t3[-1][0])
print(tuple('hello'))
print(tuple(range(10,20,2)))
tp=()
print(type(tp))
print(tp)


t=(10,20,30,40)
# t[2]=70
# print(t)
# del t[1]
# print(t)
t1=(50,60,70)
print(t1+t)
print(t*3)
print(20 in t)
print(len(t))
print(max(t))
print(min(t))
# print(max(('A',10,'B')))
t2=(10,20,10,10,20,10)
print(t2.count(10))
print(t2.index(10))
# print(t2.rindex(10))
print(sorted(t2))
print(sorted(t2,reverse=True))


t=(10,20,30,40)
a,b,c,d=t
print(a)
print(b)
print()

for i in t:
    print(i)
    
for i,j in enumerate(t):
    print(i,'-',j)


a=5
b=2
c=a+b
print("{}+{}={}".format(a,b,c))


#wapp to find sum of even and sum of odd
t=eval(input("Enter tuple"))
sumeven=0
sumodd=0
for i in t:
    if i%2==0:
        sumeven+=i
    else:
        sumodd+=i
print(t)
print(sumeven)
print(sumodd)


# wapp to encrypt the string as per key number 
s=input("Enter String: ")
key=int(input("Enter key : "))
s1=""
for i in range(key):
    s1+=(s[i::key])
print(s1)

l=len(s1)
part=l//key
extra=l%key
p1=s1[:(part+1)*extra]
p2=s1[(part+1)*extra:]
msg=''
for i in range(part+1):
    if i<part:
        msg+=p1[i::part+1]+p2[i::part]
    else:
        msg+=p1[i::part+1]
print(msg)


s=input("Enter String: ")
l=s.split()
s1=""
for i in l:
    if len(i)>1:
        s1+=i[0].upper()+i[1:-1]+i[-1].upper()+' '
    else:
        s1+=i.upper()+' '
print(s1)
