#Alifia Salwa Salsabila
#A11.2021.13245 / 7671960
#UDINUS / MSIB LearningX Batch 6

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/jobs',methods=['GET'])
def jobs():
    return render_template('detail.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)