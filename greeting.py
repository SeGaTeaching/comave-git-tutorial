import random

def create_random_number(a=1,o=100):
    random_number = random.randint(a, o)
    return random_number

if __name__ == '__main__':
    print(create_random_number)
    print("Hallo Welt")

