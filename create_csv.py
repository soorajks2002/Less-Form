# create the user information csv file

import pandas as pd
import os

csv_path = "user_data.csv"

if not os.path.isfile(csv_path) :
    columns = ["Index", "Name", "Email", "Phone", "Address", "DOB", "Education"]
    df = pd.DataFrame(columns=columns)

    df.to_csv(csv_path, index=False)