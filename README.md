# Diabetes Pipeline

This project is a reproducible pipeline for predicting the onset of diabetes within 5 years in Pima Indians given medical details. The pipeline includes data exploration, data cleaning, model training, and evaluation. The dataset used in this project comes from [this source](https://github.com/ashishpatel26/Pima-Indians-Diabetes-Dataset-Missing-Value-Imputation/blob/master/pima-indians-diabetes.data.csv).

## Requirements

- Docker (optional)
- Python 3.9+
- pip

## Setup

### Using Docker

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

### Without Docker

1. **Clone the repository**:
    ```sh
    git clone https://github.com/aleksandrafrania/diabetes_pipeline.git
    cd diabetes_pipeline
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Run the main script**:
    ```sh
    python main.py
    ```

## Project Structure

- `utils/`: Folder containing utility functions.
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
    - Rename columns using `rename_c