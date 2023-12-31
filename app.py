import gradio as gr
from huggingface_hub import from_pretrained_keras
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input

import numpy as np

model = from_pretrained_keras("yusyel/fishv2")


CLASS=["Black Sea Sprat",
 "Gilt-Head Bream",
 "Hourse Mackerel",
 "Red Mullet",
 "Red Sea Bream",
 "Sea Bass",
 "Shrimp",
 "Striped Red Mullet",
 "Trout"]


def preprocess_image(img):
    img = load_img(img, target_size=(224, 224, 3))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    print(img.shape)
    return img



def predict(img):
    img = preprocess_image(img)
    pred = model.predict(img)
    pred = np.squeeze(pred).astype(float)
    print(pred)
    return dict(zip(CLASS, pred))


demo = gr.Interface(
    fn=predict,
    inputs=[gr.inputs.Image(type="filepath")],
    outputs=gr.outputs.Label(),
    examples=[
        ["./img/Black_Sea_Sprat.png"],
        ["./img/Gilt_Head_Bream.JPG"],
        ["./img/Horse_Mackerel.png"],
        ["./img/Red_mullet.png"],
        ["./img/Red_Sea_Bream.JPG"],
        ["./img/Sea_Bass.JPG"],
        ["./img/Shrimp.png"],
        ["./img/Striped_Red_Mullet.png"],
        ["./img/Trout.png"],
    ],
    title="fish classification",
)
demo.launch(server_name="0.0.0.0", server_port=7860)
