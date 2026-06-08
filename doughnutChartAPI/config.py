import os
from dotenv import load_dotenv
load_dotenv()
CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
OUTPUT_FOLDER="outputs"
APP_NAME="DOUGHNUT CHART API"
MODEL = 'gemini-3.5-flash'
RADIUS = 0.5
DEFAULT_COLOR = 'white'
CHART_PREFIX = "DoughnutChart"