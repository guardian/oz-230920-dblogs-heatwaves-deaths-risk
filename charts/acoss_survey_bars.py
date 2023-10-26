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

# This is from the ACOSS Report:
# https://www.acoss.org.au/wp-content/uploads/2023/10/ACOSS-Energy-Cost-of-Living-Snapshot-October-2023.pdf

datah = [{"Thing": "Cutting back on cooling and heating", "Value": 74},
         {"Thing": "Cutting back further on use of lights", "Value": 62},
         {"Thing": "Taking fewer hot showers", "Value": 55},
         {"Thing": "Changing how they cook meals", "Value": 51},
         {"Thing": "Going to bed early to keep warm, reducing use of lights", "Value": 49},
         {"Thing": "Stopped having people over", "Value": 33}]


data = pd.DataFrame.from_records(datah)
# 'Thing', 'Value'


# %%

df = data.copy()

pp(df)

#%%

##########

bye = df

bye['Color'] = '#005689'
bye.loc[bye['Thing'] == 'Cutting back on cooling and heating', 'Color'] = '#e6711b'
final = bye.to_dict(orient='records') 
template = [
	{
	"title": "74% of people on income support are cutting back on cooling and heating",
	"subtitle": "Showing what actions are being taken by people on income support due to rising energy costs. Based on a survey of 427 people in August 2023",
	"footnote": "",
	"source": "ACOSS",
	"margin-left": "20",
	"margin-top": "30",
	"margin-bottom": "20",
	"margin-right": "10"
	}
]

from yachtcharter import yachtCharter
# testo = "-testo"
testo = ''
chart_key = f"oz-datablogs-heat-risk-deaths-acoss-survey-energy-prices{testo}"
yachtCharter(template=template, 
			data=final,
			chartId=[{"type":"horizontalbar"}],
            options=[{"enableShowMore":"FALSE", "autoSort":"FALSE"}],
			chartName=f"{chart_key}")