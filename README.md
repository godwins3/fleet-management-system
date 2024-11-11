# Fleet Management System

A real-time vehicle tracking and fleet management system designed to help businesses efficiently track vehicles, monitor fuel consumption, and analyze performance metrics. The system provides live tracking of vehicles, distance traveled, fuel consumption, and performance analysis.

## Features

- **Real-Time Vehicle Tracking**: Track vehicles' location using GPS data.
- **Distance Traveled & Fuel Consumption**: Automatically calculate the distance traveled and fuel consumed by each vehicle.
- **Performance Analytics**: Analyze vehicle performance trends such as efficiency and fuel consumption over time.
- **Automated Notifications**: Send real-time notifications to customers when packages are dispatched or delivered.
- **Responsive UI**: A user-friendly interface built with HTML, CSS, and JavaScript.

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (using Chart.js for performance graphs)
- **Database**: (Your choice, e.g., PostgreSQL, MongoDB)
- **Mapping**: Leaflet.js (for real-time map tracking)
- **APIs**: Flask-Restful (for handling API requests)
- **CORS**: Flask-CORS (for cross-origin resource sharing)

## Setup Instructions

### Prerequisites

Ensure that you have the following installed:

- Python 3.x
- MongoDB
- Pip (for installing Python packages)
- Flask (`pip install flask`)
- Flask-CORS (`pip install flask-cors`)
- Leaflet.js (for map functionality)
- Chart.js (for performance charts)

### Installation Steps

1. **Clone the Repository:**

   Clone the project to your local machine.

   ```bash
   git clone https://github.com/your-username/fleet-management-system.git
   cd fleet-management-system
2. **Install dependencies**

    Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

    Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**

    After setting up the environment, start the Flask server:

    ```bash
    flask run
    ```

4. **Accessing the application**

    Open a web browser and go to http://localhost:5000 to see the application in action.

## Folder Structure

```bash
fleet-management-system/
│
├── app.py              # Main Flask application file
├── helpers/          # Folder for helpers
│   ├── calc_distance.py       # distance and location helpers
│   ├── fuel_estimation.py  # fuel estimation helpers
├── templates/          # Folder for HTML templates (Jinja2)
│   ├── base.html       # Base template with common layout
│   ├── dashboard.html  # Dashboard page template
│   ├── vehicle_tracking.html  # Vehicle tracking page template
│   ├── performance_analysis.html # Performance analysis page template
│   └── notifications.html    # Notification page template
│
├── static/             # Static files (CSS, JS, Images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── requirements.txt    # Python dependencies
├── .gitignore          # git ignore config file
└── README.md           # This file
```

## Acknowledgments

- Thanks to Leaflet.js for the mapping functionality.
- Thanks to Chart.js for the performance visualization.
- Flask and Flask-CORS for the backend and handling CORS.