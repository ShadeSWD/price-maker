# Price Maker App

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
	![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

## Description

Price Maker is a web application designed for calculating resulting price of an item.

## Installation

Follow these steps:

1. **Clone repo**:  

   ```bash
   git clone https://github.com/ShadeSWD/price-maker.git
2. **Install dependencies::**

   ```bash
   cd price-maker
   poetry init

3. **Setup environment:**
    use template in .env.sample
    
4. **Perform migrations:**

   ```bash
   python manage.py migrate
5. **Run app:**

   ```bash
   python manage.py runserver
6. **Open app:** 
    The app is ready to process requests
7. **Create superuser:**
    ```bash
       python manage.py createsuperuser
8. **Create vendor:** Now, when you created a superuser, you can log in and create vendors at <your_host>/users/

## Docs:
    
Docs are available at:
- <your_host>/swagger/
- <your_host>/redoc/
