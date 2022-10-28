import random

numConcepts = 5

nouns = [
    "Knight",
    "Maid",
    "Housewife",
    "Nun",
    "Cheerleader",
    "Boxer",
    "Teacher",
    "Nurse",
    "Astronaut",
    "Pilot",
    "Librarian",
    "Farmer",
    "Barmaid",
    "Dealer",
    "Office lady",
    "Sniper"]

nounlen = len(nouns)



for i in range(numConcepts):
    word1 = nouns[random.randrange(0,nounlen)]
    word2 = nouns[random.randrange(0,nounlen)]
    print(word1+ ' - ' + word2)