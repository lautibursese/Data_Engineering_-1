import pandas as pd

class Preprocessing:
    '''
    This class takes as argument a Pandas DataFrame
    '''
    def __init__(self, data:pd.DataFrame):
        self.data = data

    '''
    Add column with the Platform database name to after make easier filters
    '''
    def columns_names(self):
        self.data.columns = (['ID', 'Type', 'Tittle', 'Director', 'Cast', 'Country', 'Date_Added', 'Release_Year', 'Rating', 'Duration', 'Listed_in', 'Description', 'Platform'])


    '''
    Add column with the Platform database name to after make easier filters
    '''
    def unify_criteria(self, column:str, old_value:str, new_value:str):
        self.data[column] = self.data[column].replace({old_value}, new_value)

    '''
    DataFrame con la data limpia a un nuevo csv guardado en la carpeta 'clean_data'
    '''
    def clean_to_csv(self, csv):
        self.data.to_csv(f"C:/Users/Predator/Desktop/Lauti/Programación/GitHub/1. Data Engineering/#1/Datasets_clean/{csv}", index=False)


