import  pickle
import streamlit as st
from streamlit_option_menu import option_menu


model = pickle.load(open("Indutrial_copper_model.pkl","rb"))

st.title('Industrial copper modelling')

with st.sidebar:
    
    selected = option_menu('Copper model status prediction',
                          ['Predict your status now...'],
                          default_index=0)
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write("Contact me")

    gmail_url = "mailto:jkbioinfo99@gmail.com"
    st.markdown(f'<a href="{gmail_url}" target="_blank"><i class="far fa-envelope"></i> jkbioinfo99@gmail.com</a>', unsafe_allow_html=True)

    github_url = "https://github.com/JayaKrishanS"
    st.markdown(f'<a href="{github_url}" target="_blank"><i class="fab fa-github"></i>  GitHub</a>', unsafe_allow_html=True)

    linkedin_url = "https://www.linkedin.com/in/jaya-krishna-s-aab674196/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>', unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)



if (selected == 'Predict your status now...'):
    
    st.markdown("<h5 style='color: orange;'>Kindly enter the details for prediction</h5>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    
    with col1:
        st.write(' ')
        item_type = st.number_input("Item Type", value=5.0)
        country = st.number_input("Country", value=28.0)
        application = st.number_input("Application", value=10.0)
        product_ref = st.number_input("Product Reference", value=1670798778)
    with col3:               
        quantity_tons = st.number_input("Quantity Tons", value=54.151139)
        thickness = st.number_input("Thickness", value=2.0)
        width = st.number_input("width", value=1500.0)
        customer = st.number_input("customer ID", value=30156308.0)
        selling_price = st.number_input("Enter the price ", value=854.0)

status_diagnosis = ''
if st.button('Predict'):
    status_prediction = model.predict([[quantity_tons, customer, country, item_type, application, thickness, width, product_ref, selling_price]])                          
    if (status_prediction[0] == 1):
        status_diagnosis = 'The status is WON'
    else:
        status_diagnosis = 'The status is LOST'
    
    st.success(status_diagnosis)
