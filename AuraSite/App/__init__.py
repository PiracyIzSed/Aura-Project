from flask import Flask,render_template,flash, request, redirect, url_for
import os,Scripts as sc

app = Flask(__name__)
UPLOAD_FOLDER = '/home/jatin/Aura-Project/AuraSite/Uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Function For Utilising the same page for upload of analysis and prediction files
def check_type_upload(type,name):
    if type == "analysis":
        return redirect(url_for('analysis_report',name=name))
    elif type == "predict":
        return redirect(url_for('prediction_report',name=name))
    else:
        return "Not a valid request"


# Flow of website : Homepage --> Upload Page (either analysis/prediction or comparison) --> Result/Report Pages


#Home Page
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


#Upload Pages
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
    return render_template("analysis_report.html",user=sc.analysis.analyse(name))

#Comparison Result Page
@app.route('/comparison_report/<id1>/<id2>')
def comparison_report(id1,id2):
    return render_template("comparison_report.html",result=sc.comparison.compare(id1,id2))

#Prediction Result Page
@app.route('/prediction_report/<name>')
def prediction_report(name):
    return render_template("prediction_report.html",prediction=sc.prediction.predict(name))

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


#Execution of app
if __name__ == "__main__":
    app.run(debug=True)
