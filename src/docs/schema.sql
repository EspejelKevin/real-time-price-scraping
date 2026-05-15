CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url TEXT NOT NULL,
    store VARCHAR(50) NOT NULL,
    scraping_strategy VARCHAR(50) NOT NULL,
    selector TEXT NOT NULL,
    target_price DECIMAL(10, 2),
    email VARCHAR(255) NOT NULL UNIQUE,
    status VARCHAR(50) DEFAULT 'activo'
);

CREATE TABLE IF NOT EXISTS price_historical (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    price DECIMAL(10, 2),
    date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    year INTEGER,
    month INTEGER,
    day INTEGER

    CONSTRAINT fk_product
    FOREIGN KEY(product_id)
    REFERENCES products(id)
    ON DELETE CASCADE;
);

CREATE TABLE IF NOT EXISTS logs (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    error_message TEXT,
    date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP

    CONSTRAINT fk_product
    FOREIGN KEY(product_id)
    REFERENCES products(id)
    ON DELETE CASCADE;
);

CREATE INDEX idx_historical_product_date ON price_historical(product_id, date);
CREATE INDEX idx_status_products ON products(status);