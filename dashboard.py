import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

order_items_df = pd.read_csv("order_items_dataset.csv")
sellers_df = pd.read_csv("sellers_dataset.csv")

merged_data = order_items_df.merge(sellers_df, on="seller_id", how="left")

seller_distribution = sellers_df["seller_state"].value_counts().reset_index()
seller_distribution.columns = ["seller_state", "total_sellers"]

transactions_per_location = merged_data.groupby(["seller_city", "seller_state"])["order_id"].count().reset_index()
transactions_per_location.rename(columns={"order_id": "total_transactions"}, inplace=True)

st.title("Dashboard Analisis Data E-Commerce")

menu = st.sidebar.selectbox("Pilih Analisis:", ["Distribusi Penjual per Negara Bagian", "Jumlah Transaksi per Lokasi Penjual"])

if menu == "Distribusi Penjual per Negara Bagian":
    st.header("Distribusi Penjual Berdasarkan Negara Bagian")
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='seller_state', y='total_sellers', data=seller_distribution.sort_values(by='total_sellers', ascending=False), palette='Blues_d', ax=ax)
    ax.set_title('Distribusi Penjual Berdasarkan Negara Bagian', fontsize=14)
    ax.set_xlabel('Negara Bagian')
    ax.set_ylabel('Jumlah Penjual')
    st.pyplot(fig)

elif menu == "Jumlah Transaksi per Lokasi Penjual":
    st.header("Jumlah Transaksi Berdasarkan Lokasi Penjual")
    
    top_cities = transactions_per_location.sort_values(by="total_transactions", ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=top_cities, x="total_transactions", y="seller_city", palette="viridis", ax=ax)
    ax.set_xlabel("Jumlah Transaksi")
    ax.set_ylabel("Kota Penjual")
    ax.set_title("10 Kota dengan Transaksi Terbanyak")
    st.pyplot(fig)

# Footer
st.sidebar.markdown("---")
st.sidebar.text("Dashboard by Bayu - Laskar AI")
