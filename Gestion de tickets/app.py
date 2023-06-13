from flask import Flask, jsonify, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('padre.html')


@app.route('/soli-soft-emergencias', methods = ['GET', 'POST'])
def emergencias_soft():
    return render_template('emergencias-soft.html')


@app.route('/soli-soft-ftth', methods = ['GET', 'POST'])
def ftth_soft():
    return render_template('ftth-soft.html')


@app.route('/soli-soft-portabilidad', methods = ['GET', 'POST'])
def portabilidad_soft():
    return render_template('porta-soft.html')


@app.route('/soli-hard-emergencias', methods = ['GET', 'POST'])
def emergencias_hard():
    return render_template('emergencias-hard.html')


@app.route('/soli-hard-ftth', methods = ['GET', 'POST'])
def ftth_hard():
    return render_template('ftth-hard.html')


@app.route('/soli-hard-portabilidad', methods = ['GET'])
def portabilidad_hard():
    return render_template('porta-hard.html')


if __name__ == '__main__':
    app.run(debug= True)