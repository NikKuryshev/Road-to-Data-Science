import pandas as pd
import openpyxl
import os
import const
import re

import func

kp_number = [4679, 5486, 5612, 4087]
final_data = pd.DataFrame()

list_of_paths = func.get_actual_kp_file(kp_number)
for path in list_of_paths:
    list_of_offer = func.get_sheet(path)
    data = func.get_data(path, list_of_offer)
    final_data = pd.concat([final_data,data]).reset_index(drop = True)
    print(final_data.shape)
    print(data.shape)
print(final_data.shape)


