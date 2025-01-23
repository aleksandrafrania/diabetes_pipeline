import pandas as pd
pd.set_option('display.max_columns', None)

def load_dataset():
    """
    Load the diabetes dataset from sklearn and return it as a pandas DataFrame.
    
    Returns:
        pd.DataFrame: The diabetes dataset as a pandas DataFrame.
    """
    df = pd.read_csv("data/pima_indians_diabetes_data.csv")
    return df


def summarize_data(df):
    """
    Print a summary of the dataset, including shape, data types, and descriptive statistics.

    Args:
        df (pd.DataFrame): The input DataFrame.
    """
    print("Dataset shape:", df.shape)
    print("\nColumn data types:")
    print(df.dtypes)
    print("\nDescriptive statistics:")
    print(df.describe(include="all"))


def check_missing_values(df):
    """
    Check for missing values in the dataset and print the result.

    Args:
        df (pd.DataFrame): The input DataFrame.
    """
    missing = df.isnull().sum()
    print("\nMissing values:")
    print(missing[missing > 0] if missing.sum() > 0 else "No missing values.")


def check_duplicates(df):
    """
    Check for duplicate rows in the dataset and print the result.

    Args:
        df (pd.DataFrame): The input DataFrame.
    """
    duplicates = df.duplicated().sum()
    print("\nNumber of duplicate rows:", duplicates)
