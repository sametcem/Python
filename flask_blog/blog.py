from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def index():
    numbers = [1,2,3,4,5] # () okay

    articles = [
        {"id":1,"title":"Book 1", "content":"Book1 content"},
        {"id":2,"title":"Book 2", "content":"Book2 content"},
        {"id":3,"title":"Book 3", "content":"Book3 content"}

    ]
    return render_template("index.html",islem = 2,articles = articles)

@app.route("/about")
def about():
    return render_template("about.html")

#Dynamic URL
@app.route("/articles/<string:id>")
def detail(id):
    return "Article Id:" + id

if __name__ == "__main__":
    app.run(debug=True)