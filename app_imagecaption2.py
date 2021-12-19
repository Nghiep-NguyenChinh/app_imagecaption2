
import streamlit as st
import  os
# import requests
# Import libraries
# sys.path.append("app_imagecaption_")

import gdown
# data flick30k
url_data = "https://drive.google.com/uc?id=1h4Aa2zqOZu7XPdg-pWW5KmHLxqbvs1jn"
output_data = "flickr30k.zip"

# predict_flicrk30k
url_json = "https://drive.google.com/uc?id=1h4Aa2zqOZu7XPdg-pWW5KmHLxqbvs1jn"
root = "predict_flicrk30k.json"

url_search_sys =  "https://drive.google.com/uc?id=16gUqEan81aq2SY4Se4wBX3d6WRZ9KSjn"
search_sys ="Search_Sys.zip"

#########################################################
##### GIAO DIỆN
#########################################################
#st.title("**OBJECT DETECTION**")
st.markdown("<h1 style='text-align: center;'>IMAGE CAPTIONING</h1>", unsafe_allow_html=True)
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

def download_data(url, output):      
    if (os.path.exists(output)==False):
        gdown.download(url, output, quiet=False)
#tai data_flick30k.zip
download_data(url_data, output_data)
download_data(url_json, root)
download_data(url_search_sys, search_sys)

# import zipfile
# with zipfile.ZipFile("flickr30k.zip", 'r') as zip_ref:
#     zip_ref.extractall("image_data")

import zipfile
with zipfile.ZipFile(search_sys, 'r') as zip_ref:
    zip_ref.extractall()
#folder_sys
save_ix = "Search_Sys"


os.system("pwd")
st.write(os.listdir("image_data/flickr30k_images"))
st.write("đã giải nén")


option = st.selectbox('Chọn model',('CLIP_', 'Yolov4'))
#st.write('You selected:', option)

##################################################################

#################
#### MAIN
################
img_l = st.file_uploader("Upload Image",type=['jpg'])


button = st.button("Bắt đầu tạo caption")

