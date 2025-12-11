# VLM-high-resolution
## Clone env
conda create --name .venv-florence-2 --clone .venv
conda remove -n .venv-florence-2 --all

## Install torch
pip install numpy==1.26.4
pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124