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

# This is from the Peril Aus data:
# https://www.sciencedirect.com/science/article/pii/S1462901114000999?ref=pdf_download&fr=RR-2&rr=817d1d9ffc1d1f6e
stringo = """
<table><thead class="valign-top"><tr><th scope="col" class="rowsep-1 align-left">Natural hazard</th><th scope="col" class="rowsep-1 align-center">Deaths 1900–2011</th><th scope="col" class="rowsep-1 align-center">% total natural hazard deaths 1900–2011</th></tr></thead><tbody><tr><td class="align-left">Extreme heat</td><td class="align-char">4,555</td><td class="align-char">55.2</td></tr><tr><td class="align-left">Flood</td><td class="align-char">1,221</td><td class="align-char">14.8</td></tr><tr><td class="align-left">Tropical cyclone</td><td class="align-char">1,285</td><td class="align-char">15.6</td></tr><tr><td class="align-left">Bush/grassfire</td><td class="align-char">866</td><td class="align-char">10.5</td></tr><tr><td class="align-left">Lightning</td><td class="align-char">85</td><td class="align-char">1</td></tr><tr><td class="align-left">Landslide</td><td class="align-char">88</td><td class="align-char">1.1</td></tr><tr><td class="align-left">Wind storm</td><td class="align-char">68</td><td class="align-char">0.8</td></tr><tr><td class="align-left">Tornado</td><td class="align-char">42</td><td class="align-char">0.5</td></tr><tr><td class="align-left">Hail storm</td><td class="align-char">16</td><td class="align-char">0.2</td></tr><tr><td class="align-left">Earthquake</td><td class="align-char">16</td><td class="align-char">0.2</td></tr><tr><td class="align-left">Rain storm</td><td class="align-char">14</td><td class="align-char">0.2</td></tr></tbody></table>
"""


data = pd.read_html(stringo)[0]
# 'Natural hazard', 'Deaths 1900–2011', '% total natural hazard deaths 1900–2011'

pp(data)


# %%

df = data.copy()

df = df[['Natural hazard', 'Deaths 1900–2011']]

pp(df)

#%%

##########

bye = df

bye['Color'] = '#005689'
bye.loc[bye['Natural hazard'] == 'Extreme heat', 'Color'] = '#e6711b'

final = bye.to_dict(orient='records') 
template = [
	{
	"title": "Deaths from natural hazards between 1900 and 2011",
	"subtitle": "Showing the numbers of deaths by the type of natural hazard. Data is based on media reports",
	"footnote": "",
	"source": "PerilAus, Coates et al 2014, Journal of Environmental Science and Policy",
	"margin-left": "20",
	"margin-top": "30",
	"margin-bottom": "20",
	"margin-right": "10"
	}
]

from yachtcharter import yachtCharter
# testo = "-testo"
testo = ''
chart_key = f"oz-datablogs-heat-risk-deaths-peril-aus-all{testo}"
yachtCharter(template=template, 
			data=final,
			chartId=[{"type":"horizontalbar"}],
            options=[{"enableShowMore":"FALSE", "autoSort":"FALSE"}],
			chartName=f"{chart_key}")