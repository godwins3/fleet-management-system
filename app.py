from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from bson.objectid import ObjectId
from helpers.calc_distance import calculate_distance
from helpers.auth import auth # import auth blueprint

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
app.config['SECRET_KEY'] = 'your_secret_key'

client = MongoClient('mongodb://localhost:27017/')
db = client.fleet_management
vehicles_collection = db.vehicles

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # Redirect to login page if not logged in

# Initialize Flask-Bcrypt
bcrypt = Bcrypt(app)

# Register the auth blueprint
app.register_blueprint(auth, url_prefix='/auth')

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # Fetch user from MongoDB based on user_id
    return db.users.find_one({"_id": user_id})

@app.route('/')
def dashboard():
    vehicles = list(vehicles_collection.find())
    return render_template('dashboard.html', vehicles=vehicles)

@app.route('/vehicle_tracking')
def vehicle_tracking():
    return render_template('vehicle_tracking.html')

@app.route('/track', methods=['POST'])
def track_vehicle():
    data = request.json
    vehicle_id = data.get('vehicleId')
    coordinates = data.get('coordinates')
    fuel_consumed = data.get('fuelConsumed')

    vehicle = vehicles_collection.find_one({'_id': ObjectId(vehicle_id)})
    if vehicle:
        last_coordinates = vehicle['coordinates'][-1] if vehicle['coordinates'] else None
        distance = calculate_distance(last_coordinates, coordinates) if last_coordinates else 0
        vehicles_collection.update_one(
            {'_id': ObjectId(vehicle_id)},
            {
                '$push': {'coordinates': coordinates},
                '$inc': {'fuelConsumed': fuel_consumed, 'distanceTravelled': distance}
            }
        )
        vehicle = vehicles_collection.find_one({'_id': ObjectId(vehicle_id)})
        socketio.emit('vehicleUpdate', vehicle)
        return jsonify(vehicle), 200
    else:
        return jsonify({'error': 'Vehicle not found'}), 404

@app.route('/performance')
def performance():
    return render_template('performance.html')

@app.route('/api/get-performance')
def get_performance():
    # Dummy data for performance metrics
    vehicles = [
        {'id': 1, 'model': 'Toyota Prius', 'distance': 1200, 'fuel': 80, 'efficiency': 15},
        {'id': 2, 'model': 'Ford Explorer', 'distance': 800, 'fuel': 100, 'efficiency': 8},
        {'id': 3, 'model': 'Honda Civic', 'distance': 1500, 'fuel': 90, 'efficiency': 16.7},
        {'id': 4, 'model': 'Nissan Leaf', 'distance': 1100, 'fuel': 70, 'efficiency': 15.7}
    ]

    total_distance = sum(vehicle['distance'] for vehicle in vehicles)
    total_fuel = sum(vehicle['fuel'] for vehicle in vehicles)

    # Dummy data for performance trends
    dates = ['2024-11-01', '2024-11-02', '2024-11-03', '2024-11-04', '2024-11-05']
    distances = [300, 400, 500, 200, 300]
    fuels = [20, 25, 30, 15, 20]

    data = {
        'vehicles': vehicles,
        'total_distance': total_distance,
        'total_fuel': total_fuel,
        'dates': dates,
        'distances': distances,
        'fuels': fuels
    }

    return jsonify(data)


if __name__ == '__main__':
    socketio.run(app, debug=True)   