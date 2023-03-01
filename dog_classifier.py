# create an app to classify dogs

# to run the app - `streamlit run dog_classifier.py`

from fastai.vision.widgets import *
from fastai.vision.all import *

# fast.ai—Making neural nets uncool again

from pathlib import Path

import streamlit as st

class Predict:
    def __init__(self, filename):
        self.learn_inference = load_learner(Path()/filename)
        self.img = self.get_image_from_upload()
        if self.img is not None:
            self.display_output()
            self.get_prediction()
    
    @staticmethod
    def get_image_from_upload():
        
    # get_image_from_upload : Allow us to upload images from your local files
    
        uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg', 'jpg'])
        if uploaded_file is not None:
            return PILImage.create((uploaded_file))
        return None

    def display_output(self):
        
        # display_output : Display the image after uploading it
        
        st.image(self.img.to_thumb(500,500), caption='Uploaded Image')

    def get_prediction(self):
        
        # get_prediction : Create a button to classify the image


        if st.button('Classify'):
            pred, pred_idx, probs = self.learn_inference.predict(self.img)
            st.write(f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}')
        else: 
            st.write(f'Click the button to classify') 

if __name__=='__main__':

    file_name='dog.pkl'

    predictor = Predict(file_name)
### Yeeeep)))
