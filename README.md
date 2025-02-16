# Weather ETL Project

## What It Does
The Weather ETL Project extracts, transforms, and loads weather data from various sources into a centralized database. It aims to provide a comprehensive and accurate dataset for weather analysis and forecasting.

## Technologies Used
- **Python**: The primary programming language used for the ETL process.
- **APIs**: To retrieve weather data from multiple sources.
- **SQLite**: A lightweight database for storing the transformed data.
- **Pandas**: For data manipulation and analysis.
- **YAML**: For configuration settings.

## About
This project was created as a personal practice project to enhance skills in data engineering and ETL processes.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/weather_etl_project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd weather_etl_project
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Configure the data sources and database settings in the `config.yaml` file.
2. Run the ETL process:
    ```bash
    python etl.py
    ```

## Project Structure
- `etl.py`: Main script to run the ETL process.
- `config.yaml`: Configuration file for data sources and database settings.
- `extract/`: Directory containing data extraction scripts.
- `transform/`: Directory containing data transformation scripts.
- `load/`: Directory containing data loading scripts.
- `tests/`: Directory containing test cases.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please contact [your email address].

#Python #DataEngineer #ETL
