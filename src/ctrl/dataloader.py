import requests
import pandas as pd
from bs4 import BeautifulSoup

class DataLoader:

    def __init__(self):
        self.ie_df = None
        self.ie2_df = None
        self.ie3_df = None

    def ie_data_loader(self):
        pass #TBD

    def ie2_data_loader(self):

        url = "http://watashiwa7.altervista.org/ie/2/stats_ie2.htm"

        response = requests.get(url)
        html_text = response.text

        soup = BeautifulSoup(html_text, "html.parser")
        h1_tags = soup.find_all("h1")

        dataframes = pd.read_html(html_text)

        dataframes = dataframes[1:]  # First Table is not useful

        for i, df in enumerate(dataframes):
            df.columns = df.iloc[0]
            df.drop(df.index[0], inplace=True)

            titulo = h1_tags[i].get_text(strip=True)
            df["Team"] = titulo

            dataframes[i] = df

        df = pd.concat(dataframes, ignore_index=True)

        df["Recr."].fillna("NS(Non Scouteable)", inplace=True)

        for col in df.columns:
            if col in ["FP", "TP", "Kick", "Body", "Control", "Guard", "Speed", "Stamina", "Guts", "Freedom"]:
                df[col] = df[col].astype(float)
        self.ie2_df = df

    def ie3_data_loader(self):
        pass #TBD
