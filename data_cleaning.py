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


def replace_zeros_with_median(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replaces all 0 values in specified columns with the median of those columns.
    These 0 values have been input to represent missing values, however they are not 
    possible measurements (e.g. one cannot have a blood pressure of 0).
    
    Parameters:
    df (pd.DataFrame): The input dataframe to replace 0 values.
    
    Returns:
    pd.DataFrame: The dataframe with 0 values replaced by median values.
    """
    columns_to_replace = [
        'plasma_glucose', 
        'blood_pressure', 
        'triceps_skin_fold_thickness', 
        'serum_insulin', 
        'bmi'
    ]
    
    for column in columns_to_replace:
        median_value = df[df[column] != 0][column].median()
        df[column] = df[column].replace(0, median_value)
    
    return df
