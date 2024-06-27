# Django_Task
# very Simple Bookstore


This is a Bookstore application built with Django and Django REST Framework.

## Setup Instructions

### Prerequisites

- Python 3.8+
- Docker (for containerization)
- Mysql (or any preferred database)

### Installation

1. **Clone the repository:**

    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    - Ensure PostgreSQL is running and create a database for the project.

    - Update the `DATABASES` setting in `settings.py`:

        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'your_db_name',
                'USER': 'your_db_user',
                'PASSWORD': 'your_db_password',
                'HOST': 'localhost',
                'PORT': '',
            }
        }
        ```

    - Run migrations:

        ```sh
        python manage.py migrate
        ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```



###  Endpoints book app

- **Book Operations:**
    - List Books : `GET /`
    - Detail View: `GET /book/<int:pk>/`
    - Create Book: `POST /book/new/`
    - Update Book: `PUT /book/<int:pk>/edit/`
    -  Delete Book: `DELETE /book/<int:pk>/delete/`
      
- **Multiplication Table:**
- Dynamic Multiplication Table: `GET /page/?number=<number>` default is `GET /page/`

### API Endpointsbook app
 - **books:**
 - Books Endpoint: `GET /api/books/`, `POST /api/books/`  Allows listing and creating books.
 - Book Detail Endpoint:` GET /api/books/<id>/`, `PUT /api/books/<id>/`, `DELETE /api/books/<id>/`
 - Allows retrieving, updating, and deleting individual books.


      

