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

fillo = 'input/AIHW_INJCAT213_Data_tables_E_06072023.xlsx'

data = pd.read_excel(fillo, sheet_name='E31-33 Nature', skiprows=2)
['Unnamed: 0', 'ICD-10 code', 'Unnamed: 2', '0–4', '5–14', '15–24', 
 '25–44', '45–64', '65+', 'Total']
# %%

df = data.copy()

df.rename(columns={'Unnamed: 0': "Cause", "Unnamed: 2": "Sex"}, inplace=True)

df = df.loc[df['Sex'] == 'Persons']

df.reset_index(drop=True, inplace=True)
df = df[:4]

df['Cause'] = df['Cause'].str.replace("Exposure to ", '')

keep = {
    'X33–X39': "Other natural forces",'X30': "Excessive natural heat",
'X31': "Excessive natural cold"}

df['Cause'] = df['ICD-10 code']


df = df.loc[df['ICD-10 code'] != 'X32']
df['Cause'] = df['Cause'].map(keep)

df.drop(columns={'Total', 'ICD-10 code','Sex'}, inplace=True)

pp(df)

#%%

#%%

##########

# bye = 

# final = bye.to_dict(orient='records') 
# template = [
#     {
#     "title": f"",
#     "subtitle": f"",
#     "footnote": "",
#     "dateFormat": "%Y-%m-%d",
#     "source": "",
#     "margin-left": "35",
#     "margin-top": "30",
#     "margin-bottom": "20",
#     "margin-right": "10",
    # "xAxisDateFormat": "%Y",
##     "tooltip":"<strong>{{#formatDate}}{{Date}}{{/formatDate}}</strong><br/> In ICU: {{ICU}}<br/>"
#     }
# ]

# from yachtcharter import yachtCharter
## testo = "-testo"
# testo = ''
# chart_key = f"oz-datablogs-something_random{igloo}{testo}"
# yachtCharter(template=template, 
#             data=final,
#             key = [{"key":"Net internal migration", "colour":'#7d0068'}],
#             chartId=[{"type":"linechart"}],
#             options=[{"colorScheme":"guardian", "lineLabelling":"TRUE"}],
#             chartName=f"{chart_key}{testo}")

# #%%

###########

# Horizontalbar
# horizontal bar 

# bye = 

# bye['Color'] = '#7d0068'
# final = bye.to_dict(orient='records') 
# template = [
# 	{
# 	"title": "Yacht Charter test chart",
# 	"subtitle": "Things",
# 	"footnote": "Footnote",
# 	"source": "The universe",
# 	"margin-left": "20",
# 	"margin-top": "30",
# 	"margin-bottom": "20",
# 	"margin-right": "10"
# 	}
# ]

# from yachtcharter import yachtCharter
## testo = "-testo"
# testo = ''
# chart_key = f"oz-datablogs-something_random{igloo}{testo}"
# yachtCharter(template=template, 
# 			data=final,
# 			chartId=[{"type":"horizontalbar"}],
#             options=[{"enableShowMore":"FALSE", "autoSort":"FALSE"}],
# 			chartName=f"{chart_key}")