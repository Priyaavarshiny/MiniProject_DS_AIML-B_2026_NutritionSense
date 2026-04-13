import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

def train_model(path):
    df = pd.read_csv(path)

    # Features and target
    X = df.drop('NObeyesdad', axis=1)
    y = df['NObeyesdad']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Model Accuracy:", accuracy)

    # Convert predictions to labels
    reverse_map = {
        0: "Insufficient Weight",
        1: "Normal Weight",
        2: "Overweight Level I",
        3: "Overweight Level II",
        4: "Obesity Type I",
        5: "Obesity Type II",
        6: "Obesity Type III"
    }

    predicted_labels = [reverse_map[i] for i in y_pred[:5]]
    actual_labels = [reverse_map[i] for i in y_test.values[:5]]

    print("Actual:", actual_labels)
    print("Predicted:", predicted_labels)

    return model


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    path = os.path.join(BASE_DIR, "dataset", "processed_data", "cleaned_data.csv")

    train_model(path)