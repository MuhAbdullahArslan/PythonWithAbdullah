from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my_Flask_Website"

# String Variable in Flask
@app.route("/string/<name>")
def hello_name(name):
    return f"Welcom {name}" 

# integer Variable in Flask
@app.route('/integer/<age>')
def age(age):
    return f"You are {age}year old."

# Float Variable in Flask
@app.route('/float/<balance>')
def balance(balance):
    return f"Your Current Balance is {balance}"

if __name__ == "__main__":
    app.run(debug=True)
    
