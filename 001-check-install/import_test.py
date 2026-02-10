#!/usr/bin/env python3
"""
Script de prueba que importa varios módulos comunes.
Si este script funciona, tu instalación está correcta.
"""

try:
    import sys
    import os
    import json
    import datetime
    import pathlib
    import subprocess
    
    print("✅ Módulos estándar importados correctamente")
    
    # Intentar importar un módulo de terceros (requests)
    try:
        import requests
        print("✅ requests instalado correctamente")
    except ImportError:
        print("⚠️  requests no está instalado (puedes instalarlo luego)")
        print("   Comando: pip install requests")
    
    # Crear un pequeño script funcional
    print(f"\n📁 Directorio actual: {pathlib.Path.cwd()}")
    print(f"🕐 Fecha y hora: {datetime.datetime.now()}")
    
    # Usar subprocess para llamar a un comando de sistema
    resultado = subprocess.run(
        ["echo", "¡Python está funcionando en Fedora!"],
        capture_output=True,
        text=True
    )
    print(f"🔧 Subprocess funcionando: {resultado.stdout.strip()}")
    
    # Crear un pequeño archivo JSON
    datos = {
        "sistema": "Fedora Linux",
        "python_version": sys.version.split()[0],
        "prueba_exitosa": True,
        "fecha": str(datetime.date.today())
    }
    
    with open("prueba.json", "w") as f:
        json.dump(datos, f, indent=2)
    
    print("📄 Archivo 'prueba.json' creado con éxito")
    print("\n🎉 ¡Todo funciona perfectamente! Puedes empezar a programar.")
    
except Exception as e:
    print(f"❌ Error encontrado: {e}")
    print("\n💡 Revisa la instalación o comparte este error para ayuda.")
