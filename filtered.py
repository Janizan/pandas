import pandas as pd
import re

def remove_special_characters(text):
    pattern = r'[^a-zA-Z0-9\s]'  
    cleaned_text = re.sub(pattern, '', text)  
    return cleaned_text

data = {
    'Name': ['Janani', 'Viji', 'Lisa', 'Taylor','Swift','Jennie','Rose','Jisoo','Dora','Ani'],
    'Address':['48/5a, 1st Street, Tuticorin','60a,Colony A,Tirunelveli','H10 Majestic Apartment 1:F,Tenkasi',
               '16/01a,First floor,Chennai','45k,New Colony,Chennai','16/06,Electronic City Phase 1,Bangalore',
               '1A/2,Old Colony,Chennai','Door no: 28,Clever Apartments,Tuticorin','5/5A,South School Street,Chennai',
               '1/5a,1st Street,Tenkasi'],
    'Age': [25, 30, 35, 40, 22, 26, 28, 33, 21, 23],
    'City': ['Bangalore','Tenkasi','Tuticorin','Salem','Madurai','Thanjavur', 'Chennai', 'Coimbatore','Bangalore', 'Tirunelveli']
}

# dataframe
df= pd.DataFrame(data)

df['Address'] = df['Address'].apply(remove_special_characters)


file_path = 'customer_details_new.xlsx'

df.to_excel(file_path, index=False)

print(f"Cleaned DataFrame saved to Excel file: '{file_path}'")
