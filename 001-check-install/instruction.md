# Learning to use pythong. Instalation health

### disclaimer:

This is a learning setup, The code in this folder was generated with AI. I'll try to make the use of AI as little as possible for my actual scripts

## Install tools

```bash

sudo dnf groupinstall "Development Tools" -y
sudo dnf install python3-devel python3-pip -y
sudo dnf install git -y

# pipx (crucial for modern tools
sudo dnf install pipx -y
pipx ensurepath

# QoL tools
# Jupyter Lab/Notebook (para experimentar interactivamente)
pipx install jupyterlab

# Formateador de código automático
pipx install black

# Organizador de imports
pipx install isort

# Linter (analizador de código estático)
pipx install flake8

# Gestor de entornos virtuales moderno
pipx install poetry
# o alternativamente:
pipx install uv  # (Más rápido, escrito en Rust)

```

## Creat a virtual environment

```bash
python3 -m venv .venv
```
Then activate the virtual environment

```bash
source .venv/bin/activate
```

## Crear scripts de configuración 

These are the "diagnostic.py" and "import_test.py" scripts in the folder

## Final checklist
```bash
echo "=== VERIFICACIÓN RÁPIDA ==="
python3 --version && echo "✅ Python instalado"
pip3 --version && echo "✅ pip funcionando"
which git && echo "✅ Git instalado"
pipx list 2>/dev/null && echo "✅ pipx configurado"
echo "=== LISTO ==="
```
