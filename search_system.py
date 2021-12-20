import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
import sys
import json
# from IPython import display
import base64
import streamlit as st

def createSearchableData(root, save_ix=None):
    '''
    Schema definition: title(name of file), path(as ID), content(indexed
    but not stored),textdata (stored text content)
    '''
    schema = Schema(imgID=TEXT(stored=True), content=TEXT, textdata=TEXT(stored=True))
    indexdir = "indexdir"
    if save_ix is not None:
        assert os.path.isdir(save_ix)
        indexdir = os.path.join(save_ix, indexdir)
    if not os.path.exists(indexdir):
        os.mkdir(indexdir)
 
    # Creating a index writer to add document as per schema
    ix = create_in(indexdir, schema)
    writer = ix.writer()
 
    assert os.path.isfile(root)
    cap_file = open(root, "r")
    caption_file = json.load(cap_file)
    print('Indexing ', root)
    for cap in caption_file:
        imgID = cap["image_id"]
        caption_text = cap["caption"]
        writer.add_document(imgID=imgID, content=caption_text, textdata=caption_text)
    print("Indexing finished!")
    writer.commit()
       
    
def append_to_html(query, urls, scores):
  """Display a text query and the top result videos and scores."""
  html = ''
  html += '<h2>Input query: <i>{}</i> </h2><div>'.format(query)
  html += 'Results: <div>'
  html += '<table><tr>'
  for idx, score in enumerate(scores):
    html += '<th>Rank #{}, Score:{:.2f}</th>'.format(idx+1, score)
  html += '</tr><tr>'
  for i, url in enumerate(urls):
    html += '<td>'
    data_uri = base64.b64encode(open(url, 'rb').read()).decode('utf-8')
    html += '<img src="data:image/png;base64,{0}" height="224">'.format(data_uri)
    html += '</td>'
  html += '</tr></table></div></div>'
  return html
  
  

import time
indexdir = os.path.join(save_ix, "indexdir")
ix = open_dir(indexdir)
img_dir = "Flickr30k/flickr30k_images"
def main(query_str):
    # query_str is query string
    
    query_str = query_str.replace(' ', ' OR ')
    # Top 'n' documents as result
    topN = int(10)
    st = time.time() 
    with ix.searcher(weighting=scoring.PL2) as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query,limit=topN)
        st.write(len(results))
        urls = []
        scores = []
        for i in range(min(topN, len(results))):
          urls.append(os.path.join(img_dir, results[i]['imgID']+'.jpg'))
          scores.append(results[i].score)
        html = append_to_html(query_str, urls, scores)
    st.write(time.time()-st)


#     display.HTML(html)
    st.write(html)
