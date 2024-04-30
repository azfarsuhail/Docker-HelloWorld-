from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read():
    return [{"Hello":"World"},
            {"Made in":"Poetry"},
            {"Developed by":"FastAPI"},
            {"Upload in ":"Images"},
            {"Running in ":"Docker"},
        ]
