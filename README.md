# CivicEye - Urban Issue Tracker & Severity Analytics

CivicEye is a professional web application built with **Django** designed to empower citizens to report urban issues (road damage, waste management, etc.) directly to authorities. It features a real-time data analytics dashboard and an interactive issue map.

## 🚀 Key Features
- **User Authentication:** Secure signup/login system for citizens.
- **Incident Reporting:** Users can upload images and provide details of urban issues.
- **Analytics Dashboard:** Real-time visualization of issue categories and severity levels using **Chart.js**.
- **Interactive Map:** Visual tracking of reported issues on a map using **Leaflet.js**.
- **Search & Filter:** Advanced filtering by category and search by title.
- **My Reports:** A dedicated dashboard for users to manage and track their reported incidents.
- **Admin Actions:** Staff members can update incident status (Pending/In Progress/Solved) directly from the front end.

## 🛠️ Tech Stack
- **Backend:** Python (Django Framework)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (Development)
- **Data Visualization:** Chart.js
- **Map Integration:** Leaflet.js with CartoDB Voyager tiles
- **Image Processing:** Pillow

## 📂 Installation & Setup
1. Clone the repository: `git clone https://github.com/AzizTanvir/CivicEye-Urban-Issue-Tracker.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate venv: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Start server: `python manage.py runserver`
