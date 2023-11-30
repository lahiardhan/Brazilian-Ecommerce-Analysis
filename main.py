import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

data = pd.read_csv('data_ready.csv')


with st.sidebar:
    
    # Menambahkan logo perusahaan
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png")
    url = "https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset"
    link_text = "Visit Kaggle Dataset "

    # Create the link
    st.write('Bike Aharing Dataset')
    st.write(f"[{link_text}]({url})")

    
    

st.header('Bike Sharing Analysis')

st.subheader('Pengaruh Cuaca Terhadap Penyewaan Sepeda')

penyewa_by_cuaca = data.groupby('weathersit', as_index = False)['cnt'].mean()
season_names = ['Clear, Few clouds', 'Cloudy, Mist', 'Light Snow, Light Rain']

fig, ax = plt.subplots()
bars = ax.bar(season_names, penyewa_by_cuaca['cnt'])

plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Sewa Harian')
plt.title('Pengaruh Cuaca Terhadap Jumlah Sewa Sepeda Harian')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/3, yval, round(yval, 2))
st.pyplot(fig)

st.subheader('Jumlah Penyewa pada Hari Kerja dan Hari Libur')
penyewa_by_day = data.groupby('workingday',as_index = False)['cnt'].mean()
day = ['Holiday/Weekend', 'Working Day']
fig, ax = plt.subplots()
bars = ax.bar(day, penyewa_by_day['cnt'])

plt.xlabel('Kondisi')
plt.ylabel('Rata-rata Jumlah Sewa Harian')
plt.title('Perbandingan Sewa Sepeda Saat Working day dan Holiday/Weekend')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/3, yval, round(yval, 2))
st.pyplot(fig)

col1, col2 = st.columns(2)
tipe_penyewa = data.groupby('workingday',as_index = False)[['registered', 'casual']].sum()
with col1: 
    fig, ax = plt.subplots()
    plt.pie([tipe_penyewa['registered'][0], tipe_penyewa['casual'][0] ], labels = ['Registered', ' Casual'], autopct='%1.0f%%')
    plt.title('Perbandingan Penyewa Terdaftar dan Tidak Terdaftar Saat Weekend/Holiday')
    st.pyplot(fig)
with col2:
    fig, ax = plt.subplots()
    plt.pie([tipe_penyewa['registered'][1], tipe_penyewa['casual'][1] ], labels = ['Registered', ' Casual'], autopct='%1.0f%%')
    plt.title('Perbandingan Penyewa Terdaftar dan Tidak Terdaftar Saat Working Day')
    st.pyplot(fig)
    
st.subheader('Grafik Penyewaan Sepeda 2011-2012')
penyewa_by_month = data.groupby('year_month',as_index = False)['cnt'].sum()
penyewa_by_month['year_month'] = penyewa_by_month['year_month'].astype(str)

fig, ax = plt.subplots()
plt.figure(figsize=(10,6))
plot = ax.plot(penyewa_by_month['year_month'], penyewa_by_month['cnt'])
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Sewa Sepeda')
ax.set_xticklabels(penyewa_by_month['year_month'],rotation=25)
ax.set_title('Perkembangan Jumlah Penyewaan Sepeda')
st.pyplot(fig)