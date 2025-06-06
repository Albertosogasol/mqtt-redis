/mi-proyecto-mqtt-redis
│
├── docker-compose.yml       # Orquestación del contenedor Redis y, opcional, el script Python
├── redis/                   # Opcional: carpeta para configuración o Dockerfile de Redis
│   └── ...                 
│
└── mqtt-to-redis/           # Código Python para el script
    ├── requirements.txt     # Dependencias: paho-mqtt, redis, etc.
    ├── main.py              # Script principal para leer MQTT y escribir en Redis
    └── README.md            # Explicación del script y cómo usarlo