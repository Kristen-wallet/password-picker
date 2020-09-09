import string
import random
while True:
    adjectives = ['brave','calm','fat','high','low','sleepy','white','black','cute','small','danger']
    nouns = ['cow','buffalo','hero','tower','baby','ship','cat','monkey']
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(1,100)
    #special_character = random.choice(string.punctuation)

    print("-----Welcome to the password picker----")
    password = adjective+noun+str(number)
    print("Your password is : %s" %password)
    ans = input("Do you want another password? (y or n)")
    if ans == "n":
        break