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

fillo = '../input/irsad_percentile_heatwave_fatalities.csv'


#%%

data = pd.read_csv(fillo)

# %%

df = data.copy()
# 'IRSAD Decile', 'Value '

df['Value '] = pd.to_numeric(df['Value '])
df['Value '] = round(df['Value '],0)

# pp(df)

print(df['IRSAD Decile'].unique().tolist())

#%%

bye = df

bye['Color'] = '#005689'

bye.loc[bye['IRSAD Decile'].isin(['1 (most disadvantaged)', '2', '3', '4', '5']), 'Color'] = '#e6711b'

final = bye.to_dict(orient='records') 
template = [
	{
	"title": "More than 60% of heatwave deaths were in the most socio-economically disadvantaged areas",
	"subtitle": "Showing heatwave deaths between 2001 to 2018 by socio-economic (IRSAD) decile of the area",
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
chart_key = f"oz-datablogs-231018-heatwave-deaths-irsad-bars{testo}"
yachtCharter(template=template, 
			data=final,
			chartId=[{"type":"horizontalbar"}],
            options=[{"enableShowMore":"FALSE", "autoSort":"FALSE"}],
			chartName=f"{chart_key}")