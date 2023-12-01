from flask import Flask, jsonify,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/calculate",methods=['post'])
def calc():
    data=request.get_json()
    dataval=list(data.values())
    c=[19.5,17,19.5,21.5,22,22.5,19.5,15]
    for i in range(len(dataval)):
        dataval[i]=float(dataval[i])
    print(dataval)
    num=sum(dataval[i]*c[i] for i in range(len(dataval)))
    print(num)
    denom=sum(c[i] for i in range(len(dataval)))
    print(denom)
    cgpa=num/denom
    return jsonify(cgpa)
    


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=3000) # run the application in debug mode on port 5