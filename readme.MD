# Dominant Color Picker

A simple web app built with Streamlit that extracts **5 dominant colors** from an uploaded image using K-Means clustering.

## How to Use

1. Clone this repo or download the files  
2. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate   # Linux/macOS
   env\Scripts\activate      # Windows

3. Install dependencies:

    ```bash
    Copy
    pip install -r requirements.txt
    Run the app:

    Bash
    Copy
    streamlit run app.py
    Upload an image and see the dominant color palette displayed.

File Structure
-app.py — Streamlit UI for uploading image and displaying colors
-color_model.py — clustering functions and color helpers
-requirements.txt — list of Python dependencies

Technologies Used
-Python 3.x
-Streamlit
-scikit-learn (KMeans)
-Pillow
-NumPy
