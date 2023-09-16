"""
fruits = {'apple','orange','banana','pineapple' }
print(fruits)
"""

# namedtuple()
#importing namedtuple()
"""
from collections import namedtuple

a = namedtuple('courses','name,technology')
#s=a('web dev','python')
#print(s)
s= a._make(['artificial intelligence','python'])
print(s)
"""
# deque
"""
from collections import deque
a= ['e','r','n','e','s','t']
d= deque(a)
print(d)
d.append('python')
print(d)
d.insert(2,'w')
print(d)
#appendleft is used to add something to the start of the list
d.pop()
print(d)
d.popleft()
print(d)


# chainmap

from collections import ChainMap
a = {1:'ernest' , 2:'arthur'}
b = {3:'wilson' , 4:'exhibit'}
m = ChainMap(a,b)
print(m)


# counter
from collections import Counter
a = [1,1,2,3,2,2,4,5,4,5,4,3,6,2,2]
d = Counter(a)
print(d)

print(list(d.elements()))
print(d.most_common())
sub = {2:1 , 6:1}
print(d.subtract(sub))
print(d.most_common())
print(d)


# OrderedDict
from collections import OrderedDict 
d = OrderedDict()
d[1] = 'w'
d[2] = 'i'
d[3] = 'l'
d[4] = 's'
d[5] = 'o'
d[6] = 'n'
print(d)
print(d.keys())
print(d.items())


# DefaultDict
from collections import defaultdict
a = defaultdict(int)
a[1] = 'python'
a[2] = 'web dev'
print(a)


# ARRAY
# LOOPING
# FOR LOOP

import array as arr
a = arr.array('d', [1.1,2.2,3.3,4.4,5.5])
print('all values')
#for x in a :
  #  print(x)
for x in a[0:4] :
    print(x)
    

    # WHILE LOOP
import array as arr
a = arr.array('d', [1,2,3,4,5,6])
b = 0

while b<len(a):
    print(a[b])
    b = b+1
   
 """

    # HASH TABLE
    #DICTIONARIES
    #Using curly braces
#my_dict = {'name':'Ernest', 'age':'97'}
#print(my_dict)

# using dict()
#new_dict = dict(ernest='boy', wilson='yes')
#print(new_dict)

# NESTED DICTIONARIES
stud_details = {'Students': {'Ernest': {'ID':'2000', 'portfolio':'class rep'},'Wilson':{'ID':'2001', 'portfolio':'Deputy class rep'}}}
#print(stud_details)


"""
 # performing operations on hash tables
# Accessing items
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('name'))
print(my_dict.get('age'))

for x in my_dict:
    print(x)

for x in my_dict.values():
    print(x)

for x in my_dict.keys():
    print(x)


for x,y in my_dict.items():
    print(x,y)

"""



# updating
#my_dict['name'] = 'Exhibit'
#my_dict['age']  = '98'
#print(my_dict)


# Deleting
#my_dict.pop('name')
#print(my_dict)
#print(my_dict.popitem())

#del my_dict['age']
#print(my_dict)

"""
#converting dictionary into a dataframe
import pandas as pd
df = pd.DataFrame(stud_details['Students'])
print(df)



# WHILE LOOP
count = 0
while count < 20:
    print("Number:",count)
    count =  count + 2
print("That's correct")    




# A guessing game
import random
n = 30
Number_to_be_guessed = int(n * random.random()) + 1
guess = 0

while guess != Number_to_be_guessed:
    guess = int(input("enter your guess here: "))

    if guess > 0:
        if guess > Number_to_be_guessed:
            print("Your guess is too large")
        
        elif guess < Number_to_be_guessed:
            print("Your guess is too small")
    
    else:
        print("Keep trying!")
        break

else:
    print("Congratulations. You finally made it!")

   


    # FOR LOOP
names_of_students = ["Ernest","Arthur","Exhibit","Wilson","Patience","Josephine","Caleb","Bervelyn"]
for name in names_of_students:
    print("Student's name:",name)
print("That's one of the students")


# finding factorial of a number
Number = int(input("Type your number here: "))
factorial = 1

if Number < 0:
    print("Your number must be positive")

elif Number == 0:
    print("factorial = 1")

else:
    for a in range(1,Number + 1):
        factorial = factorial * a
print("The factorial of your number is: ", factorial)
 


 # NESTED LOOP
 #simulatng a bank ATM
print("Welcome to my bank's ATM")
restart = ('Y')
chances = 3
balance = 100

while chances >= 0:
    pin = int(input('please enter your 4 digit pin: '))

    if pin == (6789):
        print("You've entered a correct pin: \n")

        while restart not in ('n','NO','no','N'):
            print('Press 1 for your balance\n')
            print('Press 2 to make a withdrawal\n')
            print('Press 3 to deposit\n')
            print('Enter 4 to return card\n')

            option = int(input('What would you like to choose? '))
            if option == 1:
                print('Your balance is $',balance,'\n')
                restart = input('Would you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print("Thank you")
                    break

            elif option == 2:
                option2 = ('y')
                withdrawal = float(input("How much would you like to withdraw? "))
                if withdrawal in [10,20,40,60,80,100,120]:
                    balance = balance - withdrawal
                    print("\nYour balance is now $",balance)
                    restart = input("Would you like to go back? ")
                    if restart in ('n','NO','no','N'):
                        print("Thank you")
                        break

                elif withdrawal != [10,20,40,60,80,100,120]:
                    print("Invalid amount, please retry\n")
                    restart = ('y')
                elif withdrawal == 1:
                    withdrawal = float(input("Please enter desired amount:"))

            elif option == 3:
                Deposit = float(input("How much would you like to deposit? "))
                balance = balance + Deposit
                print("\nYour balance is now $",balance)
                restart = input("Would you like to go back? ")
                restart = input("Would you like to go back? ")
                if restart in ('n','NO','no','N'):
                    print("Thank you")
                    break

            elif option == 4:
                print("Please wait whilst your card is returned...\n")
                print("Thank you for your service")
                break

            else:
                print("Please enter a correct number.\n")
                restart = ('y')

    elif pin != ('6789'):
        print("Incorrect password")
        chances = chances - 1
        if chances == 0:
            print("\nYou cannot try again")
            break
      


        # Nested for loop
        #printing pythagorean values within a specific number

from math import sqrt
n = int(input("Enter the maximal value: "))
for a in range(1, n + 1):
    for b in range(a, n):
        c_square = a ** 2 + b ** 2
        c = int(sqrt(c_square))
        if ((c_square - c**2) ==0):
            print(a, b, c)
     
 """

     # using a for loop inside a while loop
print("Do you want to enter the records of people travelling?") 
Traveling = input("Yes or No: ")
while Traveling == 'yes':
    num = int(input("Number of people traveling: "))
    for num in range(1, num + 1):
        name = input("Name: ")

        age = int(input("Age: "))

        sex = input("Male or Female: ")

        print(name)
        print(age)
        print(sex)

    Traveling = input("Oops! forgot someone ?: ")
