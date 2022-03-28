import random


vocabulary = ["The Shawshank Redemption", "Titanic", "The Batman",
              "bradd Pit", "Johnny Depp", "Ophra Haza",
              "Hermon", "Masada", "Semuc Champey", "football", "Israel"]

num = random.randint(0, len(vocabulary) - 1)

the_secret_word = vocabulary[num]
