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
