import pandas as pd

data = {
    'Name': ['Janani', 'Viji', 'Lisa', 'Taylor','Swift','Jennie','Rose','Jisoo','Dora','Ani'],
    'Age': [25, 30, 35, 40, 22, 26, 28, 33, 21, 23],
    'City': ['Bangalore','Tenkasi','Tuticorin','Salem','Madurai','Thanjavur', 'Chennai', 'Coimbatore','Bangalore', 'Tirunelveli']
}

# Create DataFrame
df = pd.DataFrame(data)


file_path = 'customer_details.xlsx'


df.to_excel(file_path, index=False)

print(f"DataFrame saved to Excel file: '{file_path}'")
