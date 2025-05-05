from flask import Flask

app = Flask(__name__)

def hello_world():
    return "Hello World"
def hello_houses():
    return 'houses'

# app.add_url_rule(route,return_statement,function_name)
app.add_url_rule('/', 'hello_world', hello_world)
app.add_url_rule('/houses', 'houses', hello_houses)

if __name__ == "__main__":
    app.run(debug=True)
