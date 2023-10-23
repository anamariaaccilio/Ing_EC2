from flask import Flask,request,render_template
from Metodos_distancias import DistanceCalculatorFactory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/index.html')
def prueba():
    return render_template('index.html')

@app.route('/distance',methods=['POST'])
def calcular_distancia():
    metodo=request.form['metodo']
    ciudad1=request.form['city1']
    ciudad2=request.form['city2']
    pais1=request.form['country1']
    pais2=request.form['country2']


    distance=DistanceCalculatorFactory.create_distance_calculator(metodo,ciudad1,pais1,ciudad2,pais2)

    return render_template('index.html',distance=distance,city1=ciudad1,city2=ciudad2,country1=pais1,country2=pais2,method=metodo)

if __name__ == '__main__':
    app.run(debug=True)


