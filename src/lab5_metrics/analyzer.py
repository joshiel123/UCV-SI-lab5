import numpy as np
import matplotlib.pyplot as plt

class ImageMetrics:
    def calcular_metricas(self, imagen):
        return {
            "mean": float(np.mean(imagen)),
            "std": float(np.std(imagen)),
            "min": int(np.min(imagen)),
            "max": int(np.max(imagen))
        }

    # Nuevo método para la visualización
    def generar_histograma(self, imagen):
        plt.hist(imagen.flatten(), bins=50, color='blue', alpha=0.7)
        plt.title("Histograma de Distribución de Píxeles")
        plt.xlabel("Intensidad de Gris")
        plt.ylabel("Frecuencia")
        plt.show()