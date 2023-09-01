# Import of Streamlit and Request Library
import streamlit as st
import requests

# Function which is used to import the Hugging Face API Transformer Model
def model(data,s):
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):

        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    if s == 'Select':
        output = "Please Select Size"
    if s=='Very Small':
        output = query({
            "inputs" : data,
            # "parameters" : {"min_length" : 200,"max_length":200},
            "parameters" : {"min_length" : int(count/4)-10,"max_length":int(count/4)},
        })
    if s== 'Small':    
        output = query({
            "inputs" : data,
            # "parameters" : {"min_length" : 200,"max_length":200},
            "parameters" : {"min_length" : int(count/3)-10,"max_length":int(count/3)},
        })
    if s== 'Medium':    
        output = query({
            "inputs" : data,
            # "parameters" : {"min_length" : 200,"max_length":200},
            "parameters" : {"min_length" : int(count/2)-10,"max_length":int(count/2)},
        })
    if s== 'Large':    
        output = query({
            "inputs" : data,
            # "parameters" : {"min_length" : 200,"max_length":200},
            "parameters" : {"min_length" : int(count/1.5)-10,"max_length":int(count/1.5)},
        })
    if s == 'Very Large':
        output = query({
            "inputs" : data,
            # "parameters" : {"min_length" : 200,"max_length":200},
            "parameters" : {"min_length" : int(count/1.2)-10,"max_length":int(count/1.2)},
        })
    output = str(output)
    return output


def output(data):
    if(name != ''):
        st.subheader("Here your summary")
        st.write(model(data))

def full_text(data):
    if(name!=''):
        st.subheader("Heres your Full Article")
        st.write(name)
        

st.title("Article Summarize Website")
col1,col2 = st.columns([4,4])

# Orignal Form Which is used to take input as text\

with st.form(key='form1',clear_on_submit=False):
    name = st.text_input("Enter your Article")

    name = str(name)

    strr = ['Select','Very Small','Small','Medium','Large','Very Large']
    size = st.selectbox("Select Size of Summary",strr)
    
    result = st.form_submit_button(label="Get Summary")

    if name == "" and size == 'Select':
        st.success("Give me Text For Summary")
        
    if name =='' and size != 'Select':
        st.warning("Please Give me text First")
        # st.subheader("Here your summary")
        # st.write(model(name))

    count = 0
    for words in name.split():
        count +=1

    with col1:
        if name !='':
            st.subheader("Here's your Full Text")
            st.write(name)
            st.write(count)

    with col2:  

        if(name != '' and count<=56):
            st.warning("We Cant Make Short Summary of Article less 57 words")
            
        if (count>56):
            if result:
                st.subheader("Here's your Short Summary")
                try:
                    st.success(model(name,size))
                    count2 = 0
                    for words in model(name,size).split():
                        count2 +=1      
                    st.write(count2) 
                except :
                    st.warning("Please Kindly Check Yor Internet Connection")       
