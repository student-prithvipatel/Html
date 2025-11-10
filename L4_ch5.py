# lambda
print(lambda a,b:a+b)
x=lambda a,b:a+b
print(x(5,2))

y=lambda x:x**2
print(y(4))


# map
l=[1,2,3,4,5]
s=list(map(lambda x:x**2,l))
print(s)

l1=['apple','banana','kiwi']
s1=(list(map(lambda x: x.startswith('a'),l1)))
print(s1)

s2=list(map(lambda x:'even' if x%2==0 else 'odd',l))
print(s2)

add1=lambda x,y,z:x+(y*z)
print(add1(y=52,z=1,x=10))
print(add1(10,20,2))


# filter
l=[10,40,56,27,13,15,70]
s=list(filter(lambda a:(a%4==0),l))
print(s)
s1=list(filter(lambda a:(a>=50),l))
print(s1)
l1=[0,1,2,3,4]
l2=[1,2,3,4,5]
s=list(map(lambda x,y:x+y,l1,l2))
print(s)


# reduce
from functools import reduce
l=[10,40,56,27,13,15,70]
sum=reduce(lambda x,y:x+y,l)
print(sum)

m=reduce(lambda x,y:x if x>y else y,l)
print(m)


l1=[{'name':'abc','age':45},{'name':'xyz','age':30},{'name':'pqr','age':33}]
n=list(map(lambda x:x['name'],l1))
print(n)


def sq(x):
    return x**2
def transform(f,l):
    o_p=[]
    for i in l:
        o_p.append(f(i))
    print(o_p)
    
l=[1,2,3]
transform(sq,l)
transform(lambda x:x**2,l)


d1={1:'a',2:'b',3:'c'}
print(sorted(d1.items(),key=lambda x:x[1]))
print(sorted(d1.items(),key=lambda x:x[1],reverse=True))

l1=['swati','swati12','swati1']
print(sorted(l1,key=len,reverse=True))
print(sorted(l1,key=len))


books_data=["Inferno,Dan Brown,Thriller,450,4,5",
           "Atomic Habits,James,selfhelp,550,4.8",
           "Ikigai,Hector Garcia,selfhelp,300,4.2",
           "Dune,Frank,sciencefiction,600,4.5"]
book_dict={}
for i in books_data:
    l=i.split(',')
    title=l[0]
    author=l[1]
    genre=l[2]
    price=l[3]
    rating=l[4]
    book_dict[title]={'Auther':author,'Genre':genre,'Price':int(price),'Rating':float(rating)}
    
print(book_dict)

# find avg price of all books
total_price=sum(i['Price']for i in book_dict.values())
avg=total_price/len(book_dict)
print("Avg = ",avg)

# find highest rating
highest_rated=max(book_dict.items(),key=lambda x:x[1]["Rating"])
title,info=highest_rated
print(title,'-',info['Rating'])

# sort by genre
book_genre={}
for i in book_dict.values():
    genre=i['Genre']
    if book_genre[genre] not in book_genre:
        book_genre[genre]=[]
    else:
        book_genre[genre].append(genre)
print(book_genre)
