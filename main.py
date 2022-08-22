from rosreestr2coord import Area
import json
import pandas as pd
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from time import sleep

app = FastAPI()


@app.get('/geojson')
def get_somebody():
  with open('list.txt', 'r') as f:
    codes = f.readlines()
  
  areas = []
  
  for code in codes:
    sleep(3)
    area = Area(code, with_proxy=True)
    geojson = area.to_geojson(geom_type="polygon")
    
    if isinstance(geojson, str):
      areas.append(json.loads(geojson))

  return {
    "data": areas,
    "count": len(areas)
  }


@app.get('/excel')
def get_excel():
  dataframe1 = pd.read_excel('2022_08_22_12_07_25.xlsx')
  return dataframe1

  
  
