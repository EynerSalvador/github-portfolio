# setup.py
from setuptools import setup, find_packages

setup(
    name="github-portfolio",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask==3.0.2",
        "flask-sqlalchemy==3.1.1"
    ],
)
