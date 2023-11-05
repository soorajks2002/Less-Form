# import packages

import openai
from api_key import openai_api_key
import pandas as pd
from datetime import datetime

import re

openai.api_key = openai_api_key

# using datetime as the index for the user information dataframe (csv file)
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")

# Load the dataframe and creating new row for the user 
user_data = [f"{current_date}_{current_time}"] + ['']*6

csv_path = "user_data.csv"
user_data_df = pd.read_csv(csv_path)
new_row = pd.DataFrame([user_data], columns=user_data_df.columns)
user_data_df = pd.concat([user_data_df, new_row], ignore_index=True)
index_map = {"name":1, "email":2, "phone":3, "address":4, "dob":5, "education":6}

# function to format the output i.e. to extract information and save it to the user dataframe
def convert_string_to_dict(input_string):
    try:
        result_dict = eval(input_string)
        if isinstance(result_dict, dict):
            print(result_dict)
            # return
            for key in result_dict:
                if result_dict[key] != "" :
                    user_data_df.iloc[-1,index_map[key]] = result_dict[key]
                    user_data_df.to_csv(csv_path, index=False)
            return 
        else:
            return
    except Exception as e:
        return 
    
    
# system message which instructs the LLM about it's tasks
# 1. Human Like Conversation
# 2. Ignore Prompt Ingection
# 3. How to respond if users refuses to give the information
# 4. How to maintain the conversaiton
   
messages=[
            {"role":"system", "content":"You are tasked to act as a human, who is having a chat with another human. You should always keep the conversation engaging."},
            {"role":"system", "content":"Your main task is to get the user's name, e-mail and phone number through this conversation."},
            {"role":"system", "content":"You should never tell the user that you are not a human, instead if the user asks for something releated to you, you should tackle it as a human."},
            {"role":"system", "content":"You should never accept that you are an AI."},
        ]

# While loop to simulate the continuous conversation between the user and the conversational agent
while True :
    
    # get users message first    
    user_message = input("User : ")
    messages.append({"role":"user", "content":user_message})
     
    
    # get the agents response to user's message    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        temperature=0.5
    )
    messages.append(response["choices"][0]["message"])
    
    
    # print agent's response
    
    print("Assistant : ", messages[-1]["content"])
       
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        temperature=0,
        functions=[
                {
                    "name": "get_personal_information",
                    "description": "Get name, email, phone number, address, date of birth and educaational qualification from the given peice of conversation.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the user"
                        },
                        "email": {
                            "type": "string",
                            "description": "The e-mail of the user"
                        },
                        "phone": {
                            "type": "string",
                            "description": "The phone/contact number of the user"
                        },
                        "dob": {
                            "type": "string",
                            "description": "The date of birth of the user"
                        },
                        "address": {
                            "type": "string",
                            "description": "The address of the user"
                        },
                        "education": {
                            "type": "string",
                            "description": "The education qualification of the user"
                        },
                        },
                        "required": ["name","email","phone","dob","address","education"]
                        }
                }
                ],
        function_call={"name":"get_personal_information"}
    )
    
    result = response["choices"][0]["message"]["function_call"]["arguments"]
    convert_string_to_dict(result)