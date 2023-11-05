
![App Screenshot](https://raw.githubusercontent.com/soorajks2002/Less-Form/master/Screenshots/banner.png)



## Installation

1. Clone the Git Repository
```bash
git clone https://github.com/soorajks2002/Less-Form.git
```

2. Add your OpenAI api key
```bash
Less-Form\api_key.py
        openai_api_key = 'your open ai api key'
```
if you dont'have an OpenAI API-key, generate one from [here](https://platform.openai.com/account/api-keys).

3. Create the User-information Dataframe
```bash
python create_csv.py
```

4. Run the terminal version
```bash
python chat.py
```

5. Run the Streamlit version
```bash
streamlit run streamlit_app.py
```
    
## Screenshots

#### Age Calculation through complex user input
![App Screenshot](https://github.com/soorajks2002/Less-Form/blob/master/Screenshots/age%20calculation.png?raw=true)

#### Personal information gathered through the text
![App Screenshot](https://github.com/soorajks2002/Less-Form/blob/master/Screenshots/age%20calculation%202.png?raw=true)

#### WebApp Home-Page
![App Screenshot](https://github.com/soorajks2002/Less-Form/blob/master/Screenshots/homepage.png?raw=true)

#### Sample Conversation
![App Screenshot](https://github.com/soorajks2002/Less-Form/blob/master/Screenshots/sample%20conversation.png?raw=true)

#### Prompt Injection
![App Screenshot](https://github.com/soorajks2002/Less-Form/blob/master/Screenshots/prompt_injection.png?raw=true)

#### User Personal Data in the csv file
![App Screenshot](https://github.com/soorajks2002/Less-Form/blob/master/Screenshots/sample%20user%20personal%20information.png?raw=true)
