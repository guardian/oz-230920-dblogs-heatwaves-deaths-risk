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
# fillo = 'inter/underlying_causes/2012-21-abs_underlying_causes.csv'

data = pd.read_csv(fillo)
['Cause', '2002', '2003', '2004', '2005', '2006', '2007', 
 '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', 'Total']

# rename_dict = {
#     'X30-X39': "All forces of nature",
# 'X30': "Excessive natural heat",
# 'X31': "Excessive natural cold",
# 'X32': "Sunlight",
# 'X33': "Lightning",
# 'X34': "Earthquake",
# 'X35': "Volcano",
# 'X36': "Avalanche, landslide etc.",
# 'X37': "Storms",
# 'X38': "Flood",
# 'X39': "Unspecified"}

# data['Cause'] = data['Cause'].map(rename_dict)

data.rename(columns={'Total': "2002-2021"}, inplace=True)

data = data[['Cause',"2002-2021" ]]

data = data.loc[~data['Cause'].isin(['All forces of nature'])]

# combiner = ['Unspecified', 'Sunlight', 'Avalanche, landslide etc.', 'Volcano', 'Earthquake']
# data['Other natural forces'] = data[combiner].sum(axis=1)

# pp(data)

# %%

df = data.copy()

df["2002-2021"] = pd.to_numeric(df["2002-2021"])
df.sort_values(by=["2002-2021"], ascending=False, inplace=True)

df = df.T.reset_index()
df.columns = df.iloc[0]
df = df[1:]

combiner = ['Unspecified', 'Sunlight', 'Avalanche, landslide etc.', 'Volcano', 'Earthquake']
df['Other natural forces'] = df[combiner].sum(axis=1)

for col in combiner:
    df.drop(columns={col}, inplace=True)
    
df = df.T.reset_index()
df.columns = df.iloc[0]
df = df[1:]



#%%

bye = df

bye.sort_values(by=["2002-2021"], ascending=False, inplace=True)


pp(bye)

bye['Color'] = '#005689'
bye.loc[bye['Cause'].str.contains('heat'), 'Color'] = '#e6711b'
final = bye.to_dict(orient='records') 
template = [
	{
	"title": "Heat was one of the leading underlying cause of death among 'natural forces' in 2002-2021",
	"subtitle": "Showing only data where the underlying cause of death was a natural force (codes x30-x39) according to the International Classification of Diseases (ICD-10). The categories are not directly comparable to some of the other charts that use different classifications. 'Other natural forces' includes avalanches, landslides, volcanos, earthquakes and the otherwise unspecified.",
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