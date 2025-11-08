s="This is python"
print(s[-14:1])
print(s[0:4])
print(s[::])
print(s[::-1])
print(s[-2:-9:-1])
print(s[-5::])
print(s[1:-1])
print(s[::2])
print(s[:-1:3])
print(s[::-2])
del s
# print(s)


s1='hello'
s2='hi'
print(s1+s2)
print(s1*3)
s1+='student'
print(s1)
print(s1>s2)
print('A'>'a')
print(''and'Hi')
print('Hello'and'Hi')
print(''or'hello')
print(not'')
print(not s2)
s3='this is python'
print('is' in s3)


s1='Hello'
index=0
for i in s1:
    print(index,'-',i)
    index+=1
for i,j in enumerate(s1):
    print(i,'-',j)


s='This is python'
print(len(s))
print(min(s))
print(max(s))
print(sorted(s))
print(sorted(s,reverse=True))
# print(dir(s))
s1='learning python is easy in all languages'
print(s1.capitalize())
print(s1.title())
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.count('i'))
print(s1.find('in'))
print(s1.rfind('in'))
print(s1.find('in',11,len(s1)))
print(s1.find('xyz'))
print(s1.index('in'))
print(s1.rindex('in'))
print(s1.index('in',11,len(s1)))
#print(s1.index('in',0,5))
s1.startswith('le')
print('Abc'.isidentifier())
'this'.join(['w','o','r','l','d'])


#wap to find frequancy of particular character in provided str by user
s=input("Enter str : ")
term='a'
count=0
for i in s:
    if i==term:
        count+=1
print(count)


#to check pelidrome or not
s=input("Enter : ")
if s==s[::-1] :
    print('pelindrome')
