import pandas as pd

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renames columns of the dataset based on the provided Pima Indians Diabetes Dataset variable names.
    
    Parameters:
    df (pd.DataFrame): The input dataframe to rename columns.
    
    Returns:
    pd.DataFrame: The dataframe with renamed columns.
    """
    column_mapping = {
        '6': 'times_pregnant',
        '148': 'plasma_glucose',
        '72': 'blood_pressure',
        '35': 'triceps_skin_fold_thickness',
        '0': 'serum_insulin',
        '33.6': 'bmi',
        '0.627': 'diabetes_pedigree_function',
        '50': 'age',
        '1': 'diabetes_class'
    }
    
    df.rename(columns=column_mapping, inplace=True)
    return df
