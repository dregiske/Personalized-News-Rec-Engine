import os
from datetime import timedelta
from dotenv import load_dotenv

# 1. Load .env
load_dotenv()  

# 2. Auth / JWT settings
SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 3. Database URL (for SQLAlchemy in app/database.py)
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not set in .env")
