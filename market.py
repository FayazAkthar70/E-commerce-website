from flask import Flask, render_template
import psycopg2

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    
    while True:
        try:
            conn = psycopg2.connect(host= app.config.get("DATABASE_HOSTNAME") , database = app.config.get("DATABASE_NAME"), user = app.config.get("DATABASE_USERNAME") , password = app.config.get("DATABASE_PASSWORD"))
            cur = conn.cursor()
            print("database connection successfull")
            break
        except Exception as error:
            print  ("error" , error)
            time.sleep(2)
            
    
    
    cur.execute("""CREATE TABLE IF NOT EXISTS items ( 
        id serial primary key not null,
        name varchar(30) not null,
        price int ,
        barcode char(30) not null unique,
        description text);
    """)
    conn.commit()
    print("table created successfully")

    @app.route("/")
    @app.route("/home")
    def get_home():
        

        return render_template('home.html')

    @app.route("/market")
    def get_market():
        cur.execute("""select * from items""")
        items = cur.fetchall()
        print(items[0])
        return render_template('market.html', items=items)
    return app