from flask import Flask,url_for,redirect

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return "Hello Admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f"Hello {guest} Welcome"

@app.route('/user/<name>')
def user_name(name):
    if name == "admin":
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))
    
if __name__ == '__main__':
    app.run(debug=True)