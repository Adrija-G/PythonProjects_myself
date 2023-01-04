import random
sn=random.randint(1,10)
guess = None
rnum= sn*30
print(rnum)
time= 0
while guess!= rnum:
    time+=1
    guess= int(input(f'Guess a number: '))
    if guess<rnum:
        print(f'Too low! {time} tries are over! Try a higher value: ')
    elif guess> rnum:
        print(f'Too high! {time} tries are over! Try a lower value!')
    if time>4 and guess!= rnum:
        if time> 4:
            print(f'\n Hint 1: The number is divisible by 3')
            if time> 6:
                print(f'\n Hint 2: The number is divisible by 2')
                if time> 8:
                    print(f'\n Hint 3: The number is divisible by 5')
                    if time> 10:
                        print(f'\n Hint 3: The number is divisible by 6')
    elif guess== rnum:
        print(f'Congrats! You have correctly guessed the number {rnum} in {time} number of tries!!')
        