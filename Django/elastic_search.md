# add(index) a single document
```
POST /my_index/my_type
{
  "title": "Elasticsearch Auto ID",
  "description": "This document has an auto-generated ID.",
  "tags": ["auto", "id", "example"],
  "published_date": "2024-12-05"
}
```
# indexing multiple documents bulk_post->
```
POST /_bulk
{ "index": { "_index": "my_index", "_type": "my_type" } }
{ "title": "Document 1", "description": "This is the first document." }
{ "index": { "_index": "my_index", "_type": "my_type" } }
{ "title": "Document 2", "description": "This is the second document." }
```

# Deletion of single document of id 1

DELETE /my_index/my_type/1
# delete index
DELETE /my_index 
# bulk delete
POST /_bulk
```
{ "delete": { "_index": "my_index", "_type": "my_type", "_id": "1" } }
{ "delete": { "_index": "my_index", "_type": "my_type", "_id": "2" } }
```
# delete by query
```
POST /my_index/my_type/_delete_by_query
{
  "query": {
    "match": {
      "status": "inactive"
    }
  }
}
```
# update by id(1)
POST /my_index/my_type/1/_update
{
  "doc": {
    "description": "Updated description for Elasticsearch."
  }
}
# update with upsert

```
POST /my_index/my_type/1/_update
{
  "doc": {
    "description": "Updated description with upsert.",
    "tags": ["updated", "elasticsearch"]
  },
  "upsert": {
    "title": "New Document",
    "description": "This is a new document as upsert example."
  }
}
```
# bulk update on available _id
```
POST /_bulk 
{ "update": { "_index": "my_index", "_type": "my_type", "_id": "1" } }
{ "doc": { "description": "Updated description for Document 1." } }
{ "update": { "_index": "my_index", "_type": "my_type", "_id": "2" } }
{ "doc": { "description": "Updated description for Document 2." } }
```
# putting mappings for making index
```
PUT /example_index
{
  "settings": {
    "number_of_shards": 3,   // Number of primary shards
    "number_of_replicas": 2  // Number of replica shards
  },
  "mappings": {
    "properties": {
      "title": { "type": "text" },
      "tags": { "type": "keyword" },
      "views": { "type": "integer" },
      "created_at": { "type": "date", "format": "yyyy-MM-dd" },
      "location": { "type": "geo_point" },
      "comments": {
        "type": "nested",
        "properties": {
          "user": { "type": "text" },
          "message": { "type": "text" }
        }
      },
      "ip_address": { "type": "ip" }
    }
  }
}
```
## putting mapping with tokenization
```
PUT /comma_tokenization_index
{
  "settings": {
    "analysis": {
      "tokenizer": {
        "comma_tokenizer": {
          "type": "pattern",
          "pattern": ","
        }
      },
      "analyzer": {
        "comma_analyzer": {
          "type": "custom",
          "tokenizer": "comma_tokenizer",
          "filter": ["trim", "lowercase"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "tags": {
        "type": "text",
        "analyzer": "comma_analyzer"
      }
    }
  }
}
```