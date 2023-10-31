import pandas as pd

columns = ["Index", "Name", "Email", "Phone", "Address", "DOB", "Education"]
df = pd.DataFrame(columns=columns)

df.to_csv("user_data.csv", index=False)