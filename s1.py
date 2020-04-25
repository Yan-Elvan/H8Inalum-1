#!/usr/bin/env python
# coding: utf-8

# In[314]:


print('INALUM')


# ## Integer
# Integer adalah type data python berupa angka/ number.

# In[315]:


print(1212123)


# In[316]:


print(16)


# In[317]:


type(10)


# ## Floating-Point
# Floating Point adalah type data di Python yang berupa decimal

# In[318]:


4.2


# In[319]:


0.2


# In[320]:


.4e7


# In[321]:


4.2e-4


# ## String
# String adalah tipe data di Python yang berupa sequence of character data.

# In[322]:


print('Ini adalah type data string')


# In[323]:


type('Ini adalah type data string')


# In[324]:


print('This string contains a double quote (") character.')


# In[325]:


print("This string contains a single quote (') character.")


# ## Boolean
# Boolean adalah tipe data di Python berupa True atau False

# In[326]:


True


# In[327]:


False


# In[328]:


type(True)


# In[329]:


type(False)


# In[330]:


type('True')


# In[331]:


type(1)


# In[332]:


type('1')


# ## Variables
# ### Variables Assignment

# In[333]:


n = 300


# In[334]:


n


# In[335]:


print(n)


# In[336]:


l = 100
m = 200


# In[337]:


l


# In[338]:


n = k = 300


# In[339]:


k


# In[340]:


print (l, m)


# ### Variables Names

# In[341]:


name = 'Titis Pradhitya'
age = 24
has_laptops = True
print(name, age, has_laptops)


# In[342]:


9_kepala_naga = True


# In[ ]:


bola_naga_9 = True


# In[ ]:


age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
print(age, Age, aGe, AGE, a_g_e)


# ## Operators and Expressions in Python

# In[ ]:


a = 10
b = 20


# In[ ]:


a + b


# In[ ]:


a + b - 5


# ### Aritmatic Operations

# In[ ]:


a = 9
b = 6

print(a + b)
print(a - b)
print(a / b)
print(a * b)


# In[ ]:


10 / 5


# ### Comparison Operators

# In[ ]:


a = 10 
b = 20

print(a == b) # sama dengan
print(a != b) # tidak sama dengan
print(a <= b)
print(a >= b)


# ### String Manipulasion

# In[ ]:


# + Operators

s = 'foo'
t = 'bar'
u = 'baz'

print(s + t)


# In[ ]:


s + t + u


# In[ ]:


print('INALUM ' + 'Hacktiv8')


# In[ ]:


# * Operators

s * 4


# In[ ]:


# in Operators

s = 'foo'

s in 'That food for us'


# In[ ]:


s in 'That good for us'


# In[ ]:


# Case Conversion

s = 'InaLUm HaCkTiVe'


# In[ ]:


# Capitalize

s.capitalize()


# In[ ]:


# Title

s.title()


# In[ ]:


# lower
print(s.lower())

# UPPERCASE
print(s.upper())

# Swapcase
s.swapcase()


# ## List 
# ditandai dengan adanya [] - type data berurutan (order)
# berisi objek campuran

# In[ ]:


a = ['foo', 'bar', 'baz', 'qux']


# In[ ]:


a


# In[ ]:


a = [21.42, 'foobar', 3, 4, 'bark', False, 3.12324]


# In[ ]:


a


# In[ ]:


#urutan dimulai dari 0 - 1 - 2 - 3 - 4 - 5
b = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']


# In[ ]:


b


# In[ ]:


b[0]


# In[343]:


b[-5]


# In[344]:


# Slicing

print(b)
print(b[2:5])
print(b[1:4])


# In[345]:


b[0:5]


# In[346]:


b[:5]


# In[347]:


b[2:]


# In[348]:


b + ['value1', 'value2']


# In[349]:


b * 2


# In[350]:


b * 1000


# In[351]:


print(b)

len(b) #length untuk menghitung panjang


# In[352]:


min(b)


# In[353]:


max(b)b


# In[361]:


c = [1,2,3,4,5,6,7,8,9,10]
print(min(c))
print(max(c))


# ### Modifying single list value

# In[362]:


b


# In[363]:


b[2] = 10


# In[364]:


b


# In[365]:


b[-1] = 20


# In[366]:


b


# In[367]:


del b[3]


# In[ ]:


b


# ### Modifying multiple list values

# In[ ]:


b


# In[ ]:


b[1:4]


# In[ ]:


b[1:4] = (1.1, 2.2, 3.3)


