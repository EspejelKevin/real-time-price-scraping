erDiagram
    PRODUCT ||--o{ PRICE_HISTORICAL : "tiene muchos"
    PRODUCT ||--o{ LOGS : "genera"
    
    PRODUCT {
        int id PK
        string name
        string url
        string store
        string scraping_strategy
        string selector
        float target_price
        string email
        string status
    }
    
    PRICE_HISTORICAL {
        int id PK
        int product_id FK
        float price
        datetime date
        int year
        int month
        int day
    }
    
    LOGS {
        int id PK
        int product_id FK
        string error_message
        datetime date
    }