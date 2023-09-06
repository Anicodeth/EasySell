from fastapi import FastAPI
from WebApi.Controllers import user_controller, product_controller

app = FastAPI()

# Mount the user controller's router under the '/users' path
app.include_router(user_controller.router, prefix="/users", tags=["Users"])

# Mount the product controller's router under the '/products' path
app.include_router(product_controller.router, prefix="/products", tags=["Products"])

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
