from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps

#Login Decorator if user didnt log in, cannot access dashboard
# Kullanıcı Giriş Decorator'ı
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("In order to see this page, please log in.","danger")
            return redirect(url_for("login"))
 
    return decorated_function

# User Register Form / flask-wtf documentation
class RegisterForm(Form):
    name = StringField("Name Surname", validators=[validators.Length(max =25), validators.DataRequired()])
    username = StringField("Username", validators=[validators.Length(max =35), validators.DataRequired()])
    email = StringField("Email", validators=[validators.Length(max =25), validators.DataRequired(),validators.Email(message="Please input valid e-mail address")])
    password = PasswordField("Password:",validators=[
        validators.DataRequired(message="Please input a password..."),
        validators.EqualTo(fieldname="confirm",message="Password couldn't match...")
    ])
    confirm = PasswordField("Password Confirm:")

class LoginForm(Form):
    username = StringField("Username")
    password = PasswordField("Password")
 
#MySql - Flask Config
app = Flask(__name__)
app.secret_key="cemblog2626"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "cemblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

#Articles Page
@app.route('/articles')
def articles():
    cursor = mysql.connection.cursor()

    query = "Select * From article"

    result = cursor.execute(query)

    if result > 0:
        articles = cursor.fetchall()
        return render_template("articles.html",articles = articles)
    else:
        return render_template("articles.html")


@app.route("/dashboard")
@login_required
def dashboard():
    cursor = mysql.connection.cursor()
    query = "Select * FROM article where author=%s"
    result = cursor.execute(query,(session["username"],))

    if result > 0:
        articles = cursor.fetchall()
        return render_template("dashboard.html",articles=articles)
    else:
        return render_template("dashboard.html")


#REGISTER with WTF form 
@app.route("/register",methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)

    if(request.method=="POST") and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()
        query = "INSERT INTO USER(name,email,username,password) VALUES(%s,%s,%s,%s)"
        cursor.execute(query,(name,email,username,password))
        mysql.connection.commit()
        cursor.close()
        flash("Registered successfully...","success")


        return redirect(url_for("login")) #method name
    else:
         return render_template("register.html",form = form)

#LOGIN
@app.route("/login", methods= ["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        username = form.username.data
        password_entered = form.password.data

        cursor = mysql.connection.cursor()
        query = "SELECT * FROM USER WHERE USERNAME=%s"

        result = cursor.execute(query,(username,))
        if(result > 0):
            data = cursor.fetchone()
            real_password = data["password"]
            if sha256_crypt.verify(password_entered,real_password):
                flash("Logged In Successfully","success")


                session["logged_in"] = True
                session["username"] = username


                return redirect(url_for("index"))
            else:
                flash("Password is wrong...","danger")
                return redirect(url_for("login"))

        else:
            flash("There is no user with this username...","danger")
            return redirect(url_for("login"))


    return render_template("login.html",form = form)

#Detail Page
@app.route("/article/<string:id>")
def article(id):
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM article WHERE id = %s"
    result = cursor.execute(query,(id,))

    if result > 0:
        article = cursor.fetchone()
        return render_template("article.html",article=article)
    else:
        return render_template("article.html")

#LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

#Add Article
@app.route("/addarticle",methods = ["GET","POST"])
def addarticle():
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        title = form.title.data
        content = form.content.data

        cursor = mysql.connection.cursor()
        query = "Insert INTO ARTICLE(title,author,content) VALUES(%s,%s,%s)"
        cursor.execute(query,(title,session["username"],content))
        mysql.connection.commit()
        cursor.close()

        flash("Article successfully added!","success")
        return redirect(url_for("dashboard"))
    return render_template("addarticle.html",form = form)

#Article Delete
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cursor = mysql.connection.cursor()
    query = " SELECT * FROM ARTICLE WHERE author =%s and id =%s" #hem bu makale varsa ve bize aitse

    result = cursor.execute(query,(session["username"],id))

    if result > 0:
        query2 = "Delete from article where id = %s"
        cursor.execute(query2,(id,))
        mysql.connection.commit()

        return redirect(url_for("dashboard"))
    else:
        flash("There is no article like that or you don't have permission to delete","danger")
        return redirect(url_for("index"))


#Article Update
@app.route("/edit/<string:id>",methods = ["GET","POST"])
@login_required
def update(id):
    if request.method =="GET":
        cursor = mysql.connection.cursor()

        query = "SELECT * FROM ARTICLE WHERE id=%s and author=%s"
        result = cursor.execute(query,(id,session["username"]))

        if result ==0:
            flash("There is no article like that or you don't have permission to edit","danger")
            return redirect(url_for("index"))
        else:
            article = cursor.fetchone()
            form = ArticleForm()

            form.title.data = article["title"]
            form.content.data = article["content"]
            return render_template("update.html",form = form)

    else:
        #POST REQUEST
        form = ArticleForm(request.form)
        
        newTitle = form.title.data
        newContent = form.content.data

        query = "UPDATE ARTICLE SET title=%s,content=%s where id = %s"
        cursor = mysql.connection.cursor()
        cursor.execute(query,(newTitle,newContent,id))

        mysql.connection.commit()
        flash("Article successfully updated","success")
        return redirect(url_for("dashboard"))

# Article Form
class ArticleForm(Form):
    title = StringField("Article Title",validators=[validators.Length(min=3, max=100)])
    content = TextAreaField("Content of Article",validators=[validators.Length(min=10)])

#Searching URL
@app.route("/search",methods =["GET","POST"])
def search():
    if request.method =="GET":
        return redirect(url_for("index"))
    else:
        keyword = request.form.get("keyword")

        cursor = mysql.connection.cursor()
        query = "SELECT * FROM ARTICLE WHERE title like '%" + keyword +"%'"
        res = cursor.execute(query)

        if res==0:
            flash("There is no article with this keyword...","warning")
            return redirect(url_for("articles"))
        else:
            articles = cursor.fetchall()
            return render_template("articles.html",articles = articles)


if __name__ == "__main__":
    app.run(debug=True)