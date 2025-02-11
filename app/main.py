from fastapi import FastAPI
from app.routers import auth, products, cart, orders

app = FastAPI(title="Mini Mart")



# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

@app.get("/")

async def root():
    return {"message": "Welcome to Mini Mart! What do you want?"}