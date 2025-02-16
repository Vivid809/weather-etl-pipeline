import requests # makes HTTP requests to API
import sqlite3 # database SQLite
import pandas as pd # data manipulation


# Function to get data from API
def extract_weather_data():
    # FETCHES weather data from open meteo API
    # and returns the data as a JSON object

    # API endpoint for open meteo API
    URL = "https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&&current_weather=true"
    
    #GET request
    response = requests.get(URL)

    #check if request was successful
    if response.status_code == 200:
        data = response.json()  #parson the JSON data
        return data
    else:
        print("Failed to fetch data from API")
        return None
    
#Transform data

def transform_weather_data(data):
    #transform raw JSON data into structured data
    #return dictionary with selected field

    if not data:
        return None
    
    #extract the current weather data
    current_weather = data["current_weather"]
    transformed_data = {
        "city": "London",
        "temperature": current_weather["temperature"],
        "weathercode": current_weather["weathercode"],
        "time": current_weather["time"]
    }
    return transformed_data

# Load data into SQLite database

#create db and store weather data in it

def create_database():
    #connect to the database
    connect = sqlite3.connect("weather.db")
    cursor = connect.cursor() #cursor object to execute SQL queries

    #create table to store weather data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather(
                   city TEXT,
                   temperature REAL,
                   windspeed REAL,
                   weathercode INTEGER,
                   time TEXT)
    """)
    connect.commit() #commit the changes
    connect.close() #close the connection


# Function to load data into SQLite database
def load_data_into_db(data):
    # insert the transformed data into the SQLite database

    #connect to the database
    connect = sqlite3.connect("weather.db") 
    cursor = connect.cursor()

    #insert the data into the table
    cursor.execute("""
        INSERT INTO weather(city, temperature, weathercode, time)
                   VALUES(?, ?, ?, ?) 
                   """, (data["city"], data["temperature"], data["weathercode"], data["time"])) #placeholders and data to be inserted
                   
    connect.commit()
    connect.close()

def run_etl_pipeline():
    # Run the ETL pipeline
    #extracted data from api, transformed the data, load the data into the db

    #Extract data
    print("Extracting weather data...")
    raw_data = extract_weather_data() #fetch data from API

    #Transform
    print("Transforming weather data...")
    transformed_data = transform_weather_data(raw_data) #transform the data

    #Load data
    if transformed_data: #check if data is not empty
        print("Loading data into database...")
        load_data_into_db(transformed_data) #load the data into the database
        print("Data loaded successfully!")
    else:
        print("Failed to load data into database!")


#Export data to CSV

def export_data_to_csv():
    #export the data from the database to a CSV file
    #connect to the database
    connect = sqlite3.connect("weather.db")
    
    #read data into a pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM weather", connect)

    #Save the data to a CSV file
    df.to_csv("weather_data.csv", index=False) #index=False to avoid saving the index column
    print("Data exported to weather_data.csv")

    connect.close()

#Execute the main function

if __name__ == "__main__": #check if the script is being run directly
    # create db
    create_database()

    #run the etl pipeline
    run_etl_pipeline()

    #export data to CSV
    export_data_to_csv()
   
    

