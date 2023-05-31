from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def HelloWorld():
    sum = 1 + 1
    return {"message": "Hello, World! (%s)" % sum}