from fastapi import FastAPI 

app = FastAPI()

@app.route("/")
def HomePage():
    return {
        "message" : "Home page"
    }