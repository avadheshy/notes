# Rules for making yaml file from json file
1. Remove curly braces {} and square brackets [].
2. Use indentation to represent hierarchy (use spaces, not tabs).
3. Replace key-value pairs with key: value syntax.
4. Use - to represent arrays (lists).
5. Quotes are not required unless needed for special characters or clarity.
6. Comments can be added using #.
   
---
   ```
   {
  "project": {
    "name": "NextGen Platform",
    "version": "1.3.5",
    "contributors": [
      { "name": "Alice", "role": "Lead Developer" },
      { "name": "Bob", "role": "DevOps Engineer" }
    ],
    "features": {
      "authentication": {
        "enabled": true,
        "providers": ["Google", "GitHub", "Email"]
      },
      "analytics": {
        "enabled": false,
        "tools": null
      }
    },
    "environments": {
      "development": {
        "debug": true,
        "db": {
          "host": "localhost",
          "port": 5432
        }
      },
      "production": {
        "debug": false,
        "db": {
          "host": "prod.db.server",
          "port": 5432
        }
      }
    }
  }
}

   ```
   ---
```
project:
  name: NextGen Platform
  version: "1.3.5"
  contributors:
    - name: Alice
      role: Lead Developer
    - name: Bob
      role: DevOps Engineer
  features:
    authentication:
      enabled: true
      providers:
        - Google
        - GitHub
        - Email
    analytics:
      enabled: false
      tools: null
  environments:
    development:
      debug: true
      db:
        host: localhost
        port: 5432
    production:
      debug: false
      db:
        host: prod.db.server
        port: 5432

   ```