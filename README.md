# MQTT-REDIS

Este proyecto escucha mensajes desde un broker MQTT y los guarda en Redis. Está diseñado para sensores tipo DHT22 que publican en diferentes topics según si están en interior o exterior.

## 📦 Estructura del proyecto

mqtt-redis/
├── config_loader.py
├── main.py
├── mqtt_client.py
├── conf_dev.json
├── requirements.txt
├── README.md
└── venv/ # Ignorado en Git


## ⚙️ Requisitos

- Python 3.8 o superior
- Redis en ejecución (local o remoto)
- Broker MQTT accesible (por ejemplo, Mosquitto o HiveMQ)

## 🔧 Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tuusuario/mqtt-redis.git
   cd mqtt-redis
2. Crea un entorno virtual
   ```bash
    python3 -m venv venv
    source venv/bin/activate
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
## ⚙️ Configuración

Modifica el archivo de configuración conf.json

## 🚀 Ejecución
Para iniciar el listener que guarda los mensajes en Redis:

    source venv/bin/activate
    python main.py
Para publicar mensajes de prueba a MQTT desde otro script incluido:
    
    python mqtt_client.py


