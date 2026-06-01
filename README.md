Social Hub

A minimalist social network web application built with Django.
This project allows users to connect, share posts, interact, and manage their profiles in a simple social media environment.

 Features
User authentication (Register / Login / Logout)
Create, edit, and delete posts
Like and comment on posts
Follow / unfollow users
Personalized feed based on followed users
User profile pages with bio and profile picture
Notifications for interactions (likes, comments, follows)
 Technologies Used
Python
Django
HTML5
CSS3
JavaScript
SQLite
 Project Structure
my_social_network_project/
│
├── users/               # User authentication and profiles
├── posts/               # Posts management
├── connections/         # Follow system
├── notifications/       # Notifications system
├── templates/           # HTML templates
├── static/              # CSS / JS files
├── media/               # Uploaded images
└── manage.py
 Installation & Setup
Clone the repository:
git clone https://github.com/sara-azouad/social_hub.git
Navigate to the project folder:
cd social_hub
Create a virtual environment:
python -m venv venv
Activate the virtual environment:
venv\Scripts\activate   # Windows
Install dependencies:
pip install -r requirements.txt
Run migrations:
python manage.py migrate
Start the server:
python manage.py runserver


Author
Sara Azouad

This is a learning project built for academic purposes.
Future improvements may include real-time chat, advanced notifications, and UI enhancements.
