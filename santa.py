import random

import itertools



people = [

    'Tom',

    'Dick',

    'Harry',

    'Jane',

    'Sally',

]



def valid(a, b):

    for i, j in itertools.zip_longest(a, b):

        if i == j: return False

    return True



a = list(people)

b = list(people)



while not valid(a, b):

    random.shuffle(a)

    random.shuffle(b)



for i, j in itertools.zip_longest(a, b):

    print('%s gives a gift to %s.' % (i, j))

#this is a testhttps://github.com/borny25/santa