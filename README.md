
#             Blog Application (Content_Review_Project)








## Getting Started


1-First of all clone this repo
--
--> git clone https://github.com/AyushTmg/Content_Review_Project.git


2-Setup a virtual enviroment
--
-->python -m venv venv

3-Install all dependencies from the requirements.txt in a virtual enviroment
--
--> pip install -r requirements.txt


4-Update the DATABASES settings in settings.py  in this case postgres is used 
--
DATABASES = {\
   'default': {\
        'ENGINE': 'django.db.backends.postgresql',\
        'NAME':os.environ.get("DB_NAME"),\
        'USER': 'your_database_user',\
        'PASSWORD': os.environ.get("DB_PASS"),\
        'HOST': 'localhost',\
        'PORT': '5432',\
}\
}

5-Add .env file and add these field
--

EMAIL_USER="Your email"
EMAIL="Your email"
EMAIL_PASSWORD="email password"
DB_NAME='database name'
DB_PASS='database password'

6-Migrate the changes to your database
--
-->python manage.py migrate\
-->python manage.py runserver

7-Run Application
--
-->python manage.py runserver

#                How it Works


The Blog Application allows users to:

- Post articles with images.\

- Leave reviews on articles.\

- Add replies to reviews.\

- Delete their posts, reviews, and replies (only with user authentication).\

- Feel free to explore the full functionality of the application and enjoy a seamless blogging experience!
