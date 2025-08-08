# Imagen base oficial de Python optimizada
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# directorio
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Variables por defecto (se pueden sobrescribir con .env)
ENV FLASK_ENV=production \
    PORT=5000

# Exponer el puerto de la app
EXPOSE 5000

# Asegurar permisos de ejecución al entrypoint
RUN chmod +x ./entrypoint.sh

# Comando de arranque
ENTRYPOINT ["./entrypoint.sh"]
