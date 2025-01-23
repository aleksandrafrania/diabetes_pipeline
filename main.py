from data_exploration import load_dataset, summarize_data, check_missing_values, check_duplicates
from data_cleaning import rename_columns, replace_zeros_with_median, scale_features
from prediction_model import train_model, predict, evaluate_model

def main():
    df = load_dataset()
    
    print("Initial data exploration:\n")
    summarize_data(df)
    check_missing_values(df)
    check_duplicates(df)
    
    df = rename_columns(df)
    df = replace_zeros_with_median(df)
    df = scale_features(df)

    