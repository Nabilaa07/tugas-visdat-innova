import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Penjualan Innova", layout="wide")

st.title("🚗 Dashboard Analisis Wholesales Toyota Innova")
st.markdown("Menganalisis tren penjualan berdasarkan model, bahan bakar, dan transmisi.")
st.divider()

# --- 1. MEMBACA DATA CSV LANGSUNG ---
# Ganti dengan nama file csv Anda jika berbeda
try:
    df = pd.read_csv("Innova_Wholesales_Data_2017_2026.csv")
    
    # Menampilkan sedikit data di paling atas
    with st.expander("Klik untuk melihat Data Tabel Mentah"):
        st.dataframe(df.head(100))

    # --- MEMBUAT VISUALISASI ---
    col1, col2 = st.columns(2)
    
    # Visualisasi 1: Total Penjualan per Tahun
    with col1:
        st.subheader("Tren Penjualan per Tahun")
        # Mengelompokkan data berdasarkan Tahun dan menjumlahkan Wholesale
        trend_tahunan = df.groupby('Year')['Wholesale'].sum().reset_index()
        
        fig_year, ax_year = plt.subplots(figsize=(8, 5))
        sns.lineplot(data=trend_tahunan, x='Year', y='Wholesale', marker='o', color='blue', ax=ax_year)
        ax_year.set_xlabel("Tahun")
        ax_year.set_ylabel("Total Unit Terjual")
        ax_year.grid(True, linestyle='--', alpha=0.6)
        st.pyplot(fig_year)
        
    # Visualisasi 2: Penjualan Berdasarkan Tipe Bahan Bakar (Fuel Type)
    with col2:
        st.subheader("Distribusi Penjualan per Tipe Bahan Bakar")
        fuel_sales = df.groupby('Fuel_Type')['Wholesale'].sum()
        
        fig_pie, ax_pie = plt.subplots(figsize=(8, 5))
        ax_pie.pie(fuel_sales, labels=fuel_sales.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2'))
        ax_pie.axis('equal') 
        st.pyplot(fig_pie)
        
    st.divider()
    
    col3, col4 = st.columns(2)
    
    # Visualisasi 3: Penjualan Model (Bar Chart)
    with col3:
        st.subheader("Total Penjualan per Model")
        model_sales = df.groupby('Model')['Wholesale'].sum().reset_index().sort_values(by='Wholesale', ascending=False)
        
        fig_bar, ax_bar = plt.subplots(figsize=(8, 5))
        sns.barplot(data=model_sales, x='Model', y='Wholesale', palette='viridis', ax=ax_bar)
        ax_bar.set_ylabel("Total Unit")
        plt.xticks(rotation=45)
        st.pyplot(fig_bar)
        
    # Visualisasi 4: Penjualan Transmisi
    with col4:
        st.subheader("Komparasi Tipe Transmisi")
        trans_sales = df.groupby('Transmission')['Wholesale'].sum().reset_index()
        
        fig_trans, ax_trans = plt.subplots(figsize=(8, 5))
        sns.barplot(data=trans_sales, x='Transmission', y='Wholesale', palette='mako', ax=ax_trans)
        ax_trans.set_ylabel("Total Unit")
        st.pyplot(fig_trans)

except FileNotFoundError:
    st.error("Gagal memuat data! Pastikan file 'Innova_Wholesales_Data_2017_2026.csv' sudah diekstrak dari zip dan diletakkan di dalam folder yang sama dengan app.py.")
except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")