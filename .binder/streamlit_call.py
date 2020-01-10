from subprocess import Popen
import os

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    os.chdir('awesome-streamlit/gallery/bokeh_experiments')
    Popen(["streamlit", "run", "bokeh_experiments.py", "--browser.serverAddress=0.0.0.0", "--browser.gatherUsageStats=False", "--server.enableCORS=False"])
