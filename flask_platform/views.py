from flask import render_template
from flask_platform import app
from systeminfo import main


@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'Martin'
    returnDict['title'] = 'Home'
    returnDict['sysinfo'] = main.main()
   
    return render_template("index.html", **returnDict)  



    
