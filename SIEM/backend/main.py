from fastapi import FastAPI

app = FastAPI(
    title="AD-Range SIEM API",
    description="Security Information and Event Management API for AD-Range",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "AD-Range SIEM API is running"
    }