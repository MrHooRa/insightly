from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
import cohere
from streamlit_extras.switch_page_button import switch_page
from streamlit_autorefresh import st_autorefresh

from datetime import datetime, timezone

MODEL_ID = '28b1f720-22ff-4556-85bc-2ae1e0ee18cf-ft'
COHERE_API_KEY = 'KOmzoZw2eX5jJgZBG501EbzSykrb27O0OuKFMjOj'
MOVING_AVERAGE_NUM = 3
co = cohere.Client(COHERE_API_KEY)


def getUserTimeSpent():
	""" Return the total time spent on the website in seconds. """
	return (st.session_state['current_time'] - st.session_state['start_time']).total_seconds()

def classify_session():
    product_viewd_avg_price = (st.session_state['products_viewed_sum_price']/st.session_state['products_viewed'] if st.session_state['products_viewed'] != 0 else 0)
    product_added_avg_price = (st.session_state['products_added_sum_price']/st.session_state['products_added'] if st.session_state['products_added'] != 0 else 0)
    product_removed_avg_price = (st.session_state['products_removed_sum_price']/st.session_state['products_removed'] if st.session_state['products_removed'] != 0 else 0)
    
    if response := co.classify(
        model=MODEL_ID,
        inputs=[f"{getUserTimeSpent()} {st.session_state['products_viewed']} {product_viewd_avg_price} {st.session_state['products_added']} {product_added_avg_price} {st.session_state['products_removed']} {product_removed_avg_price}"]):
        return response.classifications[0]
    return []

