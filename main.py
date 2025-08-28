from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/status")
def get_status():
    return {"damaged_system": "engines"}

@app.get("/repair-bay")
def repair_bay():
    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Repair</title></head>
    <body>
      <div class="anchor-point">ENG-04</div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)

@app.post("/teapot")
def teapot():
    return Response(status_code=418)
