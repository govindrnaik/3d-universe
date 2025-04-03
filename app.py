import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Space Visualizations")

# Setup template directory
templates = Jinja2Templates(directory="templates")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page redirects to solar system by default"""
    return templates.TemplateResponse(
        "solar_system.html", {"request": request, "active_page": "solar-system"}
    )


@app.get("/solar-system", response_class=HTMLResponse)
async def solar_system(request: Request):
    """Render the solar system visualization page"""
    return templates.TemplateResponse(
        "solar_system.html", {"request": request, "active_page": "solar-system"}
    )


@app.get("/big-bang", response_class=HTMLResponse)
async def big_bang(request: Request):
    """Render the big bang visualization page"""
    return templates.TemplateResponse(
        "big_bang.html", {"request": request, "active_page": "big-bang"}
    )


@app.get("/black-hole", response_class=HTMLResponse)
async def black_hole(request: Request):
    """Render the black hole visualization page"""
    return templates.TemplateResponse(
        "black_hole.html", {"request": request, "active_page": "black-hole"}
    )


@app.get("/voyager-mission", response_class=HTMLResponse)
async def voyager_mission(request: Request):
    """Render the Voyager 1 mission visualization page"""
    return templates.TemplateResponse(
        "voyager_mission.html",
        {"request": request, "active_page": "voyager-mission"},
    )


@app.get("/starlink-network", response_class=HTMLResponse)
async def starlink_network(request: Request):
    """Render the Starlink satellite network visualization page"""
    return templates.TemplateResponse(
        "starlink_network.html", {"request": request, "active_page": "starlink-network"}
    )


@app.get("/chandrayaan-mission", response_class=HTMLResponse)
async def chandrayaan_mission(request: Request):
    """Render the Chandrayaan-3 mission visualization page"""
    return templates.TemplateResponse(
        "chandrayaan_mission.html",
        {"request": request, "active_page": "chandrayaan-mission"},
    )


@app.get("/mangalyaan-mission", response_class=HTMLResponse)
async def mangalyaan_mission(request: Request):
    """Render the Mangalyaan 3 mission visualization page"""
    return templates.TemplateResponse(
        "mangalyaan_mission.html",
        {"request": request, "active_page": "mangalyaan-mission"},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
