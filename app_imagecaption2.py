import numpy as np
import streamlit as st
from requests import *
import json
from PIL import Image
from io import BytesIO
import base64

import gdown
from copy import copy

def download_url():
    
    gdown.download(id="1nK5HEjGc7z8Wfp72tCSTZm70AN8KF-g3", output="url.json")
    # gdown.download(id="1-7fXnBRgjZlydpT_7iG9e9e66vhN78nm", output="url.json")
    with open("url.json", "r") as bf:
        URL_json = json.load(bf)
        URL = URL_json["url"]
        return URL

URL = download_url()


# Tranfer img to base: 
# def convertImgToBase64_image(img):
#       return base64.encodebytes(img).decode('ascii')

def convertImgToBase64_image(image_file):
    data = base64.encodebytes(image_file.getvalue())
    return data


# Text/ Title
# st.title("helllo cu lì tutorial")
st.markdown("<h1 style='text-align: center;'>IMAGE SEARCH SYSTEM</h1>", unsafe_allow_html=True)
st.markdown("""
|Mentor   | Nguyễn Minh Trang  |
|:-------:|:------------------:|
| Mentees |Hà Sơn Tùng         |
|         |Nguyễn Văn Trực     |
|         |Phạm Ngọc Phương Linh |
|         |Nguyễn Chính Nghiệp |
"""
            
            , unsafe_allow_html=True)

st.write("Bắt đầu dowload")



# Text Input
name = st.text_input("Query for image", "Type here")
if st.button("Submit"):
    result = name
    st.success(result)
    r = post(url=f"{URL}/predit_query", data=json.dumps({'query': f"{result}"}))
    a = json.loads(r.text)
    for i in range (len(a["image"])):
        imgdata = base64.b64decode(a["image"][i])
        filename = BytesIO(imgdata)
        img = Image.open(filename)
        st.image(img, width=400, caption=f"Image {i}")
        st.write("\n")


def predict(image_file):
    values = {"file": (image_file.name, image_file, "jpg/png")}
    return values


 # upload file image
image_file = st.file_uploader("Upload Image for search image",type=['jpg'])

print("image_file >>>", image_file)

try:
    image_file_ = copy(image_file)
    image_file_ = Image.open(image_file_)
    st.image(image_file_, "Ảnh tải lên")
except: pass

# Search image
search_image_btn = st.button("Search with image")
if search_image_btn:
    predict_str = predict(image_file)
    print(URL+"/predict_image")
    r = post(url=f"{URL}/predict_image", files=predict_str)
    a = json.loads(r.text)
    for i in range (len(a["image"])):
        imgdata = base64.b64decode(a["image"][i])
        filename = BytesIO(imgdata)
        img = Image.open(filename)
        st.image(img, width=400, caption=f"Image {i}")
        st.write("\n")

st.write("-------------------------------------------------------")
st.markdown("<h3 style='text-align: center;'>IMAGE CAPTIONING </h1>", unsafe_allow_html=True)

image_file = st.file_uploader("Upload for image captioning",type=['jpg','png','JPEG'])

try:
    image_file_ = copy(image_file)
    image_file_ = Image.open(image_file_)
    st.image(image_file_, "Ảnh tải lên")
except: pass

option = st.selectbox(
     'Which model do you choose to create captions?',
     ('Oscar','ClipCap','Oscar_VN'))

image_caption_btn = st.button("Create captions")
if image_caption_btn:
    predict_str = predict(image_file)
    if option =='Oscar':
        r = post(url=f"{URL}/ic_oscar", files=predict_str)
        result_image = json.loads(r.text)
        st.success(result_image)

    elif option == 'ClipCap':
        r = post(url=f'{URL}/ic_clip/', files=predict_str)
        result_image = json.loads(r.text)
        st.success(result_image)

    elif option == 'Oscar_VN':
        r = post(url=f'{URL}/ic_oscarVN/', files=predict_str)
        result_image = json.loads(r.text)
        st.success(result_image)
