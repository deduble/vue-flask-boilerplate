import random
import string


def get_random_sequential_characters(length):
  letters_and_digits = string.ascii_letters + string.digits
  return ''.join((random.choice(letters_and_digits) for i in range(length)))
