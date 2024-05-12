# Django Project with PostgreSQL (EthanAI)

This repository contains a Django project configured to utilize PostgreSQL as its database backend.

## Requirements

Before starting the project, ensure that the following prerequisites are met:

- Python version 3.x or higher
- PostgreSQL database
- pip (Python package manager)

## Setup Instructions

Follow these steps to set up and run the project:

1. Clone the repository to your local machine:

    ```bash
    git clone
    ```

2. Navigate to the project directory:

    ```bash
    cd ethanai
    ```

3. Install the project dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a PostgreSQL database for the project. You can do this using the command line or a GUI tool such as pgAdmin.

5. Update the database configuration in the `settings.py` file located in the `projectname` directory:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

    Replace `'your_database_name'`, `'your_database_user'`, and `'your_database_password'` with your actual PostgreSQL database credentials.

6. Run database migrations to create the required tables:

    ```bash
    python manage.py migrate
    ```

## Running the Project

After completing the setup, you can start the Django development server:

```bash
python manage.py runserver
```
Access the project at: ``` http://127.0.0.1:8000/financial ```