# -*- coding: utf-8 -*-
"""
Created on 2026-10-01 13:38:14

@author: Maurice Roots

Description:
     - A simple file to query the API and compute or organize statistics
"""
#%% 

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

from pathlib import Path
import requests
import tqdm

class TOLNet_Stats: 
    base_url = r"https://tolnet.larc.nasa.gov/api"
    
    @staticmethod
    def upload_count(cls, by_data_year: bool = False) -> dict:
        if not by_data_year: 
            return requests.get(cls.base_url + r"/metrics/upload").json()
        else: 
            return requests.get(cls.base_url + r"/metrics/upload_by_data_year").json()
        
    @staticmethod
    def download_count(cls): 
        return requests.get(cls.base_url + r"/metrics/download").json()
    
    @staticmethod
    def instrument_groups(cls) -> pd.DataFrame:
        """
        Returns a DataFrame containing all instrument groups.
        Contains:
            - id
            - instrument_group_name
            - folder_name
            - description
            - display_order
            - current_pi(Principle Investigator)
            - doi
            - citation_url
        """
        response = requests.get(cls.base_url + r"/instruments/groups")
        response.raise_for_status()
        return (
            pd.DataFrame(response.json())
            .sort_values(by=["id"])
            .set_index("id", drop=True)
            )


if __name__ == "__main__": 
    tolnet_stats = TOLNet_Stats.upload_count()


# %%
