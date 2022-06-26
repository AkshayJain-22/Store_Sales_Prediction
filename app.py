from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return("Confirming for the last time")

if __name__=="main":
    app.run(debug=True)