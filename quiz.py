
# Python Online Quiz System
# A multiple-choice General Knowledge Quiz

questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": ["A. Charles Babbage", "B. Alan Turing",
                    "C. Bill Gates", "D. Steve Jobs"],
        "answer": "A"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean",
                    "C. Pacific Ocean", "D. Arctic Ocean"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol of Gold?",
        "options": ["A. Ag", "B. Au", "C. Fe", "D. Cu"],
        "answer": "B"
    },
    {
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "options": ["A. Germany", "B. Italy",
                    "C. France", "D. Canada"],
        "answer": "C"
    },
    {
        "question": "Who developed the Python programming language?",
        "options": ["A. James Gosling", "B. Guido van Rossum",
                    "C. Dennis Ritchie", "D. Bjarne Stroustrup"],
        "answer": "B"
    },
    {
        "question": "Which is the smallest prime number?",
        "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "answer": "C"
    },
    {
        "question": "Which organ pumps blood throughout the human body?",
        "options": ["A. Brain", "B. Lungs",
                    "C. Liver", "D. Heart"],
        "answer": "D"
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["A. 1945", "B. 1947", "C. 1950", "D. 1952"],
        "answer": "B"
    },
    {
        "question": "Which data structure follows FIFO?",
        "options": ["A. Stack", "B. Tree",
                    "C. Queue", "D. Graph"],
        "answer": "C"
    }
]

score = 0

print("=" * 45)
print("       WELCOME TO THE ONLINE QUIZ SYSTEM")
print("=" * 45)

print("\nInstructions:")
print("1. There are 10 multiple-choice questions.")
print("2. Each correct answer gives 1 mark.")
print("3. Enter A, B, C or D to answer.\n")

for number, question in enumerate(questions, start=1):

    print("-" * 45)
    print(f"Question {number}: {question['question']}")

    for option in question["options"]:
        print(option)

    while True:
        user_answer = input("\nEnter your answer (A/B/C/D): ").strip().upper()

        if user_answer in ["A", "B", "C", "D"]:
            break

        print("Invalid input! Please enter A, B, C or D.")

    if user_answer == question["answer"]:
        print("Correct answer!")
        score += 1
    else:
        print("Incorrect answer!")
        print("Correct answer:", question["answer"])

percentage = (score / len(questions)) * 100

print("\n" + "=" * 45)
print("             QUIZ RESULT")
print("=" * 45)

print(f"Total Questions : {len(questions)}")
print(f"Correct Answers : {score}")
print(f"Wrong Answers   : {len(questions) - score}")
print(f"Final Score     : {score}/{len(questions)}")
print(f"Percentage      : {percentage:.2f}%")

if percentage >= 80:
    print("Performance: Excellent!")
elif percentage >= 60:
    print("Performance: Good!")
elif percentage >= 40:
    print("Performance: Average!")
else:
    print("Performance: Keep Practicing!")

print("\nThank you for participating!")
print("=" * 45)
