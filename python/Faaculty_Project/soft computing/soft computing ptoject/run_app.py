import os
import subprocess
current_dir = os.path.dirname(os.path.abspath(__file__))
path_gui = os.path.join(current_dir, "gui.py")
command = f"streamlit run \"{path_gui}\""
subprocess.run(command, shell=True)
