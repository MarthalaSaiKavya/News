import pandas as pd
import numpy as np
import praw
import streamlit as st
st.set_page_config(layout="wide")
user_agent="Scraper 1.0 by /u/kav_yay"
reddit=praw.Reddit(
client_id="YCp6d62ye13q-A",
client_secret="ytcu1vnZJyHO_pK2PZC_fX2Q6ImfSA",
user_agent=user_agent
)

title_list = []
subreddit = reddit.subreddit('UpliftingNews')
hot_post = subreddit.hot(limit=20)
for sub in hot_post:
    title_list.append(sub.title)

df = pd.DataFrame({ 'NEWS':title_list})
new_df= df.iloc[1:15, :]
new_df.head(10)

st.title("Uplifting News")
result=st.button("Click Here")
if result:
    st.write(new_df.head(10))

