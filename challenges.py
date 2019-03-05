#1---------------------------------
alphabet = input('Enter a Letter: ').lower()
alphabet = str(alphabet)
if len(alphabet) > 1:
    print('Try again')
elif alphabet in 'aeiou':
    print(f'letter {alphabet} is a vowel')
else:
    print(f'letter {alphabet} is a consonant')

#2------------------------------------------
print('welcome to string counter')
while word != 'quit':
    word = input('Enter anything: ')
    if word != 'quit':
        print (len(word))
    elif word == 'quit':
        break

#3----------------------------------------------
years = input('Enter a number: ')
years = int(years)
if years <= 2:
    print(f'your dog is {years*10} years old')
elif years >2:
    print(f'Your dog is {(years-2)*7+20} years old')

#4------------------------------------------------
print('Enter the sides of the triangle')
a = input('a: ')
b = input('b: ')
c = input('c: ')
a = int(a)
b = int(b)
c = int(c)
if a == b and b == c:
    print('equalateral triangle')
elif a != b and b != c:
    print('scalene triangle')
elif (a == b and b != c) or (a != b and b == c):
    print( 'isosceles triangles')
    
#5---------------------------------------------------

nterms = 100

n1 = 0
n2 = 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

#6---------------------------------------------------
month = input("month: ").lower()
day = input("day: ").lower()

if month in ('january', 'february', 'march'):
	season = 'winter'
elif month in ('april', 'may', 'june'):
	season = 'spring'
elif month in ('july', 'august', 'september'):
	season = 'summer'
else:
	season = 'error'

if (month == 'march') and (day > 19):
	season = 'spring'
elif (month == 'june') and (day > 20):
	season = 'summer'
elif (month == 'september') and (day > 21):
	season = 'autumn'
elif (month == 'december') and (day > 20):
	season = 'winter'

print(f"{month} {day} is in", season)

