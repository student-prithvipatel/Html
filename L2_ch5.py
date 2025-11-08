# Dictionary
d={'name':'raj','age':33,'gender':'male'}
print(d)
print(type(d))
print(type({}))
# d1={[1,2,3]:'abc',1:20}
d2={(1,2,3):'abc',1:20}
print(d2)
d3={'A':10,'A':100}
print(d3)
d4={'a':[1,2,3,4]}
print(d4)
d5={'name':'raj','branch':'CST','sub':{'DE':25,'PY':24,'FSD':20}}
print(d5['name'])
print(d5['sub']['PY'])
print(d5.get('branch'))


# add element
d={'name':'raj','age':33,'gender':'male'}
d['branch']='cs'
print(d)
d.setdefault(5,50)
print(d)
d['name']='xyz'
print(d)
d.setdefault('name','Abc')
print(d)


# delete element
d={'name': 'xyz', 'age': 33, 'gender': 'male', 'branch': 'cs', 5: 50}
d.pop(5)
print(d)
d.popitem()
print(d)
del d['age']
print(d)
d.clear()
print(d)


# important funtion
d={'name': 'xyz', 'age': 33, 'gender': 'male', 'branch': 'cs'}
print(len(d))
print(min(d))
print(max(d))
print(sorted(d))
print(sorted(d,reverse=True))
print(d.keys())
print(d.values())
print(d.items())
d1={'A':10,'B':20}
d1.update(d)
print(d1)
print('name' in d)
print('xyz' in d)


for i in d:
    print(i,'-',d[i])
    
print()

for i,j in d.items():
    print(i,'-',j)


# dictionary comprehension

print({i:i**2 for i in range(1,11)})

l1=['s','m','t','w','th','f','st']
l2=[27,26,28,29,30,26,27]
print({i:j for i,j in zip(l1,l2)})
print(dict(zip(l1,l2)))

l=[('A',10),('B',20),('C',30)]
print(dict(l))


s='lj is good for events'
d={'good':'the best','events':'study'}

s1=s.split(' ')
l=[]
for i in s1:
    if i in d:
        l.append(d[i])
    else:
        l.append(i)
print(' '.join(l))


st='abccbadb'

d={}
for i in st:
    d[i]=d.get(i,0)+1
print(d)


st1='asd abc bda pqr cdb'

d={}
for i in st1.split(' '):
    d[i[0]]=d.get(i[0],0)+1
print(d)


st1='asd abc bda pqr cdb'

d={}
for i in st1.split(' '):
    if i[0] not in d:
        d[i[0]]=[]
        d[i[0]].append(i)
    else:
        d[i[0]].append(i)
print(d)


# wapp to covert entered int number into word. Note:number valid for 0 to 999

def int_to_word(n):
    d={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
       11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourty',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighty',19:'Ninteen',
       20:'Twenty',30:'Thirty',40:'Fourty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninty'}
    if(n<=20):
        return d[n]
    if(n>20 and n<100):
        if n%10==0:
            return[n]
        else:
            return d[n//10*10]+d[n%10]
    if(n>=100 and n<1000):
        if n%100==0:
            return d[n//100]+'hundred'
        else:
            return d[n//100]+'hundred'+int_to_word(n%100)
        
n=int(input("Enter No = "))
print(int_to_word(n))


# wap to get a list of int number from user(using eval fun) count number of special element from the list the element is special
# if the removal of that element make the list balance the list is balanced if sum of even index element is equal to the sum of 
# odd index element

l=eval(input("Enter number"))
c=0
for i in range(0,len(l)):
    l1=l.copy()
    l1.pop(i)
    if sum(l1[::2])==sum(l1[1::2]):
        c=c+1
print(c)


# wap to find common prefix from the list
s=''
l=[]
l.sort()
size=len(l)
if size==0:
    print("nothing")
elif size==1:
    print(l[0])
else:
    end=min(len(l[0]),len(l[-1]))
    i=0
    while (i<end and l[0][i]==l[size-1][i]):
        s=s+l[0][i]
        i=i+1
    if s=='':
        print(-1)
    else:
        print(s)


# wap to rotate n*n matrics in 90 degree

def rotate_90(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
n=int(input('Enter size of matrix : '))
matrix=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input('enter no = ')))
    matrix.append(a)
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=' ')
    print()
print('After Rotation')
rotate_90(matrix)
for i in matrix:
    for j in i:
        print(j,end=' ')
    print()


# wapp to covert int to roman no
def int_to_roman(n):
    val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    sy=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    r=''
    i=0
    while n>0:
        for j in range(n//val[i]):
            r=r+sy[i]
            n=n-val[i]
        i=i+1
    return r
n=int(input('Enter no = '))
print(int_to_roman(n))
