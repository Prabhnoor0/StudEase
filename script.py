import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

import google.generativeai as genai
genai.configure(api_key=API_KEY)

def load_resources(file_path):
    try:
        resources = pd.read_excel(file_path)
        return resources
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None

def recommend_resources(quiz_score, subject, topic, resources):
    if quiz_score > 8:
        return "Hurray! You did a great job!"
    
    
    filtered_resources = resources[(resources['subject'] == subject) & (resources['topic'] == topic)]
    
    if filtered_resources.empty:
        return "No resources found for the specified subject and topic."
    
    
    clickable_links = [f'{link}' for link in filtered_resources["links"]]
    
    return clickable_links  

# Example 
file = "data/classs6.xlsx"  
resources = load_resources(file)

if resources is not None:
    quiz_score = 7  
    subject = "Maths"  
    topic = "Playing with Numbers"  

    recommendations = recommend_resources(quiz_score, subject, topic, resources)
    if isinstance(recommendations, list):
        for link in recommendations:
            print(link)  
    else:
        print("no resources found")  