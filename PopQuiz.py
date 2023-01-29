print("Wellcome to quiz game !!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
question_no = 0
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}. what does API stand for? ').lower()
    if ques == 'Application Programming Interface':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> Application Programming Interface')

# ------1
    question_no += 1
    ques = input(f'\n{question_no}. what does GPU stand for? ').lower()
    
    if ques == 'graphics processing unit':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> Graphics Processing Unit')

# -----2
    question_no += 1
    ques = input(f'\n{question_no}. what does SEO stand for? ').lower()
    
    if ques == 'Search Engine Optimization':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> Search Engine Optimization')

# -----3
    question_no += 1
    ques = input(f'\n{question_no}. what does HTML stand for? ').lower()
    
    if ques == 'Hyper Text Markup Language':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> Hyper Text Markup Language')


    question_no += 1
    ques = input(f'\n{question_no}. what does ROM stand for? ').lower()
    
    if ques == 'Read Only memory':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> Read Only memory')

else:
    print('Thank you. You are out of the game.')
    quit()

print(f'\nTotal Number of question is {question_no}')
print(f'Your score is {score}')
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% questions are correct')

print(f'{percentage}% questions are correct.')