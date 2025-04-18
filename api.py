from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from utils import mask_email

app = FastAPI()
model = joblib.load('saved_models/classifier.pkl')

class EmailInput(BaseModel):
    email_body: str

@app.post("/classify")
def classify_email(input_data: EmailInput):
    original_email = input_data.email_body
    masked_email, entities = mask_email(original_email)
    category = model.predict([masked_email])[0]

    return {
        "input_email_body": original_email,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
