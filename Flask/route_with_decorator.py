from flask import Flask

app = Flask(__name__) # flask construcor


@app.route('/')
def hello():
    return "Hello Web-FrameWork Flask"

if __name__ == "__main__":
    app.run(debug=True)