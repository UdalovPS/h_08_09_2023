from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory='static', html=True), name='static')

templates = Jinja2Templates(directory='templates')


@app.get("/", response_class=HTMLResponse)
async def get_index_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict_one")
async def predict_one_person(name = Form(),
                             age = Form(),
                             some = Form(),
                             sel = Form(),
                             price = Form(),
                             check_1: bool = Form(False),
                             check_2: bool = Form(False),
                             flexRadioDefault = Form()):

    form_dict = {
        "name": name,
        "age": age,
        "some": some,
        "select": sel,
        "price": price,
        "check_1": check_1,
        "check_2": check_2,
        "flexRadioDefault": flexRadioDefault
    }
    return form_dict
