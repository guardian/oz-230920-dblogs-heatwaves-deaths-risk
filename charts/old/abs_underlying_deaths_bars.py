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

fillo = 'inter/abs_underlying_causes.csv'

data = pd.read_csv(fillo)

# %%

df = data.copy()

df.sort_values(by=['2012-2021'], ascending=False, inplace=True)

pp(df)

#%%

bye = df

bye['Color'] = '#005689'
bye.loc[bye['Cause'].str.contains('heat'), 'Color'] = '#e6711b'
final = bye.to_dict(orient='records') 
template = [
	{
	"title": "Heat was the leading underlying cause of death among 'natural forces' in 2012-2021",
	"subtitle": "Showing only data where the underlying cause of death was a natural force",
	"footnote": "",
	"source": "Australian Bureau of Statistics",
	"margin-left": "20",
	"margin-top": "30",
	"margin-bottom": "20",
	"margin-right": "10"
	}
]

from yachtcharter import yachtCharter
# testo = "-testo"
testo = ''
chart_key = f"oz-datablogs-heatwaves-deaths-abs-underlying-bar{testo}"
yachtCharter(template=template, 
			data=final,
			chartId=[{"type":"horizontalbar"}],
            options=[{"enableShowMore":"FALSE", "autoSort":"FALSE"}],
			chartName=f"{chart_key}")