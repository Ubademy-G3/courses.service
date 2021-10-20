# Courses Microservice

[![CI](https://github.com/Ubademy-G3/courses.service/actions/workflows/default.yml/badge.svg)](https://github.com/Ubademy-G3/courses.service/actions/workflows/default.yml)
[![codecov](https://codecov.io/gh/Ubademy-G3/courses.service/branch/main/graph/badge.svg?token=P5PT97QTE2)](https://codecov.io/gh/Ubademy-G3/courses.service)

# File Structure:
```tree
├── main.py
├── src
│   ├── infrastructure
│   │   ├── db
│   │   │   ├──  course_shema.py 
│   │   │   └──  database.py 
│   │   ├── routes
│   │   │   └──  courses.py
│   ├── persistence
│   │   └── repositories
│   │       └── course_repository_postgres.py
│   ├── application
│   │   ├── controllers
│   │   │   └── 
│   │   ├──serializers
│   │   │   └── 
│   │   └── useCases
│   │       └── 
│   └── domain
│       ├── course_model.py
│       └── course_repository.py
├── monitoring
├── deploy
└── tests
```

# Local Environment 

## Requirements 

* Docker
* Docker-compose

## Build and Deploy Services

```docker-compose up -d --build```

This command deploys the service:

* `coursesservice_web`: Web Service
* `coursesservice_db`: Data base
* `pgadmin`: Data base admin

## Stop services

```docker-compose stop```
