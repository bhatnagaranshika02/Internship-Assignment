from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


class cars(db.Model):
   id = db.Column('car_id', db.Integer, primary_key = True)
   color = db.Column(db.String(100))
   registration_number = db.Column(db.String(50))
   slot_id = db.Column(db.Integer(200)) 
  

def __init__(self, color,registeration_number,slot_id):
   self.color = color
   self.registration_number = registration_number
   self.slot_id = slot_id

app = Flask(__name__)

@app.route('/register/')
def register():
	color = request.args.get('color',None)
	registration_number = request.args.get('registration_number',None)
	global slot
	curr_slot = db.session.execute('select count(id) as c from cars').scaler()
	if slot==curr_slot:
		return "No empty slot."
	else:
		carlist = cars.query().all()
		new_car = cars(color,registration_number,slot_id)
		for car in carlist:
		if car.id == None:
			db.session.add(new_car)
			db.session.commit()


@app.route('/leave/<int:car_id>')
def leave(car_id):

@app.route('/cars/<str:color>')
def car_filter(color):


@app.route('/get_slot<int:car_id>')
def get_slot(car_id):


@app.route('/slots/<str:color>')
def get_allslots(color):


@app.route('/change_slot/<int:number_slots>')
def change_slot(number_slots):




if name == '__main__':
	app.run()