# Import necessary functions from data exploration and cleaning modules
from data_exploration import load_dataset, summarize_data, check_missing_values, check_duplicates
from data_cleaning import rename_columns

def main():
    df = load_dataset()
    
    print("Initial data exploration:\n")
    summarize_data(df)
    check_missing_values(df)
    check_duplicates(df)
    
    df = rename_columns(df)

    print("\nCleaned data:")
    print(df.head())

# Run the pipeline
if __name__ == "__main__":
    main()
