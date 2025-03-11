import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
order_items_df = pd.read_csv("order_items_dataset.csv")
sellers_df = pd.read_csv("sellers_dataset.csv")

# Gabungkan dataset untuk analisis transaksi per lokasi penjual
merged_data = order_items_df.merge(sellers_df, on="seller_id", how="left")

# Data untuk visualisasi pertanyaan 1
seller_distribution = sellers_df["seller_state"].value_counts().reset_index()
seller_distribution.columns = ["seller_state", "total_sellers"]
top_cities = sellers_df['seller_city'].value_counts().head(10).reset_index()
top_cities.columns = ['seller_city', 'total_sellers']

# Data untuk visualisasi pertanyaan 2
transactions_by_city = merged_data.groupby('seller_city')['order_id'].nunique().reset_index()
transactions_by_city.columns = ['seller_city', 'total_transactions']
top_cities_transactions = transactions_by_city.sort_values(by='total_transactions', ascending=False).head(10)
transactions_by_state = merged_data.groupby('seller_state')['order_id'].nunique().reset_index()
transactions_by_state.columns = ['seller_state', 'total_transactions']

# Judul Dashboard
st.title("Dashboard Analisis Data E-Commerce")

# Sidebar untuk navigasi
menu = st.sidebar.selectbox("Pilih Pertanyaan Analisis:", [
    "Pertanyaan 1",
    "Pertanyaan 2"
])

if menu == "Pertanyaan 1":
    st.header("Pertanyaan 1")
    st.write("**Di wilayah mana saja sebagian besar penjual berada, dan bagaimana distribusinya berdasarkan negara bagian?**")

    # Visualisasi Top 10 Kota dengan Jumlah Penjual Terbanyak
    st.subheader("Top 10 Kota dengan Jumlah Penjual Terbanyak")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='total_sellers', y='seller_city', data=top_cities, palette='viridis', ax=ax)
    ax.set_title('Top 10 Kota dengan Jumlah Penjual Terbanyak')
    st.pyplot(fig)

    # Visualisasi Distribusi Penjual Berdasarkan Negara Bagian
    st.subheader("Distribusi Penjual Berdasarkan Negara Bagian")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='seller_state', y='total_sellers', data=seller_distribution.sort_values(by='total_sellers', ascending=False), palette='Blues_d', ax=ax)
    ax.set_title('Distribusi Penjual Berdasarkan Negara Bagian')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    # Conclusion
    st.subheader("Conclusion")
    st.write("Sebagian besar penjual terpusat di beberapa kota besar seperti São Paulo, Rio de Janeiro, dan Belo Horizonte. Distribusi penjual berdasarkan negara bagian menunjukkan bahwa wilayah seperti São Paulo dan Minas Gerais memiliki konsentrasi penjual yang lebih tinggi dibandingkan negara bagian lainnya.")

elif menu == "Pertanyaan 2":
    st.header("Pertanyaan 2")
    st.write("**Bagaimana hubungan antara lokasi penjual dan jumlah transaksi yang mereka terima?**")

    # Visualisasi Top 10 Kota dengan Jumlah Transaksi Terbanyak
    st.subheader("Top 10 Kota dengan Jumlah Transaksi Terbanyak")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='total_transactions', y='seller_city', data=top_cities_transactions, palette='magma', ax=ax)
    ax.set_title('Top 10 Kota dengan Jumlah Transaksi Terbanyak')
    st.pyplot(fig)

    # Visualisasi Jumlah Transaksi Berdasarkan Negara Bagian
    st.subheader("Jumlah Transaksi Berdasarkan Negara Bagian")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='seller_state', y='total_transactions', data=transactions_by_state.sort_values(by='total_transactions', ascending=False), palette='coolwarm', ax=ax)
    ax.set_title('Jumlah Transaksi Berdasarkan Negara Bagian Penjual')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    # Conclusion
    st.subheader("Conclusion")
    st.write("Terdapat korelasi positif antara lokasi penjual dan jumlah transaksi yang diterima. Kota-kota besar dengan jumlah penjual yang tinggi juga cenderung memiliki volume transaksi yang lebih besar. Selain itu, negara bagian dengan distribusi penjual yang lebih luas juga menunjukkan aktivitas transaksi yang lebih tinggi.")

# Footer
st.sidebar.markdown("---")
st.sidebar.text("Dashboard by Bayu - Laskar AI")
