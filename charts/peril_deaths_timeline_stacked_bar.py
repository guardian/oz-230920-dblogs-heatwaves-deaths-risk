# %%
import pandas as pd 
# pd.set_option("display.max_rows", 100)

import os 
import pathlib
pathos = pathlib.Path(__file__).parent.parent
os.chdir(pathos)
print(os.getcwd())

from sudulunu.helpers import pp, make_num, dumper, rc
# from sudulunu.helpers import rand_delay, unique_in_col, null_in_col
# from sudulunu.helpers import combine_from_folder, rc

# %%

fillo = 'input/peril_paper/table2.csv'
# sheets = pd.read_excel(fillo, None).keys()
# print(sheets)

#%%

data = pd.read_csv(fillo)
# ['Decade', ' Number of deaths', 'Unnamed: 2', 
# 'Death ratea per 100,000 Mal Male to fema', 'e', 
# 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9']
# %%

df = data.copy()
# df = df[['Decade', ' Number of deaths']]
df.reset_index(inplace=True)
df = df[['index', 'Decade']]

df.rename(columns={'index':'Decade', 'Decade': "Deaths"}, inplace=True)

df = df.loc[df['Decade'] != "Total"]

df["Decade"] = df["Decade"].astype(str).str.split("–").str[-1].str.strip()

# df['Decade'] = df['Decade'].astype(int)
# df['Decade'] = round(df['Decade'], 0)

df['Decade'] = pd.to_datetime(df['Decade'], format="%Y")

df['Decade'] = df['Decade'].dt.strftime("%Y-%m-%d")
pp(df)

#%%

#%%

bye = df
bye.fillna('', inplace=True)

final = bye.to_dict(orient='records') 
template = [
	{
    "title": f"Deaths from natural heat by decade",
    "subtitle": f"Showing the number of deaths in the PerilAus database for the decade. Data is based on news and coroners reports and may not be exhaustive",
	"footnote": "",
	"source": "PerilAus database",
    "dateFormat": "%Y-%m-%d",
    "xAxisDateFormat": "%Y",
	"margin-left": "60",
	"margin-top": "30",
	"margin-bottom": "20",
	"margin-right": "10",
    "minY": '-30',
    # "tooltip":"<strong> Shortfall</strong>: {{groupValue}} "
	}
]

from yachtcharter import yachtCharter
testo = "-testo"
# testo = ''
chart_key = f"oz-datablogs-heat-risk-datablog-decades-deaths-timeline-stackedbar{testo}"
yachtCharter(template=template, 
			data=final,
            key = [],
            # trendline = trends,
            # options=[{"colorScheme":"guardian", 'trendColors': '#94b1ca,#a9af2b,#a9af2b,#a9af2b'}],
            # options=[{"colorScheme":"guardian"],
            chartId=[{"type":"stackedbar"}],
			chartName=f"{chart_key}")