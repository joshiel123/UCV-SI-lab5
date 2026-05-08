import cv2
from lab5_metrics.analyzer import ImageMetrics
def analizar(path: str):
    imagen = cv2.imread(path, 0)
    analyzer = ImageMetrics()
    return analyzer.calcular_metricas(imagen)