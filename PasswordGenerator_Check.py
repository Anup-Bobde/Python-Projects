# This is a demo of password generator project in TKinter of P.Senapathi sir

import random
import string

p=['a','b','c','d']

for _ in range(6):
    p.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))

for i in range(len(p)):
    print(p[i])


