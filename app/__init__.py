from flask import Flask

# Inisialisasi objek Flask dan tentukan lokasi folder templates
app = Flask(__name__, template_folder='templates')

# Import modul yang dibutuhkan oleh aplikasi
from app import views, models