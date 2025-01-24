import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def train_model(df: pd.DataFrame):
    """
    Trains a RandomForest model to predict the 'diabetes_class' label using cross-validation and the best parameters found.
    
    Parameters:
    df (pd.DataFrame): The input dataframe with features and label.
    
    Returns:
    RandomForestClassifier: The trained model.
    """
    X = df.drop(columns=['diabetes_class'])
    y = df['diabetes_class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Best parameters found by GridSearchCV
    best_params = {
        'max_depth': None,
        'min_samples_leaf': 4,
        'min_samples_split': 2,
        'n_estimators': 150
    }
    
    model = RandomForestClassifier(**best_params, random_state=42)
    
    # Cross-validation
    cv_scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"Cross-validation scores: {cv_scores}")
    print(f"Mean cross-validation score: {cv_scores.mean():.2f}")
    
    model.fit(X_train, y_train)
    
    return model, X_test, y_test

def predict(model, df: pd.DataFrame) -> pd.Series:
    """
    Predicts the 'diabetes_class' label using the trained model.
    
    Parameters:
    model (RandomForestClassifier): The trained model.
    df (pd.DataFrame): The input dataframe with features.
    
    Returns:
    pd.Series: The predicted labels.
    """
    predictions = model.predict(df)
    return pd.Series(predictions, index=df.index, name='diabetes_class')

def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series):
    """
    Evaluates the trained model using test data and prints metrics.
    
    Parameters:
    model (RandomForestClassifier): The trained model.
    X_test (pd.DataFrame): The test features.
    y_test (pd.Series): The true labels for the test data.
    """
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)
    
    print(f"Model Accuracy: {accuracy:.2f}")
    print("\nConfusion Matrix:")
    print(conf_matrix)
    print("\nClassification Report:")
    print(class_report)