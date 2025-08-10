import random

choices = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes – definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Don’t count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

answer = random.choice(choices)
question = input("What's your Question?\n>>> ")
print("Your question is: ", question)
print("The magic 8 ball says...")
print(answer)