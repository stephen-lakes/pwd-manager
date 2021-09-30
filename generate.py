import random


def generate_password(desired_length):
    s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[\]^_{|}~"
    generated = ''

    while len(generated) <= desired_length:
        generated += random.choice(s)

    return generated
    