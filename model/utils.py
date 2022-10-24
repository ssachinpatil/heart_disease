import json
import pickle
import numpy as np
try:
    import config
except:
    pass

class heart():
    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
        self.age=age
        self.sex=sex
        self.cp=cp
        self.trestbps=trestbps
        self.chol=chol
        self.fbs=fbs
        self.restecg=restecg
        self.thalach=thalach
        self.thalach=thalach
        self.exang=exang
        self.oldpeak=oldpeak
        self.slope=slope
        self.ca=ca
        self.thal=thal

    def load_model(self):
        try:
              

            with open (config.MODEL_FILE_PATH,"rb") as f:
                self.model=pickle.load(f)

            with open (config.JSON_FILE_PATH,"r") as m:
                self.json_data=json.load(m)  


        except:
            with open ("heart.pkl","rb") as f:
                self.model=pickle.load(f)
                
            with open ("json_data.json","r") as m:
                self.json_data=json.load(m)  


    def prediction(self):
        self.load_model()
        array=np.zeros(len(self.json_data['columns']))
        print("array",array)
        array[0]=self.age
        array[1]=self.json_data['sex'].get(self.sex)
        array[2]=self.cp
        array[3]=self.trestbps
        array[4]=self.chol
        array[5]=self.fbs
        array[6]=self.restecg
        array[7]=self.thalach
        array[8]=self.exang
        array[9]=self.oldpeak
        array[10]=self.slope
        array[11]=self.ca
        array[12]=self.thal

        print(array)
        prediction=self.model.predict([array])
        print(prediction)
        return prediction
    
if __name__=="__main__":
    age=67
    sex="male"
    cp=0
    trestbps=126
    chol=312
    fbs=0
    restecg=0
    thalach=188
    exang=1
    oldpeak=0
    slope=0
    ca=1
    thal=0
        
    pred=heart(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    pred.prediction()[0]
    
