from market import cur,conn

cur.execute("""CREATE TABLE IF NOT EXISTS Users(
   id serial PRIMARY KEY     NOT NULL,
   name           TEXT    NOT NULL,
   email    text unique     NOT NULL,
   password   text not null,
   budget int not null default 1000);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS items ( 
    id serial primary key not null,
    name varchar(30) not null,
    price int ,
    barcode char(12) not null unique,
    description text, 
    owner_id int not null,
    constraint fk_users foreign key (owner_id) references users(id) on delete cascade);
""")



conn.commit()
print("tables created successfully")