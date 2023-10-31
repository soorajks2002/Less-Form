import openai
from api_key import openai_api_key
import pandas as pd

openai.api_key = openai_api_key

def process_input(input_str):
    # Replace \" with "
    cleaned_input = input_str.replace('\\"', '"')
    
    # Convert "[]" string to Python list []
    converted_list = eval(cleaned_input)
    
    return converted_list
  

messages=[
            {"role":"system", "content":"You are a conversational agent who has been tasked with conversating with a human in human like manner and style. You are supposed to act as human throughout the conversation and your'e response should be relevant to the users queries. And during the conversation you are supposed to extracting personal information like name, e-mail, phone number, address, date of birth and education qualification from the user. You shouldn't ask for these information directly, instead you have to engage in conversation with the user and indirectly ask for it. And very important if the user declines to give his personal information then you shouldn't force them to give instead continue the conversation and try to get other information. Your tone and style should be decided according to the users response."},
           
            # {"role":"system", "content":"You are a chat bot who has been tasked with extracting name, e-mail, phone number, address, date of birth and education from the user. If the user is refusing to answer change your tone according to his response and try to get him to give his details. Your response should always be friend like casual and short."},
            # {"role": "assistant", "content": "May I know your name please ?"},
        ]

result = []

for i in range(10) :
    
    user_message = input("User : ")
    messages.append({"role":"user", "content":user_message})
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.8
    )
    messages.append(response["choices"][0]["message"])
    
    print("Assistant : ", messages[-1]["content"])
    
    
    # check_message = [{"role":"system", "content": "was there any of the required personal information of the user's response ? If yes return it in this format 'key - personal_information' for eg- 'phone no - 9353824992' and make sure the data is in proper format"}]

    # response = openai.ChatCompletion.create(
    #     model = "gpt-4", messages=messages+check_message
    # )
    
    # print("System : ", response["choices"][0]["message"]["content"])
    
    check_message = [{"role":"system", "content": "Is your conversation with user over if yes return 'YES' or else return 'NO'"}]

    response = openai.ChatCompletion.create(
        model = "gpt-4", messages=messages+check_message
    )
    # print(response["choices"][0]["message"]["content"])
    
    if response["choices"][0]["message"]["content"].lower() == "yes":
        check_message = [{"role":"system", "content": "Give me the all the required personal information of the user in this array like format [name, e-mail, phone number, address, date of birth, education]"}]
        response = openai.ChatCompletion.create(
            model = "gpt-4", messages=messages+check_message
        )
        # result = response["choices"][0]["message"]
        # print(result)
        # print(type(result['content']))
        
        result = process_input(response["choices"][0]["message"]["content"])
        # print(result)
        # print(type(result))
        break
    
print("OVER")

csv_path = "user_data.csv"

existing_df = pd.read_csv(csv_path)

new_row = pd.DataFrame([result], columns=existing_df.columns)
existing_df = pd.concat([existing_df, new_row], ignore_index=True)

existing_df.to_csv(csv_path, index=False)