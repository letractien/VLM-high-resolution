# VLM-high-resolution
## Check 

## Config github
git config --global user.name "Tiến Lê"
git config --global user.email "ww.hacker01@gmail.com"

## Clone env
conda create --name .venv-florence-2 --clone .venv
conda create --name .venv-sam3 --clone .venv
conda create --name .venv-molmo --clone .venv
conda create --name .venv-idefics2 --clone .venv
conda activate .venv-idefics2

## Install torch + other library
pip install yt-dlp
pip install dotenv
pip install bitsandbytes
pip install numpy==1.26.4
pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124
pip install flash-attn===1.0.4 --no-build-isolation
pip install huggingface_hub==0.36.0
pip install transformers==4.51.3