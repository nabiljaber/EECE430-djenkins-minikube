## 🛠️ How to Run
```bash
# 1. Clone the repository
git clone https://github.com/nabiljaber/EECE430-Lab4.git
cd EECE430-Lab4

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

# 3. Install dependencies
pip install django

# 4. Run migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver

# 6. Open in browser
http://127.0.0.1:8000/
