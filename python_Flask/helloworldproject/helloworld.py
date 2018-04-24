from flask import Flask, render_template
app = Flask(__name__)
def main():
  return 'main url'
# need / first route to write stuff
@app.route('/')
def openpage():
    return 'openpage'     

@app.route('/innertemplatehelloworld')
def innertemplatehelloworld():
  return render_template('innertemplatehelloworld.html')


app.run(debug=True)   