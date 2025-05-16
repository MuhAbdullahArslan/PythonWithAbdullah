from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def project():
    return render_template('projects.html')

@app.route('/contact',methods= ['GET',"POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        message = request.form['message']
        print(f"Received Message from {name}:{message}")
        return render_template('contact.html',success=True)
    return render_template('contact.html',success=False)

if __name__ == "__main__":
    app.run(debug=True)
    
