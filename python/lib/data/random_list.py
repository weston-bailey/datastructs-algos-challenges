from random import choice, random, randrange
from string import ascii_letters

def random_list(**kwargs):
  '''
    random_list(type_of=str, length=int, uneven=bool, negative=bool, decimal_place=bool): -> list:\n
    returns a random list of flpoats, integers, or characters based of keyword args\n
    type_of: the type the should be in list. Default: 'int', can also be 'char' or 'float'\n
    length: integer value representing length of the list of the to return. Defualt: 10\n
     ~~ Number only kwargs: ~~\n
    uneven: boolean value that dertermines if there are large gaps between values in the list. Defualt: False\n
    decimal_place: integer value that determins where to round the floats to (ex. 4 = 3.4567) Defualt: 0 (off) -- nn roundign on floats\n
    negative: boolean value that determins whether to include negatives in the list. Defualt: False\n
  '''
  length = kwargs.get('length', 10)
  uneven = kwargs.get('uneven', False)
  type_of = kwargs.get('type_of', 'int')
  negative = kwargs.get('negative', False)
  decimal_place = kwargs.get('decimal_place', False)

  random_list = []

  # char type returns early
  if type_of == 'char':
    while len(random_list) < length:
      random_list.append(choice(ascii_letters))

    return random_list

  while len(random_list) < length:
    random_list.insert(0, random() * length)
    if negative and random() > .5: random_list[0] *= -1
    if decimal_place: random_list[0] = round(random_list[0], decimal_place)
    if uneven:
      coin_toss_high = random()
      coin_toss_low = random()
      if coin_toss_high >= .9:
        random_list[0] *= random_list[0]
      if coin_toss_low <= .1:
        random_list[0] /= random_list[randrange(0, length, 1)] + 1
    if type_of == 'int': random_list[0] = round(random_list[0])

  return random_list