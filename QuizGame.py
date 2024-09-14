# mentions the quiz questions
My_quiz_questions = (
    "Which planet is known as the Red Planet?",
    "Which physicist is known for the theory of general relativity?",
    "What is the value of the derivative of the function f(x) = x^3 + 5x^2 - 3x + 2 at x = 1?",
    "Who was the Prime Minister of the United Kingdom during the Falklands War?",
    "In which Shakespeare play would you find the character Iago?"
)
#shows the quiz options
My_quiz_answer_options = (
    ('1. Mercury', '2. Venus', '3. Earth', '4. Mars'),
    ('1. Isaac Newton', '2. Albert Einstein', '3. Niels Bohr', '4. Galileo Galilei'),
    ('1. 2.4', '2. 4.8', '3. 6', '4. 10'),
    ('1. Winston Churchill', '2. Margaret Thatcher', '3. Tony Blair', '4. David Cameron'),
    ('1. Othello', '2. Hamlet', '3. Macbeth', '4. King Lear')
)
#stores the correct options
answers = ('4', '2', '3', '2', '1')

# Initialize score and guesses
score = 0
guesses = []
question_number=0

# Iterate over questions and answer options
for question in My_quiz_questions:
    print("***********************************************************************************")
    print("-----------------------------------------------------------------------------------")
    print(question)
    
    # Print the answer options for the current question
    for option in My_quiz_answer_options[question_number]:
        print(option)
    
    while True:  # Loop until a valid input is provided
        try:
            # to get the answer of user
            user_answer = input("Please enter the answer number (1, 2, 3, 4): ")
            
            # Check if the answer is valid
            if user_answer not in {'1', '2', '3', '4'}:
                print("Invalid input. Please enter a number from 1 to 4.")
                continue
            
            # Check if the user's answer is correct
            if user_answer == answers[question_number]:
                print("Correct!")
                score += 1
            else:
                print(f"Sorry! The correct answer was option {answers[question_number]}.")
            
            # Append the guess of user to the list
            guesses.append(user_answer)
            
            # Exit the loop after the answer is provided
            break
        
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
    question_number+=1

# display the result of user
print("***********************************************************************************")
print("Quiz complete!")
print(f"Your total point is {score} out of {len(My_quiz_questions)}.")
