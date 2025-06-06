import json
import os
import redis
import paho.mqtt.client as mqtt

# Archivo de configuración
CONFIG_FILE = "conf.json"

if not os.path.exists(CONFIG_FILE):
    raise FileNotFoundError(f"Falta el archivo de configuración: {CONFIG_FILE}")

with open(CONFIG_FILE) as f:
    config = json.load(f)

REDIS_HOST = config['REDIS_HOST']
REDIS_PORT = config['REDIS_PORT']
MQTT_BROKER = config['MQTT_BROKER']
MQTT_PORT = config['MQTT_PORT']
MQTT_TOPIC = config['MQTT_TOPIC']

r = redis.Redis(host=REDIS_HOST,
                port = REDIS_PORT,
                decode_responses=True)

def on_connect(client, userdata, flags, rc):
    print(f"Conectado al broker MQTT con código {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    print(f"Mensaje recibido en {msg.topic}: {payload}")
    try:
        data = json.loads(payload)
    except json.JSONDecodeError:
        data = payload

    r.lpush('mqtt_messages', json.dumps(data))
    print("Guardado en Redis")

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()

if __name__ == '__main__':
    main()