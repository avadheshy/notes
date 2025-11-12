# Type hints(also called "type annotations") ?

- These "type hints" or annotations are a special syntax that allow declaring the type of a variable.
- You can declare all the standard Python types
- Type is defined with colon(:) symbol.

```
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e
```
```
def process_items(items: list[str]):
    pass
# That means: "the variable items is a list, and each of the items in this list is a str".

```

```
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    pass
# The variable items_t is a tuple with 3 items, an int, another int, and a str.
# The variable items_s is a set, and each of its items is of type bytes.
```

```
def process_items(prices: dict[str, float]):
    pass
# The keys of this dict are of type str (let's say, the name of each item).
# The values of this dict are of type float (let's say, the price of each item).
```
```
def process_item(item: int | str):
    pass
#this means that item could be an int or a str
```
```
from typing import Optional


def say_hi(name: Optional[str] = None):
    pass
# name is always a str, when it could actually be None too.
```

```
def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"
# The important thing to remember is that the first type parameter you pass to Annotated is the actual type. The rest, is just metadata for other tools.
```
```Avoid using Optional[SomeType]
Instead  use Union[SomeType, None] 
```
FastAPI is a class that inherits directly from Starlette.

# Path Parameters¶
- You can declare path "parameters" or "variables" with the same syntax used by Python format strings.
```
@app.get("/items/{item_id}")
async def read_item(item_id):
    pass
# The value of the path parameter item_id will be passed to your function as the argument item_id.

```
- All the data validation is performed under the hood by Pydantic, so you get all the benefits from it. And you know you are in good hands.
- Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}

# Query Parameters
- When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.
```
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    pass
the query parameters are:skip: with a value of 0, limit: with a value of 10
```
- You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which. And you don't have to declare them in any specific order. They will be detected by name:

# Request Body
- To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.
- Model made with pydantic is called schema
- You can declare body, path and query parameters, all at the same time.
# Annotated 
Annotated can be used to add metadata to your parameters.
# Query Parameters and String Validations¶

```
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None,):
# We are going to enforce that even though q is optional, whenever it is provided, its length doesn't exceed 50 characters.

q: str | None = None # q: Annotated[str | None] = None
# both are same
```
This is how you would use Query() as the default value of your function parameter, setting the parameter max_length to 50:
```
async def read_items(q: str | None = Query(default=None, max_length=50)):
```
Using Annotated is recommended instead of the default value in function parameters.
## Generic validations and metadata:

```
alias # alternate name for the parameter in the URL
title # displayed in the OpenAPI docs
description # # longer doc
deprecated #  # marks it as deprecated in docs
```
## Validations specific for strings:
```
min_length 
max_length
pattern #regex
```
## Custom validations using 
```
AfterValidator
```
# Path Parameters and Numeric Validations¶
A path parameter is always required as it has to be part of the path. Even if you declared it with None or set a default value, it would not affect anything, it would still be always required.
```
@app.get("/items/{item_id}")
async def read_items(*,item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],q: str,size: Annotated[float, Query(gt=0, lt=10.5)],):
```

# Query Parameter Models¶
If you have a group of query parameters that are related, you can create a Pydantic model to declare them.

```
class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
```
In some special use cases (probably not very common), you might want to restrict the query parameters that you want to receive.