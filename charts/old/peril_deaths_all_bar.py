# %%
import pandas as pd 
# pd.set_option("display.max_rows", 100)

import os 
import pathlib
pathos = pathlib.Path(__file__).parent.parent
os.chdir(pathos)
# print(os.getcwd())

from sudulunu.helpers import pp, make_num, dumper, rc
# from sudulunu.helpers import rand_delay, unique_in_col, null_in_col
# from sudulunu.helpers import combine_from_folder, rc

# %%

fillo = 'input/peril_paper/table3.csv'
# sheets = pd.read_excel(fillo, None).keys()
# print(sheets)

#%%

data = pd.read_csv(fillo)
# 'Interval', ' 1844–1899', '1900–1955', '1956–2010'

print(data['Interval'].unique().tolist())
# ['Total  heat-associated deaths for that interval', 'In/out: number of known deaths', 
# 'Indoors', 'Outdoors', 'Activity prior: number of known deaths', 'Working', 
# 'Domestic duties', 'Travelling', 'Recreation', 'Walking', 
# 'Other (talking; in camp; too young)', 
# 'Other vulnerabilities: number of known deaths', 'Alcohol', 
# 'Mental health issues', 'Sedentary activities', 
# 'Disabled/being cared for by others', 'In the city', 'In  rural location', 
# 'Newly arrived', 'Senior', 'Very young (0–9 years)', 'Healthy/strong/young', 
# 'Strenuous activity', 'Lived alone', 'Medical condition']
# %%

df = data.copy()

pp(df)

# %%