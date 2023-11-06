# import all the required modules

import openai
from api_key import openai_api_key
import pandas as pd
from datetime import datetime

openai.api_key = openai_api_key

# function to call open ai gpt-4 API with the given messages

def assistant_response(messages) :
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        temperature=0.8,
        top_p=0.3,
        frequency_penalty=0.4,
        presence_penalty=0.8
    )
    return response["choices"][0]["message"]


def get_personal_info(message) :
    todays_date = datetime.now().strftime("%d-%m-%Y")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message+[{"role":"user", "content":"Get my personal information from my previous messages."}],
        temperature=0,
        functions=[
                {
                    "name": "get_personal_information",
                    "description": f"Get name, email, phone number, address, date of birth and educaational qualification if present from the given peice of conversation. For date of birth if age is given then calculate date of birth with today's date beign {todays_date}",
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
                            "description": "date of birth of the user in the format DD-MM-YYYY"
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
    
    return response["choices"][0]["message"]["function_call"]["arguments"]


# function to save the personal information from the messages to the specific user id

def save_information(message, index_value, csv_path) :
    
    personal_info = get_personal_info(message)
    
    index_map = {"name":1, "email":2, "phone":3, "address":4, "dob":5, "education":6}
    
    try:
        result_dict = eval(personal_info)
        
        if isinstance(result_dict, dict):
            
            if result_dict['name'] == 'John Doe' and result_dict['email'] == 'johndoe@example.com' or result_dict['name']=='N/A':
                return
            
            user_data_df = pd.read_csv(csv_path)
            
            row_index = user_data_df[user_data_df.iloc[:, 0] == index_value].index[0]

            for key in result_dict:
                if result_dict[key] != 'not present' :

                    user_data_df.iloc[row_index,index_map[key]] = result_dict[key]
                    user_data_df.to_csv(csv_path, index=False)
                    
            return 
        else:
            return
    except Exception as e:
        return
    