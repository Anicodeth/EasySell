from fastapi import FastAPI

from src.webapi.controllers import product_controller, user_controller

app = FastAPI()

app.include_router(user_controller.user_router)
app.include_router(product_controller.product_router)
