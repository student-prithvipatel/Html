# list
l=[1,2,3,4,'AB',(11,12),[14,15]]
print(type(l))
l1=[]
l2=list((1,2,3))
print(l1)
print(l2)
print([1,2,3]==[2,3,1])
l[0]=16.5
print(l)
del l[2]
print(l)


# append()
l=[1,2,3]
l.append(4)
print(l)
l.append(('a','b'))
print(l)
l1=[]
l1.append(91)
l1.append(92)
print(l1)


l=[1,2,3]
l1=[[1,2],[3,4]]
l2=[[[1,2],[3,4]],[[5,6],[7,8]]]
l3=['ABCD',1,2,(1,2,3),6.5]
print(l3[-2])
print(l3[0][1])
print(l3[-2][-2])
print(l2[1][1][1])
print(list('hello'))
print(l3[0][:2])
print(l3[1:][2][1:3])
print(l[-1:-4:-2])


# append,extend,insert
l=[1,2,3]
l.append(4)
# l.append(1,2) --error
l.append((1,2))
l.extend([6,7])
print(l)
l.extend('hello')
print(l)

l1=[1,2,3,4,5]
print(l1.extend([6,7,[1,'ab',8]]))
print(l1)

l2=[1,2,3,4]
l2.insert(1,100)
print(l2)
l2.insert(2,'hello')
print(l2)
l2.insert(2,[200,300])
print(l2)

l3=[1,2,3,4,5]
l3[-1]=500
l3[1:4]=[100,200,300]
print(l3)


# remove
ls1=[1,2,3,4,5,6,2,7]
ls1.remove(2)
print(ls1)
ls1.remove(2)
print(ls1)
# ls1.remove(9)


# pop
ls2=[1,2,3,4,5]
ls2.pop()
print(ls2)
ls2.pop(2)
print(ls2)
# ls2.pop(9)


# clear
ls3=[1,2,3]
ls3.clear()
print(ls3)

# del
ls=[1,2,3,4,5]
del ls[3]
print(ls)
del ls[1:]
print(ls)
del ls
# print(ls) error


l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)
print(l1*3)
print(1 in l1)
print([1,2]<[2,4])


for i in l1:
    print(i)
    
l3=[[1,2],[3,4]]
for i in l3:
    print(i)
    for j in i:
        print(j)
        
for i,j in enumerate(l1):
    print(i,'-',j)


# len,min,max,sum,sort,sorted,count,index,reverse,copy
l1=[8,1,7,6,3,2]
l2=['a','b',1,2]
print(len(l1))
print(min(l1))
print(max(l1))
print(sum(l1))
# print(sum(l2))
print(['A']+['B'])
# print(sum(['A','B']))
l1.sort()
print(l1)
l3=[8,1,7,6,3,2]
print(sorted(l3))
print(sorted(l3,reverse=True))
print(l3)

l6=[1,2,1,3,(1,2),1]
print(l6.count(1))
print(l6.index(1))
print(l6.index(1,1,9))
print(l6.index((1,2)))
# print(l6.index(8))

l1.reverse()
print(l1)

l1=[8,1,7,6,3,2]
l2=l1.copy()
print(id(l1))
print(id(l2))
l1[1]='cd'
print(l1)
print(l2)

l3=l1[::]
print(id(l1))
print(id(l3))
l3[-1]='hello'
print(l1)
print(l3)

l4=l1
print(id(l1))
print(id(l4))
l1[0]=['AB']
print(l1)
print(l4)


l=[]
for i in range(1,11):
    l.append(i)
print(l)

# list comprehension
l1=[i for i in range(1,11)]
print(l1)

print([i for i in range(1,51) if i%5==0])


# wap to find comman food which start with 'A' available in list 1 and list 2 using list comprehension
l1=['apple','banana','kiwi']
l2=['apple','guava','kiwi']
print([i for i in l1 if i in l2 and i[0]=='a'])


l3=list(zip(l1,l2))
print(l3)
print([[i,j] for (i,j) in zip(l1,l2)])


# wap to find conservative sum
l=[1,2,3,4,5]
sum=0
c=[]
for i in l:
    sum+=i
    c.append(sum)
print(c)


l=[2,4,6,10,1]
c=[]
for i in l:
    sum=0
    for j in l:
        if i<=j:
            sum+=j
    c.append(sum)
print(c)