# In[ ]:


b


# ## Tuples
# sama dengan List bedanya data tidak dapat dimodifikasi/ edit.
# Contoh data bulan (data yang sudah pasti/ fix) dengan tujuan agar tidak dapat diubah, untuk data yang penting/ secure.

# In[ ]:


t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
t


# In[ ]:


t[0]


# In[ ]:


t[-1]


# In[ ]:


t[0] = 'newValue'


# ### Dictionary
# tidak butuh order, hanya butuh

# In[ ]:


identitas = {
    'Fname': 'Titis',
    'Lname': 'Pradhitya',
    'Age' : 24
}


# In[ ]:


identitas


# In[ ]:


identitas['Age']


# In[ ]:


identitas['Fname']


# In[ ]:


identias['Alamat']


# In[ ]:


identitas['Pekerjaan'] = 'Karyawan BUMN'


# In[ ]:


identitas


# In[ ]:


identitas['Pekerjaan']


# In[ ]:


identitas['Pekerjaan'] = 'Data Scientist'


# In[ ]:


identitas


# In[ ]:


del identitas['Pekerjaan']


# In[ ]:


identitas


# In[ ]:


person = {}


# In[ ]:


type(person)


# In[ ]:


person['fname'] = 'Nama depan'
person['lname'] = 'Nama belakang'
person['age'] = 30
person['children'] = ['Anak 1', 'Anak 2', 'Anak 3']


# In[ ]:


person


# In[ ]:


person['pets'] = {'dog': 'dogName', 'cat': 'catName'}


# In[ ]:


person


# In[ ]:


person['age']


# In[ ]:


person['children']


# In[ ]:


person['children'][1]


# In[ ]:


person['children'][0]


# In[ ]:


person['pets']


# In[ ]:


person['pets']['cat']


# In[ ]:


d = [1,2,3,[4,5,6],7]


# In[ ]:


d[3]


# In[ ]:


d[3][0]


# In[ ]:


d = {'a': 10, 'b': 20, 'c': 30}


# In[ ]:


# keys
d.keys()


# In[ ]:


# values
d.values()


# In[ ]:


# Python Statements

print('Hello World!')

x = [1,2,3]


# In[ ]:


# Line Continuation

person1_age = 42
person2_age = 16
person2_age = 65

someone_is_of_working_age = (person1_age >= 18 and person1_age <= 65) or (person2_age >= 18 and person2_age <= 65) or (person3_age >= 18 and person3_age <= 65)
someone_is_of_working_age


# In[ ]:


someone_is_of_working_age = (
    (person1_age >= 18 and person1_age <= 65) or
    (person2_age >= 18 and person2_age <= 65) or
    (person3_age >= 18 and person3_age <= 65)
)

someone_is_of_working_age


# In[ ]:


a = [[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9]]


# In[ ]:


a


# In[ ]:


a = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


# In[ ]:


a


# In[ ]:


s = 
    'Hello World!'


# In[ ]:


s =     'Hello World!'


# In[ ]:


s


# In[ ]:


# Multiple Statements per Line

x = 1; y = 2; z = 3

print(x); print(y); print(z)


# In[ ]:


# Comments

a = ['foo', 'bar']# i am a comment


# In[354]:


a


# In[355]:


b = '# im not a comment'


# In[356]:


b


# In[357]:


"""
Initialize value for radius of circle

Then calculate the area of the circle
and display the result to the notebook
"""

pi = 3.14
r = 12

area = pi * (r ** 2)
print('The area of circle is', area)


# In[358]:


pi=3.14
pi = 3.14


# ### Conditional

# In[359]:


# If Statement

x = 0
y = 5

if x < y:
    print('yes')
    
if y < x:
    print('yes')
    
if 'aul' in 'grault':
    print('yes')


# In[360]:


if <exprs>:
    <sttm>
    <sttm>
    <sttm>
    
<statement>


# In[ ]:


if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement')
    print('...')
    print('Done')
    
print('after conditional')


# In[ ]:


if 'bar' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement')
    print('...')
    print('Done')
    
print('after conditional')


# In[ ]:


if 'foo' in ['foo', 'bar', 'baz']:
    print('Outer condition is true')
    
    if 10 > 20:
        print('Inner Condition')
        
    print('Between inner conditions')
    
    if 10 < 10:
        print('Inner Condition 2')
        
    print('End of outer condition')
    
print('After outer condition')


# In[ ]:


# else and elif

if <expr>:
    <statement>
