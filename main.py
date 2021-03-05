import random

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy',
           'Try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']


name = input('What is your name? ')
print('Hello ' + name + '!')


def magicball():
    print('Ask me a question!')
    input()
    print(random.choice(answers))
    replay()


def replay():
    print('Do you have another question? (Y/N)')
    reply = input().lower()
    if reply == 'y':
        magicball()
    elif reply == 'n':
        exit()
    else:
        print('Please repeat your answer')
        replay()


magicball()
