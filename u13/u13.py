'''LIST
x=[item1,item2,item3,item4......]
we can addition, delete items

ADD SOMETHING INTO END OF THE LIST
x.append()

ADD SOMETHING INTO YOU WANT PLACE
x.insert(index,value)

TO DELETE SOME ELEMENT
del x[]

TO DELETE SOME PHRASE
del x[0:0]

PRINT ONE ELEMENT
print(x[0])
'''

x=[15,45,'jj',45.2,5,4.6]
print(x[2])

x.append("end")#add some thing into end of the list
x.insert(5,"number")#ADD SOMETHING INTO YOU WANT PLACE
del x[0]#to delete some element
print(x)

del x[0]#to delete some element
print(x)

del x[1:4]#to delete some phrase
print("delete = ",x)

print("one = ", x[1])#print one element








