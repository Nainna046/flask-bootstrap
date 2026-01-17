from flask import Flask, render_template

app = Flask(__name__)

cars = [
    {'id':1, 'brand' : 'toyota' , 'model' : 'Yaris Ativ' , 'year' : 2024 , 'price' : 560000},
    {'id':2, 'brand' : 'toyota' , 'model' : 'Yaris Cross' , 'year' : 2025 , 'price' : 790000},
    {'id':3, 'brand' : 'Nissan' , 'model' : 'Kicks' , 'year' : 2024 , 'price' : 850000}
    
]

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')
    

@app.route('/cars')
def show_cars():
    return render_template('cars/cars.html',
                           title='Show All Cars Page',
                           cars=cars)

@app.route('/cars/new')
def new_car():
    return render_template('cars/new_car.html',
                           title='New CAr Page')










print ("Hello World") 