st.set_page_config(
    page_title="Insightly Store - Home Page",
    page_icon="✨",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------
# Products
# ---------------------------------------------------------------------
products_list = [
      {		
			'id': 1,
            'name': 'Flashlight wide',
            'price': 99.99,
            'image': "img/product_single_01.jpg",
	    	'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod temp incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse. Donec condimentum elementum convallis. Nunc sed orci a diam ultrices aliquet interdum quis nulla.'
	  },
	  {
			'id': 2,			  			
            'name': 'Apple Watch 2',
            'price': 359.95,
            'image': "img/product_single_02.jpg",
	    	'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod temp incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse. Donec condimentum elementum convallis. Nunc sed orci a diam ultrices aliquet interdum quis nulla.'
	  },
	  {
			'id': 3,
            'name': 'Ultra Camera',
            'price': 259.95,
            'image': "img/product_single_03.jpg",
	    'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod temp incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse. Donec condimentum elementum convallis. Nunc sed orci a diam ultrices aliquet interdum quis nulla.'
	  }
]

if 'current_product' not in st.session_state:
	st.session_state['current_product'] = None

if 'cart' not in st.session_state:
	st.session_state['cart'] = []

if 'prod_msg' not in st.session_state:
    	st.session_state['prod_msg'] = ''
	        
# ---------------------------------------------------------------------
# End Products
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# User behavior 
# ---------------------------------------------------------------------

# set variables
if 'products_viewed' not in st.session_state:
    st.session_state['products_viewed'] = 0

if 'products_viewed_hrice' not in st.session_state:
    st.session_state['products_viewed_sum_price'] = 0

if 'products_added' not in st.session_state:
    st.session_state['products_added'] = 0

if 'products_added_sum_price' not in st.session_state:
    st.session_state['products_added_sum_price'] = 0

if 'products_removed' not in st.session_state:
    st.session_state['products_removed'] = 0

if 'products_removed_sum_price' not in st.session_state:
    st.session_state['products_removed_sum_price'] = 0

if 'start_time' not in st.session_state:
    st.session_state['start_time'] = datetime.now(timezone.utc)

if 'current_time' not in st.session_state:
    st.session_state['current_time'] = datetime.now(timezone.utc)

if 'moving_average' not in st.session_state:
	st.session_state['moving_average'] = []

if 'moving_average_probability' not in st.session_state:
    	st.session_state['moving_average_probability'] = {
			'0': 0,
			'1': 0
		}

# update cureent_time 
st.session_state['current_time'] = datetime.now(timezone.utc)

session_stats = classify_session()

# update moving average
if len(st.session_state['moving_average']) >= MOVING_AVERAGE_NUM:
    	st.session_state['moving_average'].pop(0)
st.session_state['moving_average'].append([session_stats.labels['0'].confidence * 100, session_stats.labels['1'].confidence * 100])

# update moving average probability
st.session_state['moving_average_probability']['0'] = sum(
	i[0] for i in st.session_state['moving_average']
) / len(st.session_state['moving_average'])

st.session_state['moving_average_probability']['1'] = sum(
	i[1] for i in st.session_state['moving_average']
) / len(st.session_state['moving_average'])


# ---------------------------------------------------------------------
# End User behavior data
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------
st.markdown(
    """
<style>
    [data-testid="stSidebarNav"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# User current session details
st.sidebar.markdown(f"""
                    <center><h3>Current user behavior</h3></center>
                    Total time spent (in seconds): {str(round(getUserTimeSpent(), 2))}<br>
					Products viewed: {st.session_state['products_viewed']}<br>
					Products added: {st.session_state['products_added']}<br>
					Products removed: {st.session_state['products_removed']}<br>
                    Session stats: <br>
                    <span style="padding-left:20px;">Not purchase ({str(round(st.session_state['moving_average_probability']['0'], 4))[:5]}%)</span><br>
                    <span style="padding-left:20px;">Purchase ({str(round(st.session_state['moving_average_probability']['1'], 4))[:5]}%)</span>
					""", unsafe_allow_html=True)
# ---------------------------------------------------------------------
# End Sidebar
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Body
# ---------------------------------------------------------------------

with st.container():
    header_title, home_btn = st.columns([4,1])
    with header_title:
        st.markdown("# Insightly Store ✨ ")

    with home_btn:
        if st.button('🛒 Cart', use_container_width=True):
            switch_page("cart")
        if st.button('👥 About', use_container_width=True):
            switch_page("about")

st.markdown(""" 
			welcome to the Insightly Store, where you can buy all the Insightly swag you want!
			""", unsafe_allow_html=True)	

# product list
with st.container():
	st.write("---")
	
	with st.container():
		header_col1, header_col2 = st.columns((1,2))

		with header_col1:
			st.header("Products")
		
		with header_col2:
			if st.session_state['prod_msg'] != '':
				st.success(st.session_state['prod_msg'], icon="🛒")
				st.session_state['prod_msg'] = ''
				st_autorefresh(interval=2000, limit=2)

	st.write("##")
	img_col1, img_col2, img_col3 = st.columns((1,1,1))
	with img_col1:
		st.write(f"<center><h5>{products_list[0]['name']}</h5></center>", unsafe_allow_html=True)
		st.image(Image.open(products_list[0]['image']))
		st.write(f"<center><h5>Price: ${products_list[0]['price']}</h5></center>", unsafe_allow_html=True)
		if st.button('View', key=f"view_{products_list[0]['name']}", use_container_width=True):
			st.session_state['current_product'] = products_list[0]
			st.session_state['products_viewed'] += 1
			st.session_state['products_viewed_sum_price'] += (products_list[0]['price']/60)

			switch_page("product")
		if st.button(f'Add to cart', key=f"add_{products_list[0]['name']}", use_container_width=True):
			st.session_state['cart'].append(products_list[0])
			st.session_state['products_added'] += 1
			st.session_state['prod_msg'] = f"{products_list[0]['name']} has been added to the cart!"
			st_autorefresh(interval=1, limit=2)


	with img_col2:
		st.write(f"<center><h5>{products_list[1]['name']}</h5></center>", unsafe_allow_html=True)
		st.image(Image.open(products_list[1]['image']))
		st.write(f"<center><h5>Price: ${products_list[1]['price']}</h5></center>", unsafe_allow_html=True)
		if st.button('View', key=f"view_{products_list[1]['name']}", use_container_width=True):
			st.session_state['current_product'] = products_list[1]
			st.session_state['products_viewed'] += 1
			st.session_state['products_viewed_sum_price'] += (products_list[1]['price']/60)

			switch_page("product")
		if st.button(f'Add to cart', key=f"add_{products_list[1]['name']}", use_container_width=True):
			st.session_state['cart'].append(products_list[1])
			st.session_state['products_added'] += 1
			st.session_state['prod_msg'] = f"{products_list[1]['name']} has been added to the cart!"
			st_autorefresh(interval=1, limit=2)

	with img_col3: 
		st.write(f"<center><h5>{products_list[2]['name']}</h5></center>", unsafe_allow_html=True)
		st.image(Image.open(products_list[2]['image']))
		st.write(f"<center><h5>Price: ${products_list[2]['price']}</h5></center>", unsafe_allow_html=True)
		if st.button('View', key=f"view_{products_list[2]['name']}", use_container_width=True):
			st.session_state['current_product'] = products_list[2]
			st.session_state['products_viewed'] += 1
			st.session_state['products_viewed_sum_price'] += (products_list[2]['price']/60)

			switch_page("product")
		if st.button(f'Add to cart', key=f"add_{products_list[2]['name']}", use_container_width=True):
			st.session_state['cart'].append(products_list[2])
			st.session_state['products_added'] += 1
			st.session_state['prod_msg'] = f"{products_list[2]['name']} has been added to the cart!"
			st_autorefresh(interval=1, limit=2)

# footer


# ---------------------------------------------------------------------
# End Body
# ---------------------------------------------------------------------