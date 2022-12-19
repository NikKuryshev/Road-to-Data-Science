import pandas as pd
import openpyxl
import func

of = func.get_sheet(path4)
df = func.get_data(path4, of)

print(of)
print(df)