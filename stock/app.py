from flask import Flask, render_template, request
import pickle
import numpy as np

model1 = pickle.load(open(r'C:\Users\USER\Desktop\stock\model\stock.pickle','rb'))  

app = Flask(__name__)  # initializing Flask app


@app.route("/",methods=['GET'])
def hello():
    return render_template('home.html')


@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST': 

        d1 = request.form['Date']
        d2 = request.form['Open']
        d3 = request.form['High']
        d4 = request.form['Low']
        d5 = request.form['Close']
       
        
        
    

        arr = np.array([[d1,d2,d3,d4,d5]])
        print([d1,d2,d3,d4,d5])
        pred1 = model1.predict(arr)
        print(pred1)

    return render_template('result.html',prediction_text1=pred1)
    
if __name__ == '__main__':
    app.run(debug=False)
    
#app.run(host="0.0.0.0")            # deploy
            # run on local system
