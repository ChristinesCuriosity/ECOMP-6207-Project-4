#This is a choose your own adventure game!

import time
print('Welcome to the Carney Christmas Adventure Game!')
print('~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~*~~')
print('On a farm in the rural hills of the Berkshires, you awake on Christmas morning.')
print('It is quiet, the sun has yet to rise, but the dawn light illuminates your farmhouse bedroom.\n')
time.sleep(6)
print('You can take one item with you -')
print('phone, slippers, or book.\n')
item = input('What do you choose?: ').lower().strip()
while not (item == 'phone' or item == 'slippers' or item == 'book'):
    print('You go back to bed, it\'s too early to be awake.')
    item = input('The End.')
if item == 'phone':
    print('One can never be too far from one\'s '+item+'\n')
    time.sleep(3)
elif item == 'slippers':
    print('You can\'t have Christmas without '+item+'! Good choice.\n')
    time.sleep(3)
elif item == 'book':
    print('When you have a '+item+' you are never alone.\n')
    time.sleep(3)

print('Taking your '+item+' with you, you pass by the glowing Christmas tree and the piles of presents.')
print('You head to the kitchen to see if anyone else is awake.')
print('The light over the kitchen sink is on but no one is there.\n')
time.sleep(5)
print('You have two choices, start making the coffee or wait for someone else to do it for you.\n')
coffee = input('Do you make the coffee? y/n: ').lower().strip()
if coffee == 'y':
    print('You pick up the percolator and fill the base with water and the top with coffee grounds.')
    print('You plug it into the wall and peacefully wait in the living room with your '+item+'.\n')
else:
    print('You take your '+item+' and head to the living room to get cozy while you wait for someone else to make the coffee.\n')
time.sleep(6)
print('The glow of the tree is the perfect amount of light to help you feel comfortable as the first rays of the sun crest over the horizon and stream into the room.')
print('It isn\'t long before you hear foot steps on the stairs.')
print('It could be one of the kids coming down to see what Santa brought for them or it could be another adult, awake from routine rather than from the excitement of Christmas morning.\n')
time.sleep(10)
print('You can stay cozy or stand to greet the person coming down the stairs.')
kids = input('Do you stay or stand?:').lower().strip()
while kids == 'stand':
    print('You go to stand but find that the cozy nature of your chair keeps you held in place.')
    print('Do you listen to the call of the cozy or do you fight the cozy and try to stand again?')
    kids = input('Do you stay or stand?:')
print('You decide to stay cozy and the footsteps come closer.')

