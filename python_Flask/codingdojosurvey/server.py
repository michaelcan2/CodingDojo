from flask import Flask, render_template, request, redirect, flash, session 

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
#  this route connects the homepage to the server----The '/' HAS TO BE ONLY THAT IT CANT BE ADJUSTED
@app.route('/')
# dont put html in your function even if you match it to the form it will mess up your link
def thisfunctionusedinresultspage(): 
    return render_template('homepage.html')
# this route connects the results form on the homepage.html to the server, however 
@app.route('/this_route_is_for_the_form_on_the_homepage', methods=['POST'])
def result(): 
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    elif len(request.form['comments']) < 1:
        flash("Comments cannot be empty!")
        return redirect('/')
    elif len(request.form['comments']) > 120:
        flash("Comments cannot be longer than 120 characters!")
        return redirect('/')
    name = request.form['name']
    dojo = request.form['dojo_location']
    language = request.form['favorite_language']
    comment = request.form['comments']
    return render_template('results.html', name=name,dojo=dojo,language=language,comment=comment)


app.run(debug=True) 


# kcodebelow

# from flask import Flask, render_template, redirect, request

# app = Flask(__name__)

# @app.route("/")

# def home():
#     option1 = 'Chicago'
#     option2 = 'New York'
#     option3 = 'Seattle'
#     option4 = 'JavaScript'
#     option5 = 'Python'
#     option6 = 'C#'
#     return render_template('homepage.html', option1 = option1, option2 = option2, option3 = option3, option4 = option4, option5 = option5, option6 = option6 )

# @app.route("/results", methods=['POST'])

# def results():
#     name = request.form['name']
#     location = request.form['location']
#     language = request.form['language']
#     text = request.form['text']
#     return render_template('results.html', name = name, location = location, language = language, text = text)

# app.run(debug=True)
