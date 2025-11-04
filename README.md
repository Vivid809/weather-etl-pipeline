# Weather ETL Pipeline ⛅

A small ETL that fetches **current weather** from the Open-Meteo API, transforms the response, loads it into **SQLite** (`weather.db`), and exports a consolidated **CSV** (`weather_data.csv`).

> **Status:** working demo — intentionally lightweight for portfolio use.

---

## What it does

- **Extract** current weather for **London** from Open-Meteo.
- **Transform** to a compact schema (`city`, `temperature`, `weathercode`, `time`).
- **Load** into `weather.db` (`weather` table), appending each run.
- **Export** all rows to `weather_data.csv`.

---

## Tech

- Python, `requests`, `pandas`, `sqlite3`
- Open-Meteo API (no key required)

---

## Quick start

```bash
git clone https://github.com/Vivid809/weather-etl-pipeline.git
cd weather-etl-pipeline
pip install pandas requests
python main.py
```

## Outputs:

weather.db — SQLite database with table weather

weather_data.csv — all recorded snapshots

##Project Structure

```bash
weather-etl-pipeline/
├─ main.py
├─ weather.db           # created on run (can be git-ignored)
├─ weather_data.csv     # created on run (can be git-ignored)
└─ README.md
```

## Notes & improvements

The table includes a windspeed column; you can add it to the insert if needed.

Re-running the script appends a new row with the latest snapshot — useful for time series tracking.

To avoid committing data files, add this to .gitignore:

weather.db
weather_data.csv


## License

MIT

## 📫 Contact

- **Email:** [mutahhar.you@gmail.com](mailto:mutahhar.you@gmail.com)  
- **LinkedIn:** [Mutahher Naseer](https://www.linkedin.com/in/mutahher-naseer-30778b220)


