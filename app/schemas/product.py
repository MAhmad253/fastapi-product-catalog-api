from pydantic import BaseModel, Field ,AnyUrl ,field_validator ,model_validator ,computed_field, EmailStr
from typing import Annotated , Literal, Optional , List 
from uuid import UUID 
from datetime import datetime


class seller(BaseModel):
    seller_id: UUID
    name:Annotated[str,Field(
         min_length=3,
         max_length=80,
         title="Name of The Seller",
         description="Seller Name (3-80 chars)",
         examples=["Apple Store, Mi Store"]
    ),
    ]
    email:EmailStr
    website:AnyUrl

    @field_validator("email",mode="after")
    @classmethod
    def validate_seller_Email_Domain(cls, value:EmailStr):
        allowed_domains=["mistore.pk., hpworld.pk"]
        domain=str(value).split("@")[-1].lower()
        if domain not in  allowed_domains:
             raise ValueError(f"Seller Email Domain is not Available {domain}") 
        return value



class product(BaseModel):
    id: UUID
    sku:Annotated[
        str,Field(
            min_length=6,
            max_length=36,
            title="Sku",
            description="Stock Keeping Unit",
            examples=["XIAO-359GB-004"]
        ),
    ]
    name:Annotated[str,Field(
         min_length=3,
         max_length=80,
         title="Name of The Product",
         description="Product Name (3-80 chars)",
         examples=["Xiaomi Model Pro, Apple Model X"]
    ),
    ]
    description:Annotated[str,Field(
            max_length=200,
            description="Short Product Description"
    ),]
    category: Annotated[str,Field(
            min_length=3,
            max_length=30,
            description="Category Like Laptops/Mobiles/Accessories",
            examples=["Mobile , Laptop, Accessories"]
    ),]
    brand: Annotated[str, Field(
            min_length=2,
            max_length=40,
            examples=["Xiaomi, Apple"]
    ),]
    price: Annotated[float,Field(
        gt=0,
        strict=True,
        description="Base Price (Pkr)"
    ),]
    currency: Literal["Pkr"] = "Pkr"
            
    discount_percent: Annotated[int,Field(
        ge=0,
        le=90,
        description="Discount is in percentage (0-90)"
    ),]=0   # we put 0 at the end because when user cnnot put anything it set 0 as default
    stock: Annotated[int,Field(
          ge=0,
          description="Available Stock (>=0)"
    ),]
    is_active:Annotated[bool,Field(
        description="Is product Active?"
    ),]
    rating: Annotated[float,Field(
        ge=0,
        le=5,
        strict=True, # strict=True tells Pydantic not to automatically convert values to the required type.
        description="Rating out of 5"
    ),]

    tags: Annotated[
        Optional[list[str]],
        Field(default=None, max_length=10, description="Upto 10 tags"),         
     ]
    image_urls:Annotated[
        List[AnyUrl],
        Field(max_length=1,description="At least 1 Image Url")
        ]
    
    sellers:seller

    created_at:datetime


    @field_validator("sku",mode="after")
    @classmethod
    def validate_sku_format(cls, value:str):
        if "-" not in value:
            raise ValueError("Sku must have '-' ")
        
        last=value.split("-")[-1]
        if not(len(last)==3 and last.isdigit()):
            raise ValueError("Sku must have at last 3 digit intiger like -567")
        
        return value
    

    @model_validator(mode="after")
    @classmethod
    def validate_business_rule(cls, model: "product"):
        if model.stock == 0 and model.is_active is True:
               raise ValueError("If stock is 0 Is_Active must be False")
        
        if model.discount_percent > 0 and model.rating == 0 :
               raise ValueError("Discounted Product Must Have rating (rating != 0)")
        return model
        
    @computed_field
    @property
    def final_price(self)->float:
         return round (self.price *(1-self.discount_percent/100),2)
    
        