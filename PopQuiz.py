print("Welcome to the pop quiz!!")
print('NOTE: If your spelling has to be correct or else, it will be considered as a wrong answer!')
score = 0
question_no = 0
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}. What does API stand for? ').lower()
    if ques == 'Application Programming Interface':
        score +=1
        print('Correct! You got 1 point!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> Application Programming Interface')

# ------1
    question_no += 1
    ques = input(f'\n{question_no}. What does GPU stand for? ').lower()
    
    if ques == 'graphics processing unit':
        score +=1
        print('Correct! You got 1 point!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> Graphics Processing Unit')

# -----2
    question_no += 1
    ques = input(f'\n{question_no}. What does SEO stand for? ').lower()
    
    if ques == 'Search Engine Optimization':
        score +=1
        print('Correct! You got 1 point!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> Search Engine Optimization')

# -----3
    question_no += 1
    ques = input(f'\n{question_no}. What does HTML stand for? ').lower()
    
    if ques == 'Hyper Text Markup Language':
        score +=1
        print('Correct! You got 1 point')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> Hyper Text Markup Language')


    question_no += 1
    ques = input(f'\n{question_no}. What does ROM stand for? ').lower()
    
    if ques == 'Read Only memory':
        score +=1
        print('Correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> Read Only memory')

else:
    print('Thank you. You are out of the game.')
    quit()

print(f'\nTotal Number of questions is {question_no}')
print(f'Your score is {score}')
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% questions are correct')

print(f'{percentage}% questions are correct.')
