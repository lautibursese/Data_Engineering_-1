import pandas as pd
import numpy as np
from fastapi import FastAPI, Path, UploadFile, File

app=FastAPI(title='Data Engineering #1',
            description='Here we can do some consults')


dataframe = pd.read_csv("Datasets_clean/platforms.csv")

@app.get("/get_max_duration/")
async def get_max_duration(year:int, platform:str, min_or_season:str):
    mask_movie = dataframe['Type'] == 'Movie'
    mask_season = dataframe['Type'] == 'TV Show'
    mask1 = dataframe['Release_Year'] == year
    mask2 = dataframe['Platform'] == platform
    mask3 = dataframe['Duration'].str.contains('data') != True
    if min_or_season == "season":
        print(dataframe.loc[mask1&mask2&mask3&mask_season, 'Duration'].sort_values().tail(1).to_dict())
    else:
        return dataframe[mask1&mask2&mask3&mask_movie].sort_values('Duration')['Duration'].tail(1).to_dict()

@app.get("/get_count_platform/")
async def get_count_platform(platform):
    mask1 = dataframe['Platform'] == platform
    mask_movie = dataframe['Type'] == 'Movie'
    mask_season = dataframe['Type'] == 'TV Show'
    return {f"Movies: {dataframe[mask1&mask_movie].count()[0].tolist()}",
            f"TV Shows:, {dataframe[mask1&mask_season].count()[0].tolist()}"}

@app.get("/get_listedin/")
async def get_listedin(genre):
    mas = dataframe['Listed_in'].str.contains(genre, case=False)
    mas_amazonprime = dataframe['Platform'] == 'Amazon_Prime'
    mas_disneyplus = dataframe['Platform'] == 'Disney_Plus'
    mas_hulu = dataframe['Platform'] == 'Hulu'
    mas_netflix = dataframe['Platform'] == 'Netflix'
    return f"Amazon Prime has {dataframe[mas&mas_amazonprime].count()[0].tolist()}, Disney PLus {dataframe[mas&mas_disneyplus].count()[0].tolist()}, Hulu {dataframe[mas&mas_hulu].count()[0].tolist()} and Netflix {dataframe[mas&mas_netflix].count()[0].tolist()}"

from collections import Counter
import itertools

@app.get("/get_actor/")
async def get_actor(platform:str, year:int):
    mas_platform = dataframe['Platform'] == platform
    mas_year = dataframe['Release_Year'] == year
    mas_nodata = dataframe['Cast'].str.contains('no data') != True
    draft2 = list(itertools.chain(*dataframe.loc[mas_platform&mas_year&mas_nodata, 'Cast'].str.split(',')))
    return f"The two actors who repeat themselves the most are {Counter(draft2).most_common()[0:2]}"

# python -m uvicorn main:app --reload