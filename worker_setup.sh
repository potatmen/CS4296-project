sudo apt-get update
sudo apt-get install python3-pip
sudo apt install python3.12-venv
python3 -m venv env
source env/bin/activate
pip install flask 
python3 worker.py
