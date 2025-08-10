questions = ["What is 5 + 3?", "What is 12 − 4?", "What is 9 × 2?", "What is 15 ÷ 3?", "What is the square of 6?"]
answers = { 1: 8, 2: 8, 3: 18, 4: 5, 5: 36 }
points = 0
for index, question in enumerate(questions, start=1):
    print(question)
    answer = int(input("What's the answer?\n>>> "))
    if answers.get(index) ==  answer:
        print("Correct!\nYou get 1 point!")
        points += 1
    else:
        print("Wrong!")
print(f"Your total points count is: {points} out of {len(questions)}")

#TODO add more questions