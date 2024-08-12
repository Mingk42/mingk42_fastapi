from typing import Union

from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

#df = pd.read_parquet("/home/root2/code/ffapi/data/")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sample")
def sample_data():
    df = pd.read_parquet("/home/root2/code/ffapi/data/")

    sample_df=df.sample(n=5)
    r= sample_df.to_dict(orient="records")

    return r


@app.get("/movie/{movie_cd}")
def movie_meta(movie_cd: int):
    df = pd.read_parquet("/home/root2/code/ffapi/data/")
    
    df_select = df.loc[df["movieCd"]==str(movie_cd)].to_dict()

    if sum(df["movieCd"]==str(movie_cd))<1:
         raise HTTPException(status_code=404, detail="영화를 찾을 수 없습니다.")

    """
    meta_df=df[df['movieCd']==movie_cd]
    
    if meta_df.empty():
        raise HTTPException(status=404, detail="영화를 찾을 수 없습니다.")
    
    return meta_df
    """
    # return {"movie_cd": movie_cd, "df_count":len(df), "query":df_select}
    return df_select
