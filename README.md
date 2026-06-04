# FastAPI Product Catalog API

A RESTful Product Catalog API built with **FastAPI** that provides product management features including search, filtering, sorting, pagination, UUID-based retrieval, and product creation using JSON file storage.

---

##  Features

-  Search products by name (case-insensitive)
-  Sort products by price (ascending/descending)
-  Pagination (limit & offset)
-  UUID-based product retrieval
-  Create new products
-  FastAPI high-performance backend
-  JSON file-based storage

---

##  Tech  Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON (file database)

---


## Installation & Setup

### Clone repo
```bash
git clone https://github.com/your-username/fastapi-product-catalog-api.git
cd fastapi-product-catalog-api
````

### Create virtual environment

```bash
python -m venv venv
```

### Activate environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run server

```bash
uvicorn main:app --reload
```

---

##  API Endpoints

### Root

```
GET /
```

### Get Products

```
GET /products
```

Query Params:

* `name` → search by name
* `sort_by_price` → true/false
* `order` → asc/desc
* `limit` → number of items
* `offset` → pagination

---

### Get Product by ID

```
GET /products/{product_id}
```

---

### Create Product

```
POST /products/
```

---

##  Example Request

```
/products?name=phone&sort_by_price=true&order=asc&limit=5&offset=0
```

---

##  API Docs

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

---

##  Future Improvements

* Add PostgreSQL / MongoDB database
* Implement update & delete endpoints
* Add JWT authentication
* Add pytest test cases
* Dockerize the project

---

##  Author

Muhammad Ahmad
Software Engineering Student | COMSATS University
Backend & AI Enthusiast

```

---

If you want next step, I can also make your GitHub repo look **professional like internship-level (badges + banner + screenshots + Docker + CI/CD)** 🚀
```
