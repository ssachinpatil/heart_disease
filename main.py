from flask import Flask,render_template,request,jsonify
from model.utils import heart


app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def get_prediction():

    a = request.form
    print(a)
    age=eval(a["age"])
    sex=a["sex"]
    cp=eval(a["cp"])
    trestbps=eval(a["trestbps"])
    chol=eval(a["chol"])
    fbs=eval(a["fbs"])
    restecg=eval(a["restecg"])
    thalach=eval(a["thalach"])
    thalach=eval(a["thalach"])
    exang=eval(a["exang"])
    oldpeak=eval(a["oldpeak"])
    slope=eval(a["slope"])
    ca=eval(a["ca"])
    thal=eval(a["thal"])
    x=heart(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    result=x.prediction()
    return jsonify({'result':f"the prediction is{result}"})
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8081)
    