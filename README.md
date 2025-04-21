# Dash Python Explore
---

Set of Scripts developed by [Guilherme Arruda Pedroso](https://www.linkedin.com/in/guilherme-arruda-pedroso/)

---
### Installation
---

__1. Clone Repository__
```
git clone https://github.com/GuiArrP/Python-Dashboard
```

__2. Create Development Environment and Install Dependencies__

Windows ([conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)):
```
conda create -n pythondash python=3.12.3
conda activate FDG
python -m pip install --upgrade pip wheel
python -m pip install -r requirements.txt
python -m pip install --upgrade notebook traitlets
```

Linux:
```
$ python -m venv --clear --copies pythondash
$ source pythondash/bin/activate
(notebooks) $ python -m pip install --upgrade pip wheel
(notebooks) $ python -m pip install -r requirements.txt
(notebooks) $ python -m pip install --upgrade notebook traitlets
```

---
### Description

 - color_map: a simple map where the main objective is to color regions and states according to the current selection.
---
