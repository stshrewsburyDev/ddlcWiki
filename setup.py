from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as README_file:
    long_description = README_file.read()

setup(
    name='ddlcWiki',
    version='1.0',
    description='DDLC wiki Python 3 module. (Doki doki literature club wiki)',
    license="MIT",
    long_description=long_description,
    author='stshrewsburyDev',
    author_email='',
    url="https://github.com/stshrewsburyDev/ddlcWiki",
    packages=find_packages(),
    install_requires=[]
)
