# Ferramenta de Gestão de Tempo
---

Conjunto de Scripts desenvolvidos por [Guilherme Arruda Pedroso](https://www.linkedin.com/in/guilherme-arruda-pedroso/) e [João Pedro Bomfim](https://www.linkedin.com/in/joão-pedro-bomfim-028018225/)

---
### Instalação
---

__1. Clonar Repositório__
```
git clone https://github.com/GuiArrP/FDG.git
```

__2. Criar Ambiente de Desenvolvimento e Instalar Dependências__

Windows ([conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html)):
```
conda create -n FDG python=3.12.3
conda activate FDG
python -m pip install --upgrade pip wheel
python -m pip install -r requirements.txt
python -m pip install --upgrade notebook traitlets
```

Linux:
```
$ python -m venv --clear --copies FDG
$ source FDG/bin/activate
(notebooks) $ python -m pip install --upgrade pip wheel
(notebooks) $ python -m pip install -r requirements.txt
(notebooks) $ python -m pip install --upgrade notebook traitlets
```

---
### Uso
---
