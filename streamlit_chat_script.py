import openai
from api_key import openai_api_key
import pandas as pd
from datetime import datetime

openai.api_key = openai_api_key

def get_response(messages, temperature) :
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=temperature
    )
    return response["choices"][0]["message"]

def save_information(input_string, index_value, csv_path) :
    index_map = {"name":1, "email":2, "phone":3, "address":4, "dob":5, "education":6}
    
    try:
        result_dict = eval(input_string)
        
        if isinstance(result_dict, dict):
            
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
    