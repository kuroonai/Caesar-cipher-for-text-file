from setuptools import setup

setup(
   name='kcc',
   version='1.0',
   description="Kuroonai's Caesar cipher for text file"
   author='Naveen Vasudevan',
   author_email='naveenovan@gmail.com',
   packages=['kcc'],  #same as name
   install_requires=['PySimpleGUI'], #external packages as dependencies
)