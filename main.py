from fastapi import FastAPI, File, UploadFile
import pandas as pd
import numpy as np
from prophet import Prophet
import joblib
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/get/")
async def get_result():
        return "Choosni is a ditcher"


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
        df=pd.read_csv(file.file,error_bad_lines=False)
        df=df[['Date','Primary Type','Description','Arrest','Domestic']]
        df['Date']=pd.to_datetime(df['Date'],format='%m/%d/%Y %I:%M:%S %p')
        df.index=pd.DatetimeIndex(df.Date)
        df.drop("Date",axis=1,inplace=True)
        model_data=df.resample('M').size().reset_index()
        model_data.rename(columns={"Date":"ds",0:"y"},inplace=True)
        model=Prophet()
        model.fit(model_data)
        joblib.dump(model, "trained_prophet_model.pkl")
        return JSONResponse(content={"message": "Model trained and saved."})



@app.post("/predict/")
async def predict(months:int):
        model = joblib.load("trained_prophet_model.pkl")
        future=model.make_future_dataframe(periods=months, freq='MS')
        forecast=model.predict(future)
        return forecast.sort_values("ds")["yhat"].tail(months)





