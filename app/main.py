from fastapi import FastAPI, HTTPException , Query , Path
from services.products import get_all_products
from schemas.product import product

app = FastAPI()

@app.get('/')
def root():
    return {'message':"Welcome To FastApi"}

# @app.get("/products/{id}")
# def get_products(id:int):
#     products= ['Brush', 'laptop', 'Mouse', 'Moniter']
#     return products[id]

# @app.get("/products")
# def get_products():
#     return services.products.get_all_products()
    
@app.get("/products")
def list_products(name:str = Query(
    default=None,
    min_length=1,
    max_length=50, 
    description="Search by product Name (case insensitive)",
    example="Ahmad"
    
    ),

    sort_by_price: bool=Query(
        default=False,
        description="Sort Products By Price"
        

        ),

    order:str=Query(
        default="asc",
        description="Sort order When Sort_By_Price=true (asc, desc)"),

    limit: int=Query(
        default=4,
        ge=1,
        le=100,
        description="Number of Items to return"
    ),
    offset: int=Query(
        default=0,
        ge=0,
        description="Pagination offset"),
    
):
    products = get_all_products()
    
    if name:
        needle= name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]
    
        if not products:
            raise HTTPException(
                status_code=404, detail=f"No product Found mtching name={name}"
            )
        if sort_by_price:
            reverse = order =="desc"
            products=sorted(products, key=lambda p:p.get("price",0), reverse=reverse)


        total= len(products)
        products=products[offset:offset+limit]

 
    return {"total": total, "limit":limit, "items":products}



@app.get("/products/{product_id}")
def get_product_by_id(
    product_id:str= Path(
        min_length=36,
        max_length=36,
        description="UUID of The Products",
        example="394d40e7-2a95-445d-8738-c6af6be5a97e"
    )):

    products= get_all_products()
    for product in products :
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product Not Found")

@app.post("/products/", status_code=201)
def create_product(product: product):
    return product