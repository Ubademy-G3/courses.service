# Microservicio de Cursos

[![CI](https://github.com/Ubademy-G3/courses.service/actions/workflows/default.yml/badge.svg)](https://github.com/Ubademy-G3/courses.service/actions/workflows/default.yml)
[![codecov](https://codecov.io/gh/Ubademy-G3/courses.service/branch/main/graph/badge.svg?token=P5PT97QTE2)](https://codecov.io/gh/Ubademy-G3/courses.service)

# Estructura de archivos:
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

# Entorno local

## Requerimientos

* Docker
* Docker-compose

## Construir y levantar servicios

```docker-compose up -d --build```

Este comando levanta los servicios:

* `coursesservice_web`: Servicio web
* `coursesservice_db`: Base de datos
* `pgadmin`: Admin para base de datos

## Detener servicios

```docker-compose stop```
