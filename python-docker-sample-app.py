from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route('/test',methods = ['POST'])
def test():
    content = request.json
    if content != None:
        return "Success"
    else:
        return "Invalid content"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
