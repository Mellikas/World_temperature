**WORLD TEMPERATURE**

Website/Data analysis project created during the CodeAcademy course.

**DESCRIPTION**

Project was created to familiarize with:
- Data editing and analysis
- Django framework
- HTML templates
- SQLite

**HOW TO INSTALL AND RUN**

1. Create a new Django project in your IDE (e.g. PyCharm)
2. Download zipped project
3. Upload the unzipped files to the newly created Django project
4. In terminal run: `pip install -r requirements.txt`
5. In terminal run: `python manage.py makemigrations`
7. In terminal run: `python manage.py migrate`
8. In terminal run: `python manage.py createsuperuser` and creat admin user (while typing pasword it won't appear)
6. Download data [from here](https://www.kaggle.com/datasets/subhamjain/temperature-of-all-countries-19952020).
   1. name it "temp_data.csv" 
   2. put it in to project dir: "data_analysis/data_app/data"
   3. follow steps in **data_check_edit.py** and run it (dir: data_analysis/data_app/data/data_check_edit.py)
   4. follow steps in **data_import_edit_SQL.py** and run it (dir: data_analysis/data_app/data/data_import_edit_SQL.py)
9. In terminal run: `python manage.py runserver localhost:18080` (or similar `localhost: 18000` etc.)
10. Push on active server link in terminal.
11. Go to: 
    - http://localhost:18080
    - http://localhost:18080/admin