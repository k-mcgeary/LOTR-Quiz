print('Welcome to the Lord of the Rings quiz!')

playing = input('Do you wish to take on the burden of The One Ring? ')

if playing.lower() != 'yes':
    quit()

print('Proceed cautiously...')
score = 0

question = input('Where must the ring be destroyed? ')
if question.lower() == 'mount doom':
    print('The journey continues!')
    score += 1
else:
    print('The Eye is upon you!')

question = input('Who is the next king of men? ')
if question.lower() == 'aragorn':
    print('The journey continues!')
    score += 1
else:
    print('The Nazgul approach!')

question = input('What fell beast slowed the Fellowship in Moria? ')
if question.lower() == 'the balrog':
    print('The journey continues!')
    score += 1
else:
    print('You\'ve slipped into the bog!')

question = input('Who is the Dark Lord? ')
if question.lower() == 'sauron':
    print('The journey continues!')
    score += 1
else:
    print('The orcs have caught your scent!')

question = input('Will you cast the ring into the fires? ')
if question.lower() == 'yes':
    print('You\'re burden is finally over!')
    score += 1
else:
    print('The Dark Lord has taken Middle-Earth!')

print('You scored ' + str(score) + ' out of 5')
