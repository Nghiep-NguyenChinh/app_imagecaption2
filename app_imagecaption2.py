https://drive.google.com/uc?id=1h4Aa2zqOZu7XPdg-pWW5KmHLxqbvs1jn
import streamlit as st
import  os
# import requests
# Import libraries
# sys.path.append("app_imagecaption_")

import gdown

url = "https://drive.google.com/uc?id=1-bKUmsoKXAhr-wvlaXqaQxBhEte0fUsB"
output = "model_weights.pt"




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
#Ham tải về
##  Kiểm tra file 'name' có tồn tại chưa || không thì kéo nội dung từ link url tạo thành name 
##
def download(url, output):      
    if (os.path.exists(output)==False):
        #st.write("Đang lấy file %s..." % name)
        gdown.download(url, output, quiet=False)


#st.write("Đang lấy file weights...")
download(url, output)

import clip_pre
st.write("Trạng thái: Sẵn sàng")


option = st.selectbox('Chọn model',('CLIP_', 'Yolov4'))
#st.write('You selected:', option)

##################################################################

#################
#### MAIN
################
img_l = st.file_uploader("Upload Image",type=['jpg'])


button = st.button("Bắt đầu tạo caption")
if button:
    clip_pre.upload_image(img_l)
