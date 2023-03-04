import pandas as pd
import numpy as np
from preprocessing import Preprocessing

print("Processing...")

amazon_prime = pd.read_csv('C:/Users/Predator/Desktop/Lauti/Programación/GitHub/1. Data Engineering/#1/Datasets/amazon_prime_titles.csv', sep=',')
amazon_prime['Plataforma'] = 'Amazon_Prime' #Column assignment

disney_plus = pd.read_csv('C:/Users/Predator/Desktop/Lauti/Programación/GitHub/1. Data Engineering/#1/Datasets/disney_plus_titles.csv', sep=',')
disney_plus['Plataforma'] = 'Disney_Plus' #Column assignment

hulu = pd.read_csv('C:/Users/Predator/Desktop/Lauti/Programación/GitHub/1. Data Engineering/#1/Datasets/hulu_titles.csv', sep=',')
hulu['Plataforma'] = 'Hulu' #Column assignment

netflix = pd.read_json('C:/Users/Predator/Desktop/Lauti/Programación/GitHub/1. Data Engineering/#1/Datasets/netflix_titles.json')
netflix['Plataforma'] = 'Netflix' #Column assignment

df_definitive = pd.concat([amazon_prime, disney_plus, hulu, netflix], axis=0)

#Fill NaN values
df_definitive['director'].fillna('no data', inplace=True)
df_definitive['cast'].fillna('no data', inplace=True)
df_definitive['country'].fillna('no data', inplace=True)
df_definitive['date_added'].fillna('no data', inplace=True)
df_definitive['rating'].fillna('no data', inplace=True)
df_definitive['description'].fillna('no data', inplace=True)

#Change misimputed values
mask = df_definitive['rating'].str.contains('min')
df_definitive.loc[mask, 'duration'] = df_definitive.loc[mask]['rating']
df_definitive.loc[mask, 'rating'] = 'no data'
mask2 = df_definitive['rating'].str.contains('eason')
df_definitive.loc[mask2, 'duration'] = df_definitive.loc[mask]['rating']
df_definitive.loc[mask2, 'rating'] = 'no data'
df_definitive.fillna('no data', inplace=True)

#Criteria modification
maskkk = df_definitive['duration'].str.contains('min')
maskkk2 = df_definitive['duration'].str.contains('Season')
df_definitive.loc[maskkk, 'duration'] = df_definitive.loc[maskkk, 'duration'].str[0:-4].astype(int)
df_definitive.loc[maskkk2, 'duration'] = df_definitive[maskkk2]['duration'].str[0:-7].astype(int)

df_definitive = Preprocessing(df_definitive)

#Data normalization
df_definitive.columns_names()

#Criteria unification
df_definitive.unify_criteria('Rating', 'no data', 'UNRATED')
df_definitive.unify_criteria('Rating', 'NOT_RATE', 'UNRATED')
df_definitive.unify_criteria('Rating', 'NOT RATED', 'UNRATED')
df_definitive.unify_criteria('Rating', 'NR', 'UNRATED')
df_definitive.unify_criteria('Rating', 'UR', 'UNRATED')

df_definitive.clean_to_csv("platforms.csv")