import random

list = ["hello", "please","dog","cat"]

a = random.choice(list)
count = len(a)

a.split()

print(a,"length =", len(a))

list1 = []
for k in range(1,len(a)+1):
 list1.append('_ ')
print(list1)

while(count != 0):
 i = 0
user = input("Guess the letter")
while(i!=len(a)):

 if(a[i] == user):
  list1[i] = a[i]
count = count - 1
i = i + 1
print(list1)

print("Congratulation you WON !!!!!!")