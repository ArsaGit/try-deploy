from fastapi import FastAPI, status


app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {"text": "HI"}


@app.get("/info", status_code=status.HTTP_200_OK)
def read_info():
    return {"info": "testing deployment"}