else:
    <statement>


# In[ ]:


x = 20

if x < 50:
    print('x is small')
else:
    print('x is large')


# In[ ]:


x = 20

if x >50:
    print('x is small')
else:
    print('x is large')


# In[ ]:


if <expr>:
    <statement>
elif <expr>:
    <statement>
elif <expr>:
    <statement>
...
else:
    <statement>


# In[ ]:


name = 'Inalum'

if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Inalum':
    print('Hello Inalum')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print('I dont know')


# In[ ]:


name = 'Hacktiv8'

if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Inalum':
    print('Hello Inalum')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print('I dont know')


# In[ ]:


if 'a' in 'bar':
    print('right')
elif 1/0:
    print('wrong')
elif var:
    print('wrong also')


# In[ ]:


# One Line if Statements

if <expr>:
    <statement>
    
if <expr>: <statement>

if <expr>: <statement1>; <statement2>; <statement3>; <statement4>


# In[ ]:


if 'f' in 'foo': print('1'); print ('2'); print('3')


# In[ ]:


x = 2

if x == 1: print('foo'); print('bar')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')


# In[ ]:


x = 2

if x == 1: 
    print('foo')
    print('bar')
elif x == 2: 
    print('qux')
    print('quux')
else: 
    print('corge')
    print('grault')


# In[ ]:


## Ternary Operator (Conditional Expression)

<exprl> if <condt_expr> else <expr2>


# In[ ]:


age = 17

'teen' if age < 21 else 'adult'


# In[ ]:


age = 21

'teen' if age < 21 else 'adult'


# In[ ]:


if a > b:
    m = a
else:
    m = b
    
m = a if a > b else b


# In[ ]:


## Pass statement

if True:
    pass
print('foo')


# In[ ]:


## while

while <expr>:
    <statement>


# In[371]:


n = 5

while n > 0: #akan loop terus menerus hingga menemukan false
    n -= 1
    print(n)


# In[372]:


# break dan continue>


# In[373]:


n = 5

while n > 0: # 4
    n -= 1 # 4 3 3
    if n == 2: # 4 !=2
        break # pass
    print(n) # 4 3
print('Loop Ended')


# In[374]:


n = 5

while n > 0: # 4
    n -= 1 # 4 3 3
    if n == 2: # 4 !=2
        continue # pass
    print(n) # 4 3
print('Loop Ended')


# In[375]:


# else clause

while <expr>:
    <statement>
else:
    <additional_statement>


# In[ ]:


n = 5

while n > 0:
    n -= 1 
    print(n)
else:
    print('Loop Done')


# In[ ]:


n = 5

while n > 0:
    n -= 1 
    if n == 2:
        break
    print(n)
else:
    print('Loop Done')


# In[ ]:


# One - line while loops

n = 5

while n > 0: n -= 1; print(n)


# In[ ]:


# For Loops

for <var> in <iterable>:
    <statement>


# In[ ]:


a = ['foo', 'bar', 'baz']

for i in a:
    print(i)


# In[387]:


d = {'foo': 1, 'bar': 2, 'baz': 3}

for k in d:
    print(k)


# In[388]:


for k in d:
    print(d[k])


# In[389]:


d['foo']


# In[390]:


for v in d.values():
    print(v)


# In[391]:


# range function

x = range(100)


# In[392]:


x


# In[393]:


for n in x:
    print(n)


# In[394]:


# break continue


# In[395]:


for i in ['foo', 'bar', 'baz', 'qux']:
    if 'z' in i:
        break
    print(i)


# In[396]:


for i in ['foo', 'bar', 'baz', 'qux']:
    if 'z' in i:
        continue
    print(i)


# In[397]:


# else clause

for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('done')


# In[398]:


for i in ['foo', 'bar', 'baz', 'qux']:
    if 'z' in i:
        break
    print(i)
else:
    print('Done')


# In[421]:


temp = input("Ketikan temperatur yang ingin dikonversi, eg. 45F, 28C: ")
degree = int(temp[:-1])
i_convertion = temp[-1]

if i_convertion == 'C':
    result = int(round((9 * degree) / 5 + 32))
elif i_convertion == 'F':
    result = int(round((degree - 32) * 5 / 9))
else:
    print("Masukan input yang benar")
    
print("Temperaturnya adalah", result)


# In[422]:


temp


# In[423]:


result


# In[2]:


while True:
    msg = input("Ketikan karakter: ").lower()
    print(msg)
    if msg == 'stop':
        break


# In[ ]:




