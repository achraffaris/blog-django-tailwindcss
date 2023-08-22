# blog-django-tailwindcss

# Project Installation and Setup Guide

This guide will walk you through the process of installing the required dependencies and running the project on your local machine.

## Prerequisites

Before you begin, make sure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.10.x recommended)
- [pip](https://pip.pypa.io/en/stable/installing/) (Python package manager)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (version control system)

## Installation

1. Clone the repository:
    ```
        git clone https://github.com/achraffaris/blog-django-tailwindcss
    ```
2. Change directory to blog-django-tailwindcss and create a .env file:
    ```
        cd blog-django-tailwindcss && touch .env
    ```
3. Paste those environement variables needed for the project (PS: You must set Cloudinary credentials, It's FREE):
    """

        SECRET_KEY="generate_a_random_key" # should be private if production

        DEBUG=True
        ALLOWED_HOSTS="*" # Comma separated values, Set that if DEBUG is False
        
        USE_S3=False # Set that to False if you want to use Django's default static files storage
        DATABASE='SQLITE' # Set that to POSTGRES if you want to use POSTGRES database
        
        # Cloudflare R2 credentials -- Ignore it if you will use default static files storage
        
        AWS_STORAGE_BUCKET_NAME=''
        AWS_S3_ENDPOINT_URL=''
        AWS_S3_ACCESS_KEY_ID=''
        AWS_S3_SECRET_ACCESS_KEY=''
        AWS_S3_CUSTOM_DOMAIN=''
        
        # Postgres credentials -- Ignore it if you will use SQLITE3
        
        DB_NAME=''
        DB_USER=''
        DB_PASSWORD=''
        DB_HOST=''
        DB_PORT='5432'
        
        # Cloudinary credentials -- Mandatory
        
        CLOUDINARY_CLOUD_NAME=''
        CLOUDINARY_API_KEY=''
        CLOUDINARY_API_SECRET=''
4. Create a virtual environement and activate it:
    ```
        virtualenv env && source env/bin/activate
    ```
5. Install dependencies of this project
    ```
        pip install -r requirements.txt
    ```
6. Populate changes to DATABASE:
    ```
        cd miniproject && python manage.py migrate
    ```
7. Runserver
    ```
        python manage.py runserver
    ```
