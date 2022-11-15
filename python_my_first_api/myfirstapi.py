from fastapi import FastAPI

app = FastAPI()

@app.get("/my-first-api")
def hello(name = None):

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return text

@app.get("/read-remote-csv")
def read_remote_csv():
    import pandas as pd
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    output = pd.read_csv(url)

    return output
'''
simulating adding to database
'''
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}
