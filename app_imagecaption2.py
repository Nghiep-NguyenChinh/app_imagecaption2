
import streamlit as st
import  os
import search_system
# import requests
# Import libraries
# sys.path.append("app_imagecaption_")

import gdown
# data flick30k
# url_data = "https://drive.google.com/uc?id=1KQOWoQAq9cvKKurhC00zqGfTfLFtIUw2"
url_data = "https://drive.google.com/uc?id=136_IKI3j8AqdTs2G2JgT8fg-ezTM9eZi"
output_data = "flickr30k.zip"

# predict_flicrk30k
url_json = "https://drive.google.com/uc?id=1175qCLlLyI5pC0iXUrltAdqfMR0AvCkF"
root = "predict_flicrk30k.json"

url_search_sys =  "https://drive.google.com/uc?id=16gUqEan81aq2SY4Se4wBX3d6WRZ9KSjn"
search_sys ="Search_Sys.zip"


# import wget
# url_data = "https://public.boxcloud.com/d/1/b1!JMCSfCZ4dOsyNQ4u3nka075n7AA0iDmvyveKgNMzb0OG6iqPj9MBsaa2Q1BpB_u-sTy4gnhhExo-7MjqmloUTtbQajsUDReiWhNpLxg5W4lk7da0AhJmCt1IxnEgWxqVUYfEeU715j8CUqUR0eQlmbyzVjZJppunzOuaYoOQ5WFM3YKSXCGC6Avk1ugbD-Gc3ImK0i2i-_iEeTH0TqzJeb6d9Z3movyNbEIBI42dwIun430879H7LnpIT9NkatvPcz2Qd1JeOPDzTmWbAw4BPUhxYml_-v2gSVijMZOAoE7P0z-SkT854L2wpk9gdGbRxE0Z2ohGPl1lrfdB4IM1wUmGX53VD-72SZPHOq7OTl-u1crD5UKqy_MtQ8SS1D14_CM3ieeqZ09uxKVgKWRDnpQrtmPepO6iNSYMKU0VNLq0ayTbfSPV26-Pnv9IBXn8T30YTYoxpUM8zwzcpT6ehUDBxSq8aYG_jV8NTfHABDMoFlk_03X70XWjC3JJQVms-G5DjXYlxE6u2hmN5eTx1pL-bqsBNP2o4-xtW88a_Rt1dcuewOUQNxeF1R06KI-X99Fgjr0q_JUN7-kGyaIen8Q1EJPRnqT563cJ2BD4wZ557dcTr2_CjAS0SilrNAjx2070R32fXDgIg714dqWrGXxkySH5yxrDNCvSUtXc_oEntkmGiSWUx2FmqawYfu1YnFz2nc7KkfBH8HKtpgPXje5TPUuzyvlt9M-NQSWcCQaB1pMy2o48BRtHSqCKgjHCeZJExdhim6JTdG5NLHgA5-RnRBZj_U8Dw53Sx9qTUIZpWge1EckUQPXs4mVRdJtIvuSBKq42c8N8pgK6RECz5ZLcpH1eLcFeHrdIcrKirl0aXarqBSF7rl-sDtglfX2d-fQcREIdYKXoULGOJd19BpZboXoWiCPtYwkBd3uIQUcBwVEiT6nb_L95HDsr4uEeN3gduupo9R4XnI08I5503WcWO2Q31a_xRQLil9hxALjlPeDPFinC0R3FYN_ZS9ooPdRrFLex817fPk7sJfq54TumERT22PKVcaaCx3lEU2-ERMZMSm0CAV5_8XTD5s6a2va2MZmdA6g9QAfbaAc_hk6s0VHQ35jQfJBf1qf5MHRlXkg7GX4BHIAkbSNV7K7WJ_MH1oARdeJLK64JDi3P_6fulFHSzIgSWR2bVIZiZ6g6Qv7mqSF2BLJ08BBlANDWtDXhNLeiapn1MzPkpr4kNix0bHuNySp_SZzQWI4zK0To7v7QoXQW82g33bvgeBWdfP-dBECxsxzMILQXR0JV0TW0ZfQ8SP8tLoQP6VKiQUoov2k6G--r9PNjMSQzrxH8o8Dythhd/download"
# output_data = "flickr30k-images.tar.gz"

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

def download_data_2(url, output):      
    if (os.path.exists(output)==False):
        wget.download(url)
#tai data_flick30k.zip
download_data(url_data, output_data)
# download_data_2(url_data, output_data)
download_data(url_json, root)
download_data(url_search_sys, search_sys)



import zipfile
with zipfile.ZipFile(output_data) as zip_ref:
    zip_ref.extractall()


with zipfile.ZipFile(search_sys, 'r') as zip_ref:
    zip_ref.extractall()
#folder_sys
save_ix = "Search_Sys"


os.system("pwd")
st.write(os.listdir("Flickr30k"))
st.write("đã giải nén")


option = st.selectbox('Chọn model',('CLIP_', 'Yolov4'))
#st.write('You selected:', option)

##################################################################

#################
#### MAIN
################
# img_l = st.file_uploader("Upload Image",type=['jpg'])


button = st.button("Bắt đầu tạo caption")
if button:
    search_system.main("baby car")    
