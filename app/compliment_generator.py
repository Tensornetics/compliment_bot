import random

compliments = [
    "You're amazing!",
    "You're a true inspiration.",
    "You're making a difference!",
    "You're a wonderful person.",
    "You light up the room.",
    "You have a great sense of humor.",
    "You're one of a kind.",
    "You're talented and creative."
]


def generate_compliment():
    return random.choice(compliments)
