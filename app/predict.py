from app import __version__
from pathlib import Path
import pickle
import pandas as pd

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}\\trained_pipeline-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

def prediction(data):
    print(data)
    predictions = model.predict(data)
    return predictions[0]