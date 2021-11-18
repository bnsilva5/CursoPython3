from setuptools import setup, version

# Comando para crear un distribuible
# - python3 setup.py sdist
#
# Instalar paquete en python del sistema operativo
# - pip3 install paquete-0.1.tar.gz  (Linux)
#
# Listar paquetes con
# - pip3 list
#
# Desinstalar un paquete
# - pip3 unistall paquete-0.1.tar.gz

setup(
    name="paquete",
    version="0.1",
    description="Este es un paquete de ejemplo",
    author="Nicholas Silva Ruiz",
    author_email="nicholas@silva.ruiz",
    url="http://nicho.info",
    scripts=[],
    packages=["paquete", "paquete.adios", "paquete.hola"]
)