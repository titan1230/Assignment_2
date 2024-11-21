import json
import random
import os
from typing import Literal

class Quiz:
    
    def __init__(self, variation: Literal["dsa", "dbms", "os"]):
        valid_types = {"dsa", "dbms", "os"}
        
        if variation.lower().strip() not in valid_types:
            raise ValueError("Invalid quiz type!")
        
        self.quiz_data = []
        self.score = 0
        self.current_question = 0
        self.type = variation.lower().strip()

    def load_quiz_data(self):
        filename = "dsa" if self.type == "dsa" else "dbms" if self.type == "dbms" else "os"
        
        if not os.path.exists(f'quizes/{filename}.json'):
            raise FileNotFoundError(f"Quiz file {filename}.json not found!")
        
        with open(f'quizes/{filename}.json', 'r') as file:
            quiz_data = json.load(file)["quiz_data"]
            
        selected_data = random.sample(quiz_data, 5)
        random.shuffle(selected_data)
        self.quiz_data = selected_data
    
    def start_quiz(self):

        self.load_quiz_data()
        
        while self.current_question < 5:
            question = self.quiz_data[self.current_question]
            print(f"{self.current_question + 1}> {question['question']}")
            
            for i, option in enumerate(question['options'], 1):
                print(f"{i}. {option}")
            
            answer = input("Enter your answer: ")
            
            if not answer.isdigit() or int(answer) not in range(1, 5):
                print("Invalid Answer!")
                continue
            
            answer = int(answer)
            
            if question["options"][answer - 1] == question['answer']:
                self.score += 1
            
            self.current_question += 1
            
        print(f"Quiz Completed! Your score is {self.score}/5")
        self.current_question = 0