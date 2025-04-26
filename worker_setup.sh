mkdir worker_dir
cd worker_dir
sudo apt-get update
sudo apt install -y python3.12-venv python3-full
python3 -m venv env
env/bin/pip install flask 
git clone https://github.com/potatmen/CS4296-project.git
env/bin/python3 CS4296-project/worker.py
