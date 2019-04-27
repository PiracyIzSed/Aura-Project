from flask import Flask,render_template,flash, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/var/www/AuraSite/Uploads'  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Function For Checking Utilising the same page for upload of analysis and prediction files
def check_type_upload(type,name):
    if type == "analysis":
        return redirect(url_for('analysis_report',name=name))
    elif type == "predict":
        return redirect(url_for('prediction_report',name=name))
    else:
        return "Not a valid request"

#Home Page
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

#Upload Page For Analysis & Predictions
@app.route('/predict_aura/')
@app.route('/analyse_aura/')
def upload():
    return render_template("upload_aura.html")

#Upload Page for Comparison
@app.route('/compare_aura/')
def compare():
    return render_template("upload_aura_compare.html")


#Report/Result Pages

#Analysis Result Page
@app.route('/analysis_report/<name>')
def analysis_report(name):
    return "Analysis Report for "+name+" has been generated"

#Comparison Result Page
@app.route('/comparison_report/<id1>/<id2>')
def comparison_report(id1,id2):
    return "Comparison Report for "+id1+" & "+id2+" has been generated"

#Prediction Result Page
@app.route('/prediction_report/<name>')
def prediction_report(name):
    return "Predicition Report for "+name+" has been generated"

#Upload Utility For Files
@app.route('/uploader/<type>', methods = ['GET', 'POST'])
def upload_file(type):
   if request.method == 'POST':
       if type == 'predict' or type == 'analysis':
          file = request.files['uploadedFile']
          file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
          return check_type_upload(type,file.filename)
       elif type == 'compare' :
          files = request.files.getlist('uploadedFile')
          for file in files :
              file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
          return redirect(url_for('comparison_report',id1=files[0].filename,id2=files[1].filename))
   else:
       return 'file upload unsuccessfull'

if __name__ == "__main__":
    app.run()
