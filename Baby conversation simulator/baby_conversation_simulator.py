from random import choice

questions = ["Why is the sky blue ?: ",
             "Why is the rain cold ?: ", "Why should we sleep at night ?:"]
question = choice(questions)
answer = input(question).strip().lower()
while answer != 'Just because'.lower():
    answer = input("Why " + answer + " ?").strip().lower()
print('Oh..okay')
