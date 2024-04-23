import psycopg2
from psycopg2 import OperationalError
import time
import random
import datetime

# Function to create a database connection
def create_connection(host_name, user_name, password, db_name):
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=user_name,
            password=password,
            host=host_name,
            port="5432"
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to insert a new record into the measurements table for sensor_id=6
def insert_voltage(connection, voltage):
    cursor = connection.cursor()
    # Get the current time with millisecond accuracy and timezone offset
    current_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
    query = "INSERT INTO microgrid_back_measurementssix(sensor_id, voltage, time) VALUES (6, %s, %s);"
    cursor.execute(query, (voltage, current_time))
    connection.commit()
    cursor.close()

# Replace with your actual database credentials
connection = create_connection("localhost", "sensor2", "microgrid", "sensors")

import math
import time
import random
import datetime
import psycopg2
from psycopg2 import OperationalError

# Constants for the sine wave
AMPLITUDE = 50  # The peak value of the voltage
FREQUENCY = 50  # 50 cycles per second
PHASE = 0  # Phase shift, if any
NOISE_LEVEL = 1  # The maximum level of random noise

# Time variable to simulate continuous time
start_time = time.time()

# Modified function to simulate a sine wave with perturbations
def get_sine_wave_voltage(current_time):
    # Sine wave formula: V(t) = A * sin(2 * pi * f * t + phase)
    sine_wave = AMPLITUDE * math.sin(2 * math.pi * FREQUENCY * current_time + PHASE)
    # Add random noise to simulate perturbations
    noise = random.uniform(-NOISE_LEVEL, NOISE_LEVEL)
    return sine_wave + noise


# Use the modified function in your loop
try:
    while True:
        current_time = time.time() - start_time
        # Simulate voltage reading with sine wave and noise
        voltage = get_sine_wave_voltage(current_time)
        print(f"Voltage: {voltage:.2f} V")

        # Insert the voltage and current time into the database for sensor_id=6
        insert_voltage(connection, voltage)

        # Delay of 1 millisecond before the next loop iteration to achieve 1000Hz insertion rate
        # time.sleep(0.001)

except KeyboardInterrupt:
    print("Exiting...")
    if connection:
        connection.close()
        print("PostgreSQL connection is closed")
