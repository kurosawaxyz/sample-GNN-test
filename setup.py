# install_deps.py
import torch
import subprocess
import sys

torch_version = torch.__version__.split('+')[0]
cuda_tag = torch.version.cuda
cuda_str = f"+cu{cuda_tag.replace('.', '')}" if cuda_tag else "+cpu"

url = f"https://data.pyg.org/whl/torch-{torch_version}{cuda_str}.html"

# Install basic deps
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Install PyG deps with correct wheels
subprocess.run([sys.executable, "-m", "pip", "install", "torch-scatter", "-f", url])
subprocess.run([sys.executable, "-m", "pip", "install", "torch-sparse", "-f", url])
subprocess.run([sys.executable, "-m", "pip", "install", "git+https://github.com/pyg-team/pytorch_geometric.git"])
