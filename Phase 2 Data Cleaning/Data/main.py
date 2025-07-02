import pandas as pd

angka = 5


# Load a specific sheet in the Excel file
df = pd.read_excel(f'Model {angka}.xlsx', sheet_name='1')
# Open the text file in write mode
with open(f'predicted{angka}.txt', 'w') as f:
    # Loop through the rows in the specified range
    for i in df.loc[0:8013, 'Prediction: income']:
        if i == '>50K':
            f.write('1\n')
        elif i == '<=50K':
            f.write('0\n')
        else:
            f.write('UNIDENTIFIED\n')
