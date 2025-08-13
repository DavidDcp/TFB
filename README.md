# TFB
REQUISITOS:

- Python 3.10+
- PostgreSQL (o Docker)
- pip
- Docker y Docker Compose (opcional)

Pasos a seguir:

EN LOCAL
1. Descargar el zip del proyecto o clonar con el comando
git clone https://github.com/DavidDcp/TFB.git
cd TFB

2. Copiar el archivo de entorno
cp env.example .env

3.Entorno virtual
$env:PYTHONPATH = "C:\turuta"
python -m venv venv
source venv/bin/activate       (venv\Scripts\activate en Windows)

4. Instalar las dependencias
pip install -r requirements.txt
pip list (OPCIONAL PARA VER QUE SE INSTALÓ)

5.Variables de entorno Flask
export FLASK_APP=app      ($env:FLASK_APP = "app" en Windows)

6.Ejecutar
flask run

7.Ejecutar Tests
pytest -v

CON DOCKER:

Contruir imagen y levantar servicio
1. docker compose build
2. docker compose up

