# Personal Portfolio Website

This project is a personal portfolio website developed using Django. It contains personal information, projects, technology stacks, contact inquiries, testimonials, and an admin dashboard for managing portfolio content.

## Technologies Used

* Python
* Django
* SQLite
* HTML
* CSS
* python-dotenv
* Git and GitHub

## Features

### Public Features

* Home page
* About page
* Projects page
* Project details
* Contact form
* Testimony form
* Testimony list and details

### Admin Features

* Admin-only sign in
* Admin dashboard
* Project management
* Tech stack management
* Project editing
* Project and tech stack tables
* Sign out

Only superusers can access the admin dashboard and management pages.

## How to Clone the Project

Clone the repository:

```bash
git clone https://github.com/Lance0812/Lance-Portfolio.git
cd Lance-Portfolio
```

## Create a Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

For macOS or Linux:

```bash
source venv/bin/activate
```

## Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root directory.

Add:

```text
SECRET_KEY=your-secret-key-here
DEBUG=True
```

Do not share or commit the real `SECRET_KEY`.

The `.env` file is excluded from Git using `.gitignore`.

## Database Setup

Run the existing migrations:

```bash
python manage.py migrate
```

Create a superuser for the admin dashboard:

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create the administrator account.

## Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Open the website in a browser:

```text
http://127.0.0.1:8000/
```

The admin dashboard can be accessed through the sign-in page.

## Project Structure

```text
Lance-Portfolio/
│
├── manage.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── website/
    ├── migrations/
    ├── static/
    ├── templates/
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    └── views.py
```

## Git Workflow

The project uses Git and GitHub for version control.

Development work is done on a separate branch instead of directly on the main or master branch.

Changes are committed using descriptive commit messages. Completed work is submitted through a Pull Request before being merged into the development branch.

## Deployment

The project is deployed using PythonAnywhere.

The deployed website is available at:

```text
https://lancereyes08.pythonanywhere.com/
```

The deployed version uses a separate production environment and database.

## Important Notes

* Do not commit `.env`.
* Do not commit `db.sqlite3`.
* Do not commit the virtual environment.
* Install dependencies using `requirements.txt`.
* Run migrations after cloning the project.
* A superuser is required to access the admin dashboard.
* Regular users cannot access the admin dashboard.
