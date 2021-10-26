#render_template allows for other files to be called in return statements
from flask import Flask, render_template, request, url_for, redirect#import flask into this file and render_template
restaurants = ["Applebees", "Olive Garden", "McDonalds", "Popeyes"]
app = Flask(__name__)

print(__name__) 

@app.route('/') #someone has visited base url and we have to provide information
def login(): #return some object to be displayed to the user | general python syntax for defining a function
    return render_template('home.html') #name='Irfan'

@app.route('/about')
def about(): #name of function and name of route do not have to match
    return 'This is a url shortener'

@app.route('/register', methods=['GET', 'POST'])
def registration_form():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('registration_form.html')

@app.route('/Restaurant')
def dropdown():
    return render_template('dropdown.html', content = ["Applebees", "Olive Garden", "McDonalds", "Popeyes"])

if __name__ == "__main__":
    app.run()



# from flask import Flask, render_template
# restaurants = ["Applebees", "Olive Garden", "McDonalds", "Popeyes"]
# app = Flask(__name__)

# # @app.route("/<name>")
# # def home(name):
# #     return render_template("index.html", content = name)

# @app.route("/Restaurant")
# def dropdown():
#     return render_template("dropdown.html", content = ["Applebees", "Olive Garden", "McDonalds", "Popeyes"])

# if __name__ == "__main__":
#     app.run()