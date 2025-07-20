# Desktop-Assistant
The source code of my Window Desktop Assistant. All coded in python.

# Functionalities
- time demo

# Environment setup
```shell
conda create -n desktop-helper python=3.10 # python version is 3.10.16
conda activate desktop-helper # enter the env

# install necessary packages
pip install pyside6 # qt
pip install pyinstaller # to pack the proj into exe
```

# Usage
## Testing
```shell
python src/main.py
```

## Packing into executable program
```shell
pyinstaller --noconfirm --windowed --name DesktopHelper src/main.py
```
