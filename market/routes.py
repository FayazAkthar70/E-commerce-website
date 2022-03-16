from market import app, cur
from flask import render_template

@app.route("/")
@app.route("/home")
def get_home():
    

    return render_template('home.html')

@app.route("/market")
def get_market():
    cur.execute("""select * from items""")
    items = cur.fetchall()
    
    return render_template('market.html', items=items)