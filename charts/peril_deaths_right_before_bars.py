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

keep = ['Working', 
'Domestic duties', 'Travelling', 'Recreation', 'Walking', 
'Other (talking; in camp; too young)',  ]

df = df.loc[df['Interval'].isin(keep)]

for col in [' 1844–1899', '1900–1955', '1956–2010']:

    df[col] = df[col].astype(str)

    df[col] = df[col].str.split("(").str[-1].str.replace(")", "").replace('–', '')

    df[col] = pd.to_numeric(df[col])

    df.rename(columns={col: col.strip()}, inplace=True)

df.loc[df['Interval'] == 'Other (talking; in camp; too young)', 'Interval'] = "Other"

df.fillna("", inplace=True)

#%%

piv = df.T.reset_index()
piv.columns = piv.iloc[0]
piv = piv[1:]

piv.fillna("", inplace=True)

pp(piv)


#%%

#%%

bye = piv

final = bye.to_dict(orient='records') 
template = [
	{
	"title": "The share of people dying from heat while working has dropped dramatically",
	"subtitle": "Showing the activities being performed just before death by natural heat as a percentage those where activities are known. Some data has been significantly influenced by counts taken the Victorian Coroner after the 2009 heatwave. Due to gaps data may not add up to 100",
	"footnote": "",
	"source": "PerilAus database",
	"margin-left": "20",
	"margin-top": "30",
	"margin-bottom": "20",
	"margin-right": "10"
	}
]

from yachtcharter import yachtCharter
# testo = "-testo"
testo = ''
chart_key = f"oz-datablogs-heat-waves-risk-death-just-before{testo}"
yachtCharter(template=template, 
			data=final,
			chartId=[{"type":"horizontalbar"}],
            options=[{"enableShowMore":"FALSE", "autoSort":"FALSE"}],
			chartName=f"{chart_key}")