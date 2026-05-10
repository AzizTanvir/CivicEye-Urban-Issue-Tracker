# CivicEye - Smart Urban Issue Tracker & Analytics

CivicEye is a full-stack **Django** application designed for smart city governance. It allows citizens to report urban issues with precise GPS data, visualize problem distributions through dynamic charts, and track incidents on an interactive satellite map.

## 🚀 Advanced Features
- **High-Accuracy GPS Reporting:** Automatically detects user location using Browser Geolocation API with high-precision mode.
- **Interactive Satellite Map:** Built with **Leaflet.js** and **Esri Satellite Imagery** for building-level accuracy.
- **Click-to-Pick & Search:** Users can search for locations or manually adjust pins by clicking on the map.
- **Real-time Data Analytics:** Dynamic **Chart.js** integration to visualize issue categories and severity levels.
- **User Ownership & Security:** Robust signup/login system where users can manage their own reports.
- **Administrative Status Tracking:** Staff can update issue progress (Pending/In Progress/Solved) directly from the front-end.
- **Production Ready:** Configured with **WhiteNoise** for static file management during deployment.

## 🛠️ Tech Stack
- **Backend:** Python (Django 5.x)
- **Frontend:** HTML5, CSS3 (Custom Gradient Theme), Bootstrap 5
- **Maps:** Leaflet.js, Esri World Imagery, Leaflet Geocoder
- **Charts:** Chart.js
- **Middleware:** WhiteNoise (Static serving)
- **Database:** SQLite (Development)

## 📂 Installation & Local Setup
1. Clone: `git clone https://github.com/AzizTanvir/CivicEye-Urban-Issue-Tracker.git`
2. Environment: `python -m venv venv` and `venv\Scripts\activate`
3. Install: `pip install -r requirements.txt`
4. Migrate: `python manage.py migrate`
5. Run: `python manage.py runserver`

---
*Developed by Aziz Tanvir as a showcase of Geospatial Web Development and Data Analytics.*