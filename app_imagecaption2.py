
import streamlit as st
import  os
# import requests
# Import libraries
# sys.path.append("app_imagecaption_")

import gdown
# data flick30k
url_data = "https://drive.google.com/uc?id=1h4Aa2zqOZu7XPdg-pWW5KmHLxqbvs1jn"
output_data = "flickr30k.zip"




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
#os.system("unzip flickr30k.zip -d image_data")
os.system("pwd")
st.write(os.listdir())
st.write("đã giải nén")


option = st.selectbox('Chọn model',('CLIP_', 'Yolov4'))
#st.write('You selected:', option)

##################################################################

#################
#### MAIN
################
img_l = st.file_uploader("Upload Image",type=['jpg'])


button = st.button("Bắt đầu tạo caption")

