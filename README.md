# UCV-SI-lab5

## Descripción

Este proyecto es parte del laboratorio 5 de la asignatura Sistemas de Información en la Universidad Central de Venezuela (UCV). Implementa un sistema de análisis de métricas para imágenes en escala de grises, utilizando Python con bibliotecas como NumPy, OpenCV y Matplotlib. Incluye una API REST construida con FastAPI para el procesamiento de imágenes subidas por el usuario.

El sistema calcula métricas estadísticas básicas de las imágenes (media, desviación estándar, mínimo y máximo) y proporciona una API para integrar estas funcionalidades en aplicaciones web.

## Características

- **Cálculo de métricas**: Media, desviación estándar, valor mínimo y máximo de píxeles en imágenes en escala de grises.
- **Visualización**: Generación de histogramas de distribución de píxeles.
- **API REST**: Endpoint para subir imágenes y obtener métricas automáticamente.
- **Procesamiento de imágenes**: Soporte para imágenes en formato compatible con OpenCV.
- **Pruebas unitarias**: Cobertura básica con pytest.

## Tecnologías Utilizadas

- **Python 3.11+**
- **NumPy**: Para cálculos numéricos.
- **Matplotlib**: Para visualización de histogramas.
- **OpenCV**: Para lectura y procesamiento de imágenes.
- **FastAPI**: Framework para la API REST.
- **Uvicorn**: Servidor ASGI para FastAPI.
- **Poetry**: Gestión de dependencias y construcción del proyecto.
- **Pytest**: Para pruebas unitarias.

## Instalación

### Prerrequisitos

- Python 3.11 o superior instalado.
- Poetry para gestión de dependencias (instalar con `pip install poetry`).

### Pasos de Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/joshiel123/UCV-SI-lab5.git
   cd UCV-SI-lab5
   ```

2. Instala las dependencias usando Poetry:
   ```bash
   poetry install
   ```

3. Activa el entorno virtual:
   ```bash
   poetry shell
   ```

## Uso

### API

La API proporciona un endpoint para analizar métricas de imágenes.

#### Endpoint: `/analyze-metrics`

- **Método**: POST
- **Descripción**: Sube una imagen y recibe las métricas calculadas.
- **Parámetros**:
  - `file`: Archivo de imagen (multipart/form-data).
- **Respuesta**: JSON con métricas (mean, std, min, max).

Ejemplo de uso con curl:
```bash
curl -X POST "http://localhost:8000/analyze-metrics" -F "file=@imagen.jpg"
```

#### Ejecutar la API

1. Desde el directorio del proyecto:
   ```bash
   uvicorn src.lab5_metrics.api.main:app --reload
   ```

2. Accede a la documentación interactiva en `http://localhost:8000/docs`.

### Uso Programático

```python
from lab5_metrics.analyzer import ImageMetrics
import cv2

# Cargar imagen
imagen = cv2.imread('ruta/a/imagen.jpg', 0)  # Escala de grises

# Calcular métricas
analyzer = ImageMetrics()
metricas = analyzer.calcular_metricas(imagen)
print(metricas)

# Generar histograma
analyzer.generar_histograma(imagen)
```

## Pruebas

Ejecuta las pruebas con pytest:

```bash
pytest tests/
```

## Estructura del Proyecto

```
UCV-SI-lab5/
├── data/                    # Directorio para imágenes subidas
├── src/
│   └── lab5_metrics/
│       ├── analyzer.py      # Clase para cálculo de métricas y visualización
│       ├── api/
│       │   └── main.py      # API REST con FastAPI
│       └── services/
│           └── metrics_service.py  # Servicio de análisis de métricas
├── tests/
│   └── test_metrics.py      # Pruebas unitarias
├── pyproject.toml           # Configuración del proyecto y dependencias
├── sonar-project.properties # Configuración para SonarCloud
└── README.md                # Este archivo
```

## Análisis de Calidad

El proyecto está configurado para análisis con SonarCloud. Para ejecutar análisis local:

1. Instala SonarQube Scanner.
2. Ejecuta:
   ```bash
   sonar-scanner
   ```

## Contribución

Este es un proyecto académico. Para contribuciones, contacta al autor.

## Autor

- **Joshi Alfageme Negrón**
- Email: jalfagemene@ucvvirtual.edu.pe
- Universidad Central de Venezuela

## Licencia

Este proyecto es para fines educativos y no tiene una licencia específica asignada.