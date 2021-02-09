from flask import Flask, jsonify, request
from random import random
import urllib




# insert flask annotation here
app = Flask(__name__)


@app.route('/api/v1/sum')
def _sum():
    # A: first number to sum
    # B: second number to sum
    a = request.args.get('a', default=0, type=float)
    b = request.args.get('b', default=0, type=float)
    sum = a+b
    
    URL = "sum-s"
    #r = requests.get(url = URL, PARAMS = sum)
    #return jsonify({'result': str(a + b)})

    contents = urllib.request.urlopen(URL:5000?somma=sum) 

@app.route('/api/v1/rand')
def _randomNumber():
    return jsonify({'result': str(random())})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
