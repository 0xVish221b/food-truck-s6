DROP TABLE IF EXISTS food;

CREATE TABLE food(id SERIAL PRIMARY KEY, name TEXT NOT NULL, image_url TEXT, price_in_cents INTEGER NOT NULL);

INSERT INTO food(name, image_url, price_in_cents) VALUES
    ('Egg tart', 'https://cn.foodporn.zone/wp-content/uploads/2021/09/shutterstock_146112062-1024x683.jpg', 300),
    ('Crepe', 'https://www.angsarap.net/wp-content/uploads/2017/01/Hachijo-Dori-Street-Food-Crepes-04.jpg', 550),
    ('Taiyaki', 'https://cdn1.jp.orstatic.com/userphoto/Article/0/D/0002MT2E720422AFD91FEEj.jpg', 400);
