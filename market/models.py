from market import cur,conn



cur.execute("""CREATE TABLE IF NOT EXISTS items ( 
    id serial primary key not null,
    name varchar(30) not null,
    price int ,
    barcode char(12) not null unique,
    description text);
""")
conn.commit()
print("table created successfully")