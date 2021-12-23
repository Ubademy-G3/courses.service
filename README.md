# Courses Microservice

[![CI](https://github.com/Ubademy-G3/courses.service/actions/workflows/default.yml/badge.svg)](https://github.com/Ubademy-G3/courses.service/actions/workflows/default.yml)
[![codecov](https://codecov.io/gh/Ubademy-G3/courses.service/branch/main/graph/badge.svg?token=P5PT97QTE2)](https://codecov.io/gh/Ubademy-G3/courses.service)

Service dedicated to the management of courses: creation, edition, removal, and everything related to online courses.

# File Structure:
```tree
├── application
│   ├── controllers
│   │   ├── course_category_controller.py
│   │   ├── course_certificate_controller.py
│   │   ├── course_controller.py
│   │   ├── course_media_controller.py
│   │   ├── course_module_controller.py
│   │   ├── course_rating_controller.py
│   │   ├── course_user_controller.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── serializers
│   │   ├── course_category_serializer.py
│   │   ├── course_certificate_serializer.py
│   │   ├── course_media_serializer.py
│   │   ├── course_module_serializer.py
│   │   ├── course_rating_serializer.py
│   │   ├── course_serializer.py
│   │   ├── course_user_serializer.py
│   │   └── __init__.py
│   ├── services
│   │   ├── auth.py
│   │   ├── certificate_generator
│   │   │   ├── certificate_generator.py
│   │   │   ├── CoreSansC-35Light.ttf
│   │   │   ├── __init__.py
│   │   │   ├── output
│   │   │   ├── template-certificate.png
│   │   │   └── ubademy-mobile-ae5a598939c9.json
│   │   └── __init__.py
│   └── use_cases
│       ├── course
│       │   ├── create.py
│       │   ├── delete.py
│       │   ├── get.py
│       │   └── update.py
│       ├── course_category
│       │   ├── create.py
│       │   ├── delete.py
│       │   └── get.py
│       ├── course_certificate
│       │   ├── create.py
│       │   └── get.py
│       ├── course_media
│       │   ├── create.py
│       │   ├── delete.py
│       │   └── get.py
│       ├── course_module
│       │   ├── create.py
│       │   ├── delete.py
│       │   ├── get.py
│       │   └── update.py
│       ├── course_rating
│       │   ├── create.py
│       │   ├── delete.py
│       │   └── get.py
│       ├── course_user
│       │   ├── create.py
│       │   ├── delete.py
│       │   ├── get.py
│       │   └── update.py
│       └── __init__.py
├── deploy
│   └── heroku-entrypoint.sh
├── docker-compose.yml
├── Dockerfile
├── domain
│   ├── course_category_model.py
│   ├── course_certificate_model.py
│   ├── course_media_model.py
│   ├── course_model.py
│   ├── course_module_model.py
│   ├── course_rating_model.py
│   ├── course_user_model.py
│   └── __init__.py
├── exceptions
│   ├── auth_error.py
│   ├── http_error.py
│   ├── __init__.py
│   └── ubademy_error.py
├── heroku.yml
├── infrastructure
│   ├── db
│   │   ├── course_category_schema.py
│   │   ├── course_certificate_schema.py
│   │   ├── course_media_schema.py
│   │   ├── course_module_schema.py
│   │   ├── course_rating_schema.py
│   │   ├── course_schema.py
│   │   ├── course_user_schema.py
│   │   ├── database.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── database.cpython-38.pyc
│   ├── __init__.py
│   └── routes
│       ├── course_category_router.py
│       ├── course_certificate_router.py
│       ├── course_media_router.py
│       ├── course_module_router.py
│       ├── course_rating_router.py
│       ├── course_router.py
│       ├── course_user_router.py
│       ├── __init__.py
│       └── user_courses_router.py
├── LICENSE
├── logging.ini
├── main.py
├── monitoring
│   └── datadog.yml
├── persistence
│   ├── __init__.py
│   └── repositories
│       ├── course_category_repository_postgres.py
│       ├── course_certificate_repository_postgres.py
│       ├── course_media_repository_postgres.py
│       ├── course_module_repository_postgres.py
│       ├── course_rating_repository_postgres.py
│       ├── course_repository_postgres.py
│       ├── course_user_repository_postgres.py
│       └── __init__.py
├── README.md
├── requirements.txt
└── tests
    ├── conftest.py
    ├── courses
    │   ├── test_course_category.py
    │   ├── test_course_media.py
    │   ├── test_course_modules.py
    │   ├── test_courses.py
    │   └── test_course_users.py
    └── __init__.py
```

# Tech Stack

* Python 3.x
* FastAPI (as web framework to building the API with Python)
* SQLAlchemy (as PostgreSQL Toolkit for Python and an ORM)
* PostgreSQL (object-relational database)


# Local Environment 

## Requirements 

* Docker
* Docker-compose

## Environment variables

To run this application you need to define the following environment variable:

```
API_KEY = YOUR_COURSES_SERVICE_APIKEY
```

## Build and Deploy Services

```docker-compose up -d --build```

This command deploys the service:

* `coursesservice_web`: Web Service
* `coursesservice_db`: Data base
* `pgadmin`: Data base admin

## Stop services

```docker-compose stop```

## Down services and remove containers, networks, volumes and images created by 'up'

```docker-compose down```

## To run tests

```docker-compose exec web pytest .```


You can try it out at <https://staging-courses-service-app-v2.herokuapp.com/docs>
