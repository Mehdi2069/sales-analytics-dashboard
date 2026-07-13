from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data" / "sales_data.csv"
DB_PATH = BASE_DIR / "authentication" / "users.db"
