from fastapi import FastAPI
from prometheus_client import Counter, start_http_server

app = FastAPI()

# Iniciar servidor de métricas en el puerto 8000
start_http_server(8000)

# Contadores de Prometheus
server_requests_total = Counter('server_requests_total', 'Total number of requests to this webserver')
healthcheck_requests_total = Counter('healthcheck_requests_total', 'Total number of requests to healthcheck')
main_requests_total = Counter('main_requests_total', 'Total number of requests to main endpoint')
bye_requests_total = Counter('bye_requests_total', 'Total number of requests to bye endpoint')

@app.get("/")
async def read_root():
    main_requests_total.inc()
    server_requests_total.inc()
    return {"health": "ok"}

@app.get("/health")
async def health_check():
    healthcheck_requests_total.inc()
    server_requests_total.inc()
    return {"message": "Hello World"}

# Nuevo endpoint
@app.get("/bye")
async def say_bye():
    bye_requests_total.inc()
    server_requests_total.inc()
    return {"msg": "Bye Bye"}
