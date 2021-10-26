#render_template allows for other files to be called in return statements
from flask import Flask, render_template, request, url_for, redirect#import flask into this file and render_template
import random

import mysql.connector #import SQL

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "3072", database ="FreshFood_Database") #connect to database, bad practive since problems with multiple connecctions and errors can occur, but fine for single user only
mycursor = mydb.cursor()

restaurants = ["Applebees", "Olive Garden", "McDonalds", "Popeyes"]
app = Flask(__name__)

print(__name__) 

@app.route('/', methods=['GET', 'POST']) #someone has visited base url and we have to provide information
def login(): #return some object to be displayed to the user | general python syntax for defining a function
    if request.method == 'POST':
        return redirect(url_for('dropdown'))
    return render_template('home.html') #name='Irfan'

@app.route('/about')
def about(): #name of function and name of route do not have to match
    return 'This is a url shortener'

@app.route('/register', methods=['GET', 'POST'])
def registration_form():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        street = request.form.get('street')
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')
        zipcode = request.form.get('zipcode')
        phonenum = request.form.get('phoneNum')
        emailaddress = request.form.get('emailAddress')
        creditcard = request.form.get('creditCard')
        userID = random.randint(0, 1000000)
        mycursor.execute("INSERT INTO User_Profile(User_ID,city,state,street,country,zip_code,user_password,username,phoneNum,email_address,credit_card_number) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
         (userID, city, state, street, country, zipcode, password, name, phonenum,emailaddress,creditcard))
        mydb.commit()
        return redirect(url_for('login'))
    return render_template('registration_form.html')

@app.route('/Restaurant', methods=['GET', 'POST'])
def dropdown():
    if request.method == 'POST':
        return redirect(url_for('menu'))
    return render_template('dropdown.html', content = ["Applebees", "Olive Garden", "McDonalds", "Popeyes"])

@app.route('/menu', methods=['GET', 'POST']) #someone has visited base url and we have to provide information
def menu(): #return some object to be displayed to the user | general python syntax for defining a function
    if request.method == 'POST':

        return redirect(url_for('orderStats'))

    return render_template('menu.html') #name='Irfan'

@app.route('/orderStats', methods=['GET', 'POST']) #someone has visited base url and we have to provide information
def orderStats(): #return some object to be displayed to the user | general python syntax for defining a function
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('orderStats.html') #name='Irfan'

if __name__ == "__main__":
    app.run()

