# Ejecuta la app con Docker Compose
run:
    docker-compose up --build

# Ejecuta los tests dentro del contenedor web (asumiendo que la app está en /app)
test:
    docker-compose exec devops_web pytest --cov=app --cov-report=term

# Linting con flake8 sobre la app y pruebas
lint:
    flake8 app tests

# Genera reporte HTML de cobertura
coverage:
    docker-compose exec devops_web pytest --cov=app --cov-report=html
