import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="YouTube Analysis",
    layout="wide"
)

# Load dataset
df = pd.read_csv("data/INvideos.csv")

# Title
st.title("YouTube Trending Video Analysis")

# Show dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Top viewed videos
st.subheader("Top 10 Most Viewed Videos")

top_videos = df.sort_values(by='views', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(12,6))

sns.barplot(
    x='views',
    y='title',
    data=top_videos,
    ax=ax
)

st.pyplot(fig)

# Views vs Likes
st.subheader("Views vs Likes")

fig2, ax2 = plt.subplots(figsize=(10,6))

sns.scatterplot(
    x='views',
    y='likes',
    data=df,
    ax=ax2
)

st.pyplot(fig2)

# Sidebar
st.sidebar.title("Filter")

selected_channel = st.sidebar.selectbox(
    "Select Channel",
    df['channel_title'].unique()
)

filtered_data = df[df['channel_title'] == selected_channel]

st.write(filtered_data.head())


st.metric("Total Videos", len(df))
st.metric("Total Views", int(df['views'].sum()))

st.subheader("Correlation Heatmap")

fig3, ax3 = plt.subplots(figsize=(10,6))

sns.heatmap(
    df[['views', 'likes', 'dislikes', 'comment_count']].corr(),
    annot=True,
    cmap='coolwarm',
    ax=ax3
)

st.pyplot(fig3)