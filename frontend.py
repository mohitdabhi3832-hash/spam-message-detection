import streamlit as st
import pickle

model=pickle.load(open('model.pkl','rb'))
c=pickle.load(open('vectorizer.pkl','rb'))
st.title("Spam Message Prediction.")

msg=st.text_area("Enter Meaasge.")

if st.button("check"):
    data=c.transform([msg])
    pred= model.predict(data)

    if pred[0]==1:
        st.error("spam message..")
    else:
        st.success("Normal message..")