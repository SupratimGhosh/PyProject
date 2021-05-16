import time


print("******Welcome to NUMBER GUESSING GAME******")
print('\n\n')

name=input("May I know your name? \n")
if name==('no' or 'No' or 'NO'):
    print('Uhhhg! No Problem.')
else:
    print('Welcome, ',name)

print('\n\n :::Think of a number between 1 to 100:::')
print('\nOhh No! No! You definately no don\'t have to tell me..')
time.sleep(3)
print('\nAhh Great! I guess you have already guessed a number..')
print('So here\'s my challenge! i\'ll guess your number within 7 tries ', u"\U0001F609")
print('\nPlease press Enter to continue')
x=input()

l,u,c,f=1,100,0,0
m=(l+u)//2
m1=m
while u>l:
    c+=1
    m = (l + u) // 2
    print('\nPress 1 if the number you have guessed is greater than ',m)
    print('Press 2 if the number you have guessed is lesser than ', m)
    print('Press 3 if the number you have guessed is equal to ', m)

    ch=int(input('\nEnter your choice: '))

    if ch==1:
        if(m1-1==m):
            print('\nDon\'t be oversmart!')
            f=1
            break
        l=m+1
    elif ch==2:
        if (m1 + 1 == m):
            print('\nDon\'t be oversmart!')
            f=1
            break
        u=m-1
    elif ch==3:
        print("\n\nGreat! I\'ve guessed your number in ",c,' chances..')
        f=1
        break
    else:
        print('\nSorry! It looks like you have entered a wrong choice.')
        print('Please try again;\n')
        c=c-1
        continue

    m1=m


c+=1
if f==0:
    m=m+1
    print('\nPress 1 if the number you have guessed is greater than ',m)
    print('Press 2 if the number you have guessed is lesser than ', m)
    print('Press 3 if the number you have guessed is equal to ', m)

    ch=int(input('\nEnter your choice: '))
    if ch==3:
        print("\n\nGreat! I\'ve guessed your number in ", c, ' chances..')
        f = 1
    else:
        print('\nDid you just played the game wrong? or were you trying to be oversmart? Ayways!!')


if f==0:
    print("\nWOW! It looks you are smarter than me to guess outside the range.")

print('\n\nIt was great to play with you! Thanks!')
print('Please press Enter to Exit.')
x=input()
