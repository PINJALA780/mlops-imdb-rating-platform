from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="IMDb Rating Prediction API")

# ✅ Prometheus instrumentation
Instrumentator().instrument(app).expose(app)

# Load model
model = joblib.load("models/movie_rating_model.pkl")


class MovieInput(BaseModel):
    year: int
    runtime_minutes: int
    num_votes: int


@app.get("/")
def home():
    return {"message": "IMDb Rating Prediction API"}


@app.post("/predict")
def predict(movie: MovieInput):

    prediction = model.predict([[
        movie.year,
        movie.runtime_minutes,
        movie.num_votes
    ]])

    return {
        "predicted_rating": round(float(prediction[0]), 2)
    }
