import random
import string

def num_generator(size = 20 , chars = string.ascii_letters + string.ascii_lowercase):
    return ''.join(random.choice(chars) for i in range(size))
