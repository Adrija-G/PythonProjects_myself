import random 
from random import randint
age= random.randint(10,90)
adj1= input("Adjective: \n")
adj2= input("Adjective: \n")
pr= input("Pronoun: \n")
v= input("Verb:\n") 
n= input("Noun:\n")
hobby= input("Hobby: \n")
q= input("Enter any quote: \n")
job= input("Enter name of any profession\n")
name= input("Name:\n")
print(f"The name is {name} and at {age} years old, {pr} is/are a {job}, but also loves {hobby}. {name} spends all the time {v} nothing. {name} believes that {q}")
print(f"According to {name}, pursuing {hobby} is very {adj2}. People love {name} as {pr} is/are an expert {adj1} and {adj2} {job}. After all, {q}")