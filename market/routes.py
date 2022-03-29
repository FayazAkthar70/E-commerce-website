from crypt import methods
from market import app, cur, conn
from flask import render_template, redirect, url_for
from market.forms import RegisterForm
from market.model import Create_User

@app.route("/")
@app.route("/home")
def get_home():
    

    return render_template('home.html')

@app.route("/market")
def get_market():
    cur.execute("""select * from items""")
    items = cur.fetchall()
    
    return render_template('market.html', items=items)

@app.route("/register", methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user = Create_User(username=form.username.data,
                                     email_address=form.email_address.data,
                                     password=form.password1.data)
        cur.execute("INSERT INTO users (name, email, password,budget) VALUES(%s, %s, %s,%s);", (user.username, user.email_address, user.password, user.budget)) 
        conn.commit()
        print('inserted data')
        return redirect(url_for('get_market'))
    if form.errors != {}:
        for err_msg in form.errors.values:
            print(f"There was an error in creating user : {err_msg}")
            
    return render_template('register.html', form=form)