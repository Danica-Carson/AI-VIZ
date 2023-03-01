from chushi import chu

chu()

import streamlit as st
from location import locate
from PIL import Image

st.title('My first app')

form1 = st.form(key='my_form1')#key是form的关键字，不同form的key不能相同
input_text=form1.text_input(label='Enter some text')
submit_button = form1.form_submit_button(label='Submit')

if submit_button:
        locate(input_text)
        image = Image.open('final_canvas.jpg')
        st.image(image, caption=input_text,use_column_width=True)
