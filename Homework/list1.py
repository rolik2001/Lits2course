list1 = ['apple','orange','milk']
print(list1)
list1.remove('apple')
print(list1)
list1.append( 'bread' )
print(list1)
i = len(list1)
while 0<i:
 i=i-1
 del list1[i]
 print(list1)
