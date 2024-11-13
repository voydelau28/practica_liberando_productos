# Simple Server Project

## Descripción
Este proyecto implementa un servidor FastAPI con monitoreo y métricas. Incluye endpoints básicos y un despliegue en Kubernetes utilizando Helm, junto con la configuración de Prometheus y Alertmanager para la monitorización.

## Endpoints
- `/`: Devuelve `{"health": "ok"}`
- `/health`: Devuelve `{"message": "Hello World"}`
- `/bye`: Devuelve `{"msg": "Bye Bye"}`

## Configuración del Entorno
1. Asegúrate de tener Python 3.11.8 o superior.
2. Instala `virtualenv` con:
   ```bash
   pip3 install virtualenv

# Instalación

Crear un entorno virtual:
python3 -m venv venv

Activar el entorno:
source venv/bin/activate

Instalar dependencias:
pip3 install -r requirements.txt

# Construir y Ejecutar con Docker

Construir la imagen:
docker build -t simple-server:0.0.1 .

Ejecutar el contenedor:
docker run -d -p 8000:8000 -p 8081:8081 --name simple-server simple-server:0.0.1

# Despliegue en Kubernetes

Aplicar configuración de Prometheus:
kubectl apply -f k8s/prometheus-configmap.yaml

Desplegar la aplicación:
helm install simple-server helm-chart/

# Monitorización y Alertas

Las métricas se exponen en http://<EXTERNAL-IP>:8000.
Configura alertas usando alertmanager-config.yaml.

# Pruebas

Ejecuta los tests unitarios con:
pytest --cov

# Notas
Configura el archivo /etc/hosts para simple-server.local si usas Minikube.
Las alertas se envían al canal de Slack configurado.




