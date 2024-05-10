import random
questions = [
    ["Where is the K-2 mountain located?",
     "India","Pakistan","Nepal","China",
     2],
    ["What is the capital of Pakistan?",
     "Karachi","Lahore","Islamabad","Peshawar",
     3],
    ["What is the national Language of Pakistan?",
     "Urdu","Punjabi","Sindhi","English",
     1],
    ["Which of the following rivers is the longest in Pakistan?",
     "Chenab River","Jhelum River","Indus River","Sutlej River",
     3],
    ["The major cash crop of Pakistan is?",
     "Sugarcane","Cotton","Rice","Wheat",
     4],
    ["The Thar Desert is located in which province of Pakistan?",
     "Punjab","Balochistan","Sindh","Khyber Pakhtunkhwa",
     3],
    ["The Mohenjo-daro archaeological site is located in which province of Pakistan?",
     "Balochistan","Punjab","Khyber Pakhtunkhwa","Sindh",
     4],
    ["The founder of Pakistan is known as?",
     "Liaquat Ali Khan","Muhammad Iqbal","Allama Iqbal","Muhammad Ali Jinnah",
     4],
    ["The highest mountain peak entirely within Pakistan is?",
     "K2","Tirich Mir","Broad Peak","Gasherbrum",
     2],
    ["The traditional sport of Pakistan is?",
     "Polo","Hockey","Cricket","Kabaddi",
     4],
    ]
# Initial prize money as per levels
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000,320000] # The list contains ten elements, each representing the prize money awarded for correctly answering a question at a specific level in the quiz. The first element (1000) corresponds to the prize money for the first question, and so on.
money = 0 # This line creates a variable named money and initializes it to 0. "money" will keep track of the total amount of money the player has accumulated throughout the quiz.
for i in range(0, len(questions)):  #range(0, len(questions)) creates a sequence of numbers from 0 to the length of the questions list. This ensures the loop repeats over all questions in the list.
    question = questions[i] #Inside the loop, this line get the current question from the questions list.
    print(f"Question for Rs. {levels[i]}") # This line prints a message to the user, displaying the current question number along with the corresponding prize money from the levels list.
    print(question[0]) #It assumes the structure of the questions list where the first element (question[0]) holds the question text itself.
    print(f"a. {question[1]} ") #These lines print the answer options (a, b, c, d) for the current question. They use f-strings to incorporate the corresponding options (question[1], question[2], question[3], and question[4]) from the questions list,
    print(f"b. {question[2]} ")
    print(f"c. {question[3]} ")
    print(f"d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) ")) 

    if (reply == question[-1]):
        print(f"Correct answer, You have won {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000

    else:
        print("Wrong answer!")
        break
     
print(f"Your take home money is {money}")












