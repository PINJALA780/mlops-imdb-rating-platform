import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# MLflow Experiment
mlflow.set_experiment("IMDb-Rating-Prediction")

# Load Dataset
df = pd.read_csv("data/imdb_top_movies_1980_2026.csv")

print("Dataset Shape:", df.shape)

# Select Features
df = df[
    [
        "year",
        "runtime_minutes",
        "num_votes",
        "average_rating"
    ]
]

# Remove Missing Values
df = df.dropna()

X = df[
    [
        "year",
        "runtime_minutes",
        "num_votes"
    ]
]

y = df["average_rating"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

with mlflow.start_run():

    # Train Model
    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Prediction
    predictions = model.predict(X_test)

    # Metrics
    mae = mean_absolute_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    print(f"MAE: {mae:.3f}")
    print(f"R2 Score: {r2:.3f}")

    # Log Parameters
    mlflow.log_param(
        "n_estimators",
        200
    )

    mlflow.log_param(
        "random_state",
        42
    )

    # Log Metrics
    mlflow.log_metric(
        "mae",
        mae
    )

    mlflow.log_metric(
        "r2_score",
        r2
    )

    # Log Model
    mlflow.sklearn.log_model(
    sk_model=model,
    name="imdb-rating-model",
    registered_model_name="IMDbRatingModel"
    )

    # Save Local Model
    joblib.dump(
        model,
        "models/movie_rating_model.pkl"
    )

    print("Model saved successfully")
