- You can use the jsonable_encoder to convert the input data to data that can be stored as JSON (e.g. with a NoSQL database). For example, converting datetime to str.
- PUT is used to receive data that should replace the existing data.
- You can also use the HTTP PATCH operation to partially update data.
# Partial update 
## 1. using  exclude_unset 
- If you want to receive partial updates, it's very useful to use the parameter exclude_unset in Pydantic's model's .model_dump().
```
@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
```
## 2. Using Pydantic's update parameter
Now, you can create a copy of the existing model using .model_copy(), and pass the update parameter with a dict containing the data to update.
```
@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
```

