import random 

name = ['Richard', 'Ricardo']
residence = ['Britain', 'Mexico', 'France']
job_place = ['call center', 'grocery store', 'hotel']
print(f'This is {random.choice(name)}, he lives in {random.choice(residence)} and he works at a {random.choice(job_place)}')

#Card picking
cards = ["Spades", "Clubs", "Diamonds", "Hearts"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "King", "Queen", "Jack", "Ace"]

def pick_a_card():
    card = random.choice(cards)
    rank = random.choice(ranks)
    print(f'The {rank} of {card}')

pick_a_card()

#Story generator
import random

when = ['Five days ago', 'A year ago', 'On Sep 13th']
who = ['a young boy', 'an old lady', 'a cat']
residence = ['London', 'Paris', 'Washington']
went = ['went to the store', 'went to the restaraunt', 'went to the park']
objetive = ['find a store', 'eat', 'take a walk']

print(f"{random.choice(when)}, {random.choice(who)}, who lived in {random.choice(residence)}, {random.choice(went)}, to {random.choice(objetive)}")

#Password length test
#passlen = int(input("Enter the length of the password: "))
#keys = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
#p = ''.join(random.sample(keys, passlen))
#print(p)

#random randint dice roll
print("This is a dice roll simulator")
play = input("Do you want to play?")
roll_again = 'yes'
while roll_again == 'yes' or roll_again == 'y':
    if play == 'y' or play == 'Y':
        print("Alright, let's roll the dices.")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"The values are:\n{dice1}\n{dice2}")
    else:
        print("Oh well, come back if you want to play.")
        break

    roll_again = input("Wanna roll again?")
   
    