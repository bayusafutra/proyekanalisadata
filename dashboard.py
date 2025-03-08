import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
order_items_df = pd.read_csv("order_items_dataset.csv")
sellers_df = pd.read_csv("sellers_dataset.csv")

# Gabungkan dataset untuk analisis transaksi per lokasi penjual
merged_data = order_items_df.merge(sellers_df, on="seller_id", how="left")
transactions_per_location = merged_data.groupby(["seller_city", "seller_state"])['order_id'].count().reset_index()
transactions_per_location.rename(columns={"order_id": "total_transactions"}, inplace=True)

# Judul Dashboard
st.title("Dashboard Analisis Data E-Commerce")

# Sidebar untuk navigasi
menu = st.sidebar.selectbox("Pilih Analisis:", ["Distribusi Harga Produk", "Korelasi Harga & Biaya Pengiriman", "Jumlah Transaksi per Lokasi Penjual"])

if menu == "Distribusi Harga Produk":
    st.header("Distribusi Harga Produk")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(order_items_df["price"], bins=50, kde=True, ax=ax)
    ax.set_xlabel("Harga Produk")
    ax.set_ylabel("Jumlah Produk")
    ax.set_title("Distribusi Harga Produk")
    st.pyplot(fig)
    
elif menu == "Korelasi Harga & Biaya Pengiriman":
    st.header("Korelasi antara Harga Produk dan Biaya Pengiriman")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(data=order_items_df, x="price", y="freight_value", alpha=0.5, ax=ax)
    ax.set_xlabel("Harga Produk")
    ax.set_ylabel("Biaya Pengiriman")
    ax.set_title("Korelasi antara Harga Produk dan Biaya Pengiriman")
    st.pyplot(fig)
    
elif menu == "Jumlah Transaksi per Lokasi Penjual":
    st.header("Jumlah Transaksi Berdasarkan Lokasi Penjual")
    
    top_cities = transactions_per_location.sort_values(by="total_transactions", ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=top_cities, x="total_transactions", y="seller_city", palette="viridis", ax=ax)
    ax.set_xlabel("Jumlah Transaksi")
    ax.set_ylabel("Kota Penjual")
    ax.set_title("10 Kota dengan Transaksi Terbanyak")
    st.pyplot(fig)
    
# Footer
st.sidebar.markdown("---")
st.sidebar.text("Dashboard by Bayu - Laskar AI")
