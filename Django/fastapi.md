```
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
    
```
@ is path operation decorator

get in path operation

"/items/{item_id}" is path

read_item is path operation function

Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}:

When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.
And you don't have to declare them in any specific order.

If the parameter is also declared in the path, it will be used as a path parameter.

If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.

If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(title="Query string", min_length=3)] = None,
):
```
You can use Path for validating numeric and Query for validating string in query parameters,

You can use Pydantic models to declare query parameters in FastAPI