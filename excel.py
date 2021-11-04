import pandas as pd

path = "C:\\Users\\KJS\\Desktop\\CPD\\"
file_1 = "BOT-2_raw_score.xlsx"
file_2 = "test_file.xlsx"

row, column = 6, 0

data_pd = pd.read_excel(file_1)
data_np = pd.DataFrame.to_numpy(data_pd)
print(type(data_np[row][31]))