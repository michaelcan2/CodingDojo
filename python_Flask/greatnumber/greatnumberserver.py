from flask import Flask, render_template, request, session
import random 
app = Flask(__name__)
app.secret_key= 'secretnumberrserver'
#  this route connects the homepage to the server----The '/' HAS TO BE ONLY THAT IT CANT BE ADJUSTED
@app.route("/")

def home():
    return render_template('home.html')

# you dont have to set your app.route method as I would believe it would be set to GET, however since you wanted this input info for 
# this game to be secret,you call this method POST
# Our route is waiting to receive a POST request to the route because we assigned it to wait for a request called post from the route
# thats connected to our html form.
# ****whatever you name this route after the ++/++ will be seen and needed to type in if you wanted to reach this particular page.
@app.route("/the_route_to_connect_the_form_answer_inputted_by_the_user", methods=['POST'])
def the_function_to_connect_the_form_answer_inputted_by_the_user():
# request.form links to the form in html w/e the answer that the user inputs, also the parameter in py is 'num' and the parameter is named 
# 'num' in the html in the form under input, name
# num is in [] because that is how you contain information in a request form.
# you are linking them.
    num = int(request.form['num'])
    # means if random number parameter called 'num1' in py is not saved yet in session then it will now be saved in session as a INTEGER
    # between ((1 and 100.)) !!!!!request.form originally saves only as a string so you must specifiy it is an integer
    if 'num1' not in session:
        session['num1'] = int(random.randint(1, 100))
 
    if num > session['num1']:
        answer  = "Too high"
    elif num < session['num1']:
        answer  = "Too low"
    elif num == session['num1']:
        answer  = str(num) + " was the number!\nYou started new game with new number!"
        session['num1'] = int(random.randint(1, 100))
# BELOW means 
    return render_template('home.html', num = num, num1 = session['num1'], answer  = answer)

app.run(debug=True)
# app.secret_key= 'secretnumberrserver'
# @app.route('/')
# def homepage():
#     return render_template('home.html')
#     if not answer in session:
#         session['answer']= random.randint(0,101)

# @app.route('/users',methods=["POST"])
# def the_guess_from_the_player():
#     # users used to connect the form information back to the server.py
#     print "form info recieved"
# hint_for_player_if_too_high_or_too_low 

#     return render_template('home.html')