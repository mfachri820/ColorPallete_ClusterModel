import streamlit as st
from PIL import Image
from color_model import extract_dominant_colors, rgb_to_hex

def main():
    st.set_page_config(page_title="Color Picker Dominan Modular", layout="centered")
    st.title("🎨 Color Picker Warna Dominan dari Gambar")

    st.markdown("Upload gambar kamu, dan dapatkan 5 warna dominan yang diekstrak.")

    uploaded_file = st.file_uploader("Upload gambar (jpg/png)", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar Kamu", use_container_width=True)

        with st.spinner("Sedang mengekstrak warna dominan..."):
            colors = extract_dominant_colors(image, n_colors=5)

        st.subheader("Palet Warna Dominan")
        cols = st.columns(len(colors))

        for idx, col in enumerate(cols):
            rgb = colors[idx]
            hex_code = rgb_to_hex(rgb)
            col.markdown(
                f"""
                <div style="background-color:{hex_code}; padding:40px; border-radius:8px; text-align:center; color:#fff; font-weight:bold;">
                {hex_code}
                </div>
                """,
                unsafe_allow_html=True,
            )

if __name__ == "__main__":
    main()
