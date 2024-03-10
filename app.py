from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cheese')
def cheese():
    return render_template('index1.html')

@app.route('/love/<chiz>')
def love(chiz):
    return render_template('index2.html', chiz=chiz)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port='5002')
