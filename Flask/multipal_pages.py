from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return "HomePage"

@app.route("/register")
def register():
    return "Register Page"

# we run code in debug mode 
if __name__ == "__main__":
    app.run(debug=True)