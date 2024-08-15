import streamlit as st
import time as t
#image
st.image("ned.png")


#tittle
st.title("welcome to intellipaat made by ayesha siddiqui")

#header
st.header("Machine Learning")


#subheader
st.subheader("linear integration")

#for giving information
st.info("here are the detail of user info")


#warning msg
st.warning("Dont come late next time if you csme late so you would be eliminated")

#error
st.error("wrong password")

#success
st.success("congrtulations you got A grade")


#write func
st.write("Employee Name : Ayesha Riaz Ahmed Siddiqui")
st.write(range(50))

#markdown
st.markdown("# intellipaat")  #h1
st.markdown("## intellipaat") #h2
st.markdown("### intellipaat") #h3
st.markdown(":moon:")


#text
st.text("intellipaat learner")


#to write a caption
st.caption("caption is this")


#for writing expression
st.latex( '''ax+bx^2+c''')


#WIDGETS

#radio 
st.radio("select your gender",["male","female","other"])

#select
st.selectbox("choose your field",["cloud computing","quantum physics","geology"])

#multiselect
st.multiselect("choose your skills",["html","css","javascript","c","c++","oops","dsa"])

#select slider
st.select_slider("give the rating",["bad","average","good","excellent","wonderful"])

#number slider
st.slider("selct your number",0,70)

#number input
st.number_input("enter your number",0,90)


#text input
st.text_input("enter the text or email address")

#date input
st.date_input("enter the date of opening ceremony")


#time input
st.time_input("enter the time")

#text area
st.text_area("enter your msg")

#for uploading file and folder
st.file_uploader("upload any file or folder")

#colorpicker
st.color_picker("pic your desired color")

#progress
st.progress(67)


#spinner 
with st.spinner("want a while"):
    t.sleep(3)


#side bar
st.sidebar.title("this is the side bar")
st.sidebar.text_input("enter the email address")
st.sidebar.text_input("enter the password")
st.sidebar.radio("seelct professionalism",["student","teacher","faculty"])
st.sidebar.button("Submit")


#balloons


#checkbox
st.checkbox("done")

#button
st.button("submit")

st.balloons()






#DATA VISUALIZATION
import pandas as pd
import numpy as np
#bar chart
st.title("bar chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)

#line chart
st.title("line chart")  
st.line_chart(data)


#area chart
st.title("area chart")  
st.area_chart(data)