# %%
import pandas as pd 
# pd.set_option("display.max_rows", 100)

import os 
import pathlib
pathos = pathlib.Path(__file__).parent
os.chdir(pathos)
# print(os.getcwd())

from sudulunu.helpers import pp, make_num, dumper, rc
# from sudulunu.helpers import rand_delay, unique_in_col, null_in_col
# from sudulunu.helpers import combine_from_folder, rc

# %%

fillo = '../input/fatalities_age_frontiers.csv'


#%%

data = pd.read_csv(fillo)

# %%

df = data.copy()
'Age', 'Value'

df['Value'] = pd.to_numeric(df['Value'])
df['Value'] = round(df['Value'],0)

# pp(df)

# print(df['Age'].unique().tolist())

#%%

bye = df

bye['Color'] = '#005689'

bye.loc[bye['Age'].isin(['60-64', '65-69', '70-74', '75-79', '80-84', '85+']), 'Color'] = '#e6711b'

pp(bye)

final = bye.to_dict(orient='records') 
template = [
	{
	"title": "Almost 70% of heatwave deaths were in the 60+ age group",
	"subtitle": "Showing heatwave deaths between 2001 to 2018 by age group, where age is known",
	"footnote": "",
	"source": "Risk Frontiers, Coates et al.",
	"margin-left": "20",
	"margin-top": "30",
	"margin-bottom": "20",
	"margin-right": "10"
	}
]

from yachtcharter import yachtCharter
# testo = "-testo"
testo = ''
chart_key = f"oz-datablogs-231024-heatwave-deaths-ages-bars{testo}"
yachtCharter(template=template, 
			data=final,
			chartId=[{"type":"horizontalbar"}],
            options=[{"enableShowMore":"FALSE", "autoSort":"FALSE"}],
			chartName=f"{chart_key}")