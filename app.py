from flask import Flask
from flask import render_template, request
import app


app = Flask(__name__)


def sort(list):
    l = len(list)
    if l <= 1:
        return list
    else:
        p = list.pop()
    large = []
    small = []
    for i in list:
        if i > p:
            large.append(i)
        else:
            small.append(i)
    return sort(small) + [p] + sort(large)


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/input', methods=['GET','POST']) 
def input():
    listLength = request.form["length"]
    listLength = int(listLength)
    
    return render_template('inputs.html', len=listLength)  


@app.route('/sort', methods=['GET','POST']) 
def sorte():
    valueS = request.form.getlist('values')
    valueS = [(float(i)) for i in valueS]
    res = sort(valueS)

    return render_template('returnValue.html', sorts=len(valueS)+1, sorted=res)   


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    

