from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
# class Base(DeclarativeBase):
#     pass
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
# db = SQLAlchemy(model_class=Base)
# db.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# db.create_all()


# # CREATE TABLE IN DB
# class User(db.Model):
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     email: Mapped[str] = mapped_column(String(100), unique=True)
#     password: Mapped[str] = mapped_column(String(100))
#     name: Mapped[str] = mapped_column(String(1000))
 
# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    # return render_template("index.html")
    # Passing True or False if the user is authenticated. 
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        # if User.query.filter_by(email=request.form.get('email')).first():
        #     #User already exists
        #     flash("You've already signed up with that email, log in instead!")
        #     return redirect(url_for('login'))
        
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_and_salted_password,
        )
        
        db.session.add(new_user)
        db.session.commit()

        #Log in and authenticate user after adding details to database.
        login_user(new_user)
        
        # return redirect(url_for("secrets"))
        return redirect(url_for("secrets", name=new_user.name))

    # return render_template("register.html")
    # Passing True or False if the user is authenticated. 
    return render_template("register.html", logged_in=current_user.is_authenticated)


# @app.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form.get('email')
#         password = request.form.get('password')
        
#         #Find user by email entered.
#         user = User.query.filter_by(email=email).first()
        
#         #Check stored password hash against entered password hashed.
#         if check_password_hash(user.password, password):
#             login_user(user)
#             return redirect(url_for('secrets'))
          
#     return render_template("login.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        result = db.session.execute(db.select(User).where(User.email == email))
    
        # user = User.query.filter_by(email=email).first()
        user = result.scalar()
        #Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        #Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        #Email exists and password correct
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    # return render_template("login.html")
    # Passing True or False if the user is authenticated. 
    return render_template("login.html", logged_in=current_user.is_authenticated)

# @app.route('/secrets/<name>')
# def secrets(name):
#     return render_template("secrets.html", name=name)

@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    # return render_template("secrets.html", name=current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory='static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
