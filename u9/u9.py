'''
(තනි අකුරු ප්‍රින්ට් කරීම සදහා පහත සදහන් ආනාරයට අදාල වචනය/ වාකය අංක කරගත යුතුය)
0    1   2   3   4   5   6
d    u   l   e   e   k   a
-7  -6  -5  -4  -3  -2  -1
x = [start;stop]
(examples are given below)
'''
x="duleeka"
print("print unique no for this",x[-7])#print unique no for this
print(x[-6])#print unique no for this
print(x[-5])#print unique no for this
print(x[-4])#print unique no for this
print(x[-3])#print unique no for this
print(x[-2])#print unique no for this
print(x[-1])#print unique no for this

print("print -7 to -2 = ",x[-7:-2])#print -7 to -2

print("print all characters = ",x[-7:])#print all characters

print("didnt print any thing = ",x[5:-15])# didnt print any thing (because out of range)

print('print till you given no = ',x[:-1])# print till you given no

print("print all characters = ",x[:])#print all characters

'''අකුරක් ඇර අකුරක් ප්‍රින්ට් වෙන්න
x = [start:stop:step]'''

print("අකුරක් ඇර අකුරක් ප්‍රින්ට් වෙන්න = ",x[-7:-2:2])#අකුරක් ඇර අකුරක් ප්‍රින්ට් වෙන්න
print("අකුරක් 2 ඇර ප්‍රින්ට් වෙන්න = ",x[-7:-2:3])#අකුරක් 2 ඇර අකුරක් ප්‍රින්ට් වෙන්න

print("to print against side",x[::-1])#to print against side
print(x[::-2])#to print against side (අකුරක් ඇර අකුරක් ප්‍රින්ට් වෙන්න)

print("අවශ්‍ය කොටසක් විරුද්ද දෙසට ප්‍රිනට් කර ගැනීමට = ",x[-1:-3:-1])#අවශ්‍ය කොටසක් විරුද්ද දෙසට ප්‍රිනට් කර ගැනීමට





