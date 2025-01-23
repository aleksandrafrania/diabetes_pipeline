# Diabetes Pipeline

This project is a reproducible pipeline for predicting the onset of diabetes within 5 years in Pima Indians given medical details. The pipeline includes data exploration, data cleaning, model training, and evaluation. The dataset used in this project comes from [this source](https://github.com/ashishpatel26/Pima-Indians-Diabetes-Dataset-Missing-Value-Imputation/blob/master/pima-indians-diabetes.data.csv).

## Requirements

- Docker

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/aleksandrafrania/diabetes_pipeline.git
    cd diabetes_pipeline
    ```

2. **Build the Docker image**:
    ```sh
    docker build -t diabetes_pipeline .
    ```

3. **Run the Docker container**:
    ```sh
    docker run -it --rm diabetes_pipeline
    ```

## Project Structure

- `data_exploration.py`: Functions for data exploration.
- `data_cleaning.py`: Functions for data cleaning.
- `prediction_model.py`: Functions for model training and evaluation.
- `main.py`: Main script to run the pipeline.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Docker configuration.

## Usage

The pipeline will load the dataset, perform data exploration, clean the data, train the model, and evaluate it. The results will be printed to the console.

## Detailed Steps

1. **Data Exploration**:
    - Load the dataset using `load_dataset()`.
    - Summarize the data using `summarize_data()`.
    - Check for missing values using `check_missing_values()`.
    - Check for duplicate rows using `check_duplicates()`.

2. **Data Cleaning**:
    - Rename columns using `rename_columns()`.
    - Replace zero values with median values using `replace_zeros_with_median()`.
    - Scale features using `scale_features()`.

3. **Model Training and Evaluation**:
    - Train the model using `train_model()`.
    - Predict the labels using `predict()`.
    - Evaluate the model using `evaluate_model()`.

## Example Output

The pipeline will output the following information:

- Initial data exploration summary
- Cleaned data preview
- Cross-validation scores
- Model accuracy
- Confusion matrix
- Classification report
- Predictions

## Dependencies

The project requires the following Python packages, specified in `requirements.txt`:

```plaintext
pandas==2.2.3
scikit-learn==1.5.2