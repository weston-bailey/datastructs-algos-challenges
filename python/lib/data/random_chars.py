import random 
import math
import string

# returns a random list of integers with a specified length
def random_ints(length, **kwargs):
  uneven = kwargs.get('uneven', False)
  type_of = kwargs.get('type_of', 'int')
  negative = kwargs.get('negative', False)

  types = {
    'int': 'something',
    'float': 'something',
    'char': 'something',
  }

  random_ints = []

  while len(random_ints) < length:
    random_ints.append(random.randrange(0, length, 1))
  
  if uneven:
    for i in range(len(random_ints)):
      coin_toss_high = random.random()
      coin_toss_low = random.random()
      if coin_toss_high >= .9:
        random_ints[i] *= random_ints[i]
      if coin_toss_low <= .1:
        random_ints[i] //= random_ints[random.randrange(0, length, 1)] + 1

  return random_ints

def random_ints_negetive(length):
  random_ints = []

  while len(random_ints) < length:
    if random.random() > .5:
      random_ints.append(random.randrange(0, length, 1))
    else:
      random_ints.append(random.randrange(0, length, 1) * -1)


  
  return random_ints


# returns a random list of integers with a specified length
# optional arg is how many decimal places
def random_floats(length, *args, **kwargs):
  uneven = kwargs.get('uneven', False)
  random_floats = []

  while len(random_floats) < length:
    random_floats.append(random.random() * length)
  
  # format the decimal places if argument is present
  if args:
    for i in range(len(random_floats)):
      random_floats[i] = round(random_floats[i], args[0])

  if uneven:
    for i in range(len(random_floats)):
      coin_toss_high = random.random()
      coin_toss_low = random.random()
      if coin_toss_high >= .9:
        random_floats[i] *= random_floats[i]
      if coin_toss_low <= .1:
        random_floats[i] //= random_floats[random.randrange(0, length, 1)] + 1
  

  return random_floats


def random_letters(length):
  random_letters = []

  while len(random_letters) < length:
    random_letters.append(random.choice(string.ascii_letters))
  
  return random_letters