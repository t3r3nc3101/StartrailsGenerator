curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install opencv-python
pip install imageio

del get-pip.py

echo "DEPENDENCIES INSTALLED!"
pause