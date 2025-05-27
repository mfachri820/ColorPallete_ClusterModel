from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def extract_dominant_colors(image: Image.Image, n_colors=5):
    """
    Ekstrak warna dominan dari gambar menggunakan KMeans clustering.
    Input:
        image: PIL Image object
        n_colors: jumlah warna dominan yang diinginkan
    Output:
        colors: list warna dominan dalam format RGB integer
    """
    img = image.convert('RGB')
    pixels = np.array(img).reshape(-1, 3)

    kmeans = KMeans(n_clusters=n_colors, random_state=42, n_init=10)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_.astype(int)
    return colors

def rgb_to_hex(rgb):
    """Konversi tuple RGB ke string HEX."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)
