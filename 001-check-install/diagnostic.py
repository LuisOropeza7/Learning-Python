#!/usr/bin/env python3
"""
Script de diagnóstico para verificar la instalación de Python.
"""

import sys
import platform
import subprocess
import os

print("=" * 50)
print("DIAGNÓSTICO DE INSTALACIÓN PYTHON")
print("=" * 50)

# 1. Información básica
print(f"\n1. Sistema Operativo: {platform.system()} {platform.release()}")
print(f"2. Distribución: Fedora (detectado por entorno)")

# 2. Versiones de Python
print(f"\n3. Versión de Python: {sys.version}")
print(f"4. Ruta del ejecutable: {sys.executable}")

# 3. Verificar comandos del sistema
print("\n5. Herramientas del sistema:")
herramientas = ["git", "python3", "pip3", "pipx"]
for herramienta in herramientas:
    try:
        resultado = subprocess.run(
            ["which", herramienta],
            capture_output=True,
            text=True
        )
        estado = "✓ INSTALADO" if resultado.returncode == 0 else "✗ NO ENCONTRADO"
        print(f"   - {herramienta}: {estado}")
    except:
        print(f"   - {herramienta}: ✗ ERROR AL VERIFICAR")

# 4. Verificar módulos de Python importantes
print("\n6. Módulos de Python instalados:")
modulos = ["pip", "setuptools", "venv", "requests", "numpy"]
for modulo in modulos:
    try:
        __import__(modulo)
        print(f"   - {modulo}: ✓ DISPONIBLE")
    except ImportError:
        print(f"   - {modulo}: ✗ NO DISPONIBLE")

# 5. Variables de entorno
print("\n7. Variables de entorno importantes:")
env_vars = ["PATH", "VIRTUAL_ENV", "PYTHONPATH"]
for var in env_vars:
    valor = os.environ.get(var, "No definida")
    print(f"   - {var}: {valor[:80]}{'...' if len(valor) > 80 else ''}")

# 6. Espacio en disco
print("\n8. Espacio en disco (directorio actual):")
try:
    resultado = subprocess.run(
        ["df", "-h", "."],
        capture_output=True,
        text=True
    )
    lineas = resultado.stdout.strip().split('\n')
    if len(lineas) > 1:
        print(f"   {lineas[1]}")
except:
    print("   No se pudo verificar el espacio")

print("\n" + "=" * 50)
print("DIAGNÓSTICO COMPLETADO")
print("=" * 50)

print("\nRECOMENDACIONES:")
if "VIRTUAL_ENV" not in os.environ:
    print("  - No estás en un entorno virtual. Considera crear uno con:")
    print("    python3 -m venv .venv")
    print("    source .venv/bin/activate")
else:
    print(f"  - Estás en entorno virtual: {os.environ.get('VIRTUAL_ENV')}")

print("\n  - Para tu primer proyecto, ejecuta:")
print("    mkdir ~/proyecto_python && cd ~/proyecto_python")
print("    python3 -m venv .venv")
print("    source .venv/bin/activate")
print("    pip install requests  # Para probar instalación de paquetes")
