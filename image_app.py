import streamlit as st
# we use streamlit to build web apps using Python(code),
#          - Create buttons, text boxes, sliders,
#          - Upload and display images/files,
# import streamlit<package/library> as st<alias/petname>
# if we didnt install the package, we get module not found error
# we can install the package in terminal using:
                                   # python -m pip install streamlit 
# save file and run 
# run a python file i.e .py  : 
                            #  python filename.py ( check for every package similarway)
# run a streamlit app :
# to see the app,syntax:
                         # python -m streamlit run <filename.py>
from dotenv import load_dotenv
# dotenv is the module in python-dotenv package(or library)
# install python-dotenv package in terminal using:
                                                   # python -m pip install python-dotenv 
# from dotenv<module> import load_dotenv<function>
# searches for dotenv file and loads environment variable from dotenv file
import os
# import os ,os is inbuilt python module(acess files and directories,environment variables)
# here we access the environment variables
from PIL import Image
# PIL(python image library)is the module in Pillow package
# pillow is updated version of PIL, it is used to open and manipulate images in python
# install Pillow package using:
                               # python -m pip install Pillow 
from google import genai
# genai is the module in google-genai package
# google-genai is the package provided by google to access genai models
# install google-genai package using:
                                 # python -m pip install google-genai
load_dotenv() # load environment variables from .env file
api_key=os.getenv("API_KEY") # access the environment variable API_KEY and store it in api_key variable
                             # to check if envronment variable is loadded successfully,run the file
                            # syntax: python filename.py (file should be in same directory as .env file)
file=st.file_uploader("upload an image",
                      type=["jpg","png"]) # st.file_uploader() is a streamlit function that creates a file uploader in the app
                                        # ulpload an image file of type jpg or png and store the file in file variable

if file is not None: # check if file is uploaded, if file is not None means file is uploaded
    st.image(Image.open(file)) # st.image() is a streamlit function that displays an image in the app
                               # open the uploaded file using Image.open() and display the image in the app
                             # Image.open() is a function in PIL that opens and identifies the given image file and returns an image object
    
prompt=st.text_input("enter the prompt") # st.text_input() is a streamlit function that creates a text input box in the app

if st.button("generate content"): # st.button() is a streamlit function that creates a button in the app, when the button is clicked it returns True
    client=genai.Client(api_key=api_key) # create a client object of genai.Client class and pass the api_key as an argument to access the genai models
    img=Image.open(file) # open the uploaded file using Image.open() and store the image object in img variable
    Input=[img,prompt] # create a list of image object and prompt and store it in Input variable
    response=client.models.generate_content(model='gemini-2.5-flash'
                                            ,contents=Input) 
     # call the generate_content() method of client.models and pass the model name and contents as arguments to generate content using the genai model and store the response in response variable        
    st.success(response.text) # st.success() is a streamlit function that displays a success message in the app, here we display the generated content from the response variable in the app
    
