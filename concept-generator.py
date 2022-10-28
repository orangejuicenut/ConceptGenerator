from nltk.corpus import wordnet as wn
import random

nouns = list(wn.all_synsets(wn.NOUN))

nounlen = len(nouns)

numConcepts = 5

for i in range(numConcepts):
    word1raw = nouns[random.randrange(0,nounlen)].name()
    word2raw = nouns[random.randrange(0,nounlen)].name()
    word1 = word1raw.split('.')[0]
    word2 = word2raw.split('.')[0]
    print(word1+ ' - ' + word2)

