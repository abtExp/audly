import numpy as np
import gradio as gr

def print_name(fl):
    print(fl[0])
    print(np.unique(fl[1]))
    print('Hi')
    return fl, fl

demo = gr.Interface(
    fn = print_name,
    inputs=['audio'],
    outputs=[gr.Audio(label="drums"), gr.Audio(label="vocals")],
    title='Audio Source Separation',
    description='Audio Source Separation Demo' 
)

demo.launch()