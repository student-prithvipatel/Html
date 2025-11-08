# set
s={1,2,3}
print(s)
s1=set()
print(type(s1))
print(s1)
s2={1,1.5,'AB',(1,2)}
s.update(s2)
print(s)
s4={1,1,2,2,3}
print(s4)
print({1,2}=={2,1})


# add
s4.add(5)
print(s4)
s4.update([7,8,9])
print(s4)


# delete
s={1,2,3,4,5,6,7,8}
s.discard(4)
print(s)
s.discard(50)
print(s)
s.remove(6)
print(s)
# s.remove(50)
# print(s)
s.pop()
print(s)
s.clear()
print(s)


s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1|s2)
print(s1.union(s2))
print(s1&s2)
print(s1.intersection(s2))
print(s1-s2)
print(s2-s1)
print(s1.difference(s2))
print(s1^s2)
print(s1.symmetric_difference(s2))


fs=frozenset({1,2,3})
# fs.add(5)
print(fs)


s1={1,2,3,4,5}
s2={3,4,5}
print(s1.issuperset(s2))
print(s2.issubset(s1))


print({i**2 for i in range(1,11)})
l=(i**2 for i in range(1,11))
print(list(l))
for i in l:
    print(i)


t=(1,2,3)
# print(reversed(t))
print(tuple(reversed(t)))


l=[5,1,2,3,1]
g=[1]
n=len(l)  
for i in range(1,len(l)):
    if l[i]>l[i-1]:
        g.append(g[i-1]+1)
    else:
        g.append(1)
for i in range(n-2,-1,-1):
    if l[i]>l[i+1]:
        g[i]=max(1+g[i+1],g[i])
print(g)
print(sum(g))
