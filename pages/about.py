import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title="Insightly - About us",
    page_icon="✨",
    initial_sidebar_state="collapsed",
)

with st.container():
    header_title, home_btn = st.columns([4,1])
    with header_title:
        st.markdown("# About")

    with home_btn:
        if st.button('📟 Demo', use_container_width=True):
            switch_page("main_page")

st.header('Team Members')
team_cols = st.columns(4)
with team_cols[0]:
    st.image(
        'https://media.licdn.com/dms/image/D4D03AQHKSS0hnIPH9A/profile-displayphoto-shrink_800_800/0/1682775053750?e=1694044800&v=beta&t=Va4esOiGbYKVO_hSYBWV9iegHCAjEvqmVs6Qet4-mhQ', 
        caption='Salman Alessa',clamp=True)
    
    st.write('Data Scientist')
    st.write('[LinkedIn](https://www.linkedin.com/in/smalessa/)')
            
with team_cols[1]:
    st.image(
        'https://media.licdn.com/dms/image/D4E03AQGkaax11-rxVQ/profile-displayphoto-shrink_800_800/0/1684507881780?e=1694044800&v=beta&t=3S_GFX9ZpO3ZMhCkGKOY_ZMsBFBdCCeDVlyqlZ0BEPI', 
        caption='Saad Alabdulsalam',clamp=True)
    
    st.write('AI&ML Devloper')
    st.write('[LinkedIn](https://www.linkedin.com/in/saad-alabdulsalam-55b9361a5/)')

with team_cols[2]:
    st.image(
        'https://media.licdn.com/dms/image/D4D03AQGc1Z1MXSve0A/profile-displayphoto-shrink_800_800/0/1646027763319?e=1694044800&v=beta&t=Q6daLRhbq03ag7kPOTFZbaoQJhI0-jmjV316_arhC-M', 
        caption='Abdulaziz Matar',clamp=True)
    
    st.write('Bounty Hunter')
    st.write('[LinkedIn](https://www.linkedin.com/in/abdulaziz-matar-83b238203/)')
            
with team_cols[3]:
    st.image(
        'https://media.licdn.com/dms/image/D4E03AQHBYcfK46JLZQ/profile-displayphoto-shrink_800_800/0/1676151939014?e=1694044800&v=beta&t=taRWa5-KV4iO242t6EmTcHH8H9koh7ms6f_30Q3Z2J8', 
        caption='Fahd Alaskar',clamp=True)
    
    st.write('Busniess Analyst')
    st.write('[LinkedIn](https://www.linkedin.com/in/fahd-alaskar-986b57256/)')

## Problem Statement
st.markdown('''
## Problem Statement

This statement highlights the importance of creating a positive
online shopping experience to attract and retain customers in the
competitive digital marketplace. Despite having a well-designed
website, the sales figures are not meeting expectations.''')


## Solution Overview
cols =  st.columns(2)
with cols[0]:
    st.markdown('''
## Solution Overview
The project aims to identify the reasons behind the low customer
conversion rate and take actionable steps to improve the customer
experience, boost sales, and achieve greater business success and
customer satisfaction. This allows online store owners to incorage the user to buy the products, by showing them the some marketing techniques. such as: discount, free shipping, and more.
''')

with cols[1]:
    st_lottie("https://assets5.lottiefiles.com/packages/lf20_9wpyhdzo.json")


## Features
st.markdown('''
## Key Features
''')
            
cols = st.columns(2)
with cols[0]:
    st.markdown('''
### Cohere

Provides access to advanced Large Language Models and NLP tools through one easy-to-use API. Get started for free.
''')

with cols[1]:
    st.markdown('''
### Data Aggregation

By aggregating data from multiple sources, our trained model provides a tool to classify each session. 
''')

st.write('---')

st.title('About Project')

## Value Proposition
st.markdown('''
## Value Proposition

The project offers innovative solutions to increase sales and customer loyalty for online stores. 
It can track and analyze customer behavior, offer temporary discount codes to incentivize purchases, and provide valuable insights into customer behavior.

''')

## Target Market
st.markdown('''
## Target Market

The target market for the project is online stores that are looking to improve their sales and customer satisfaction.

''')


## Business Model
st.markdown('''
## Business Model

We plan to offer a subscription-based AI-powered solution for online stores to increase sales and loyalty, complemented by a commission-based model.

''')