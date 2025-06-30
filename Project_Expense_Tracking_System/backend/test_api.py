from fastapi import FastAPI

app = FastAPI()

@app.post("/test-post")
def dummy_test_post():
    return {"message": "POST request successful!"}
