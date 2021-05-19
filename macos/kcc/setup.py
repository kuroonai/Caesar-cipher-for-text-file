from setuptools import setup

APP=['kcc.py']
OPTIONS={'argv_emulation':True,'iconfile':'/Users/kuroonai/Downloads/macos/kcc.icns'}
setup(
   name='kcc',
   version='1.0',
   description="Kuroonai's Caesar cipher for text file",
   author='Naveen Vasudevan',
   author_email='naveenovan@gmail.com',
   packages=['kcc'],  #same as name
   install_requires=['PySimpleGUI'], #external packages as dependencies
   app=APP,
   options={'py2app':OPTIONS},
   setup_requires=['py2app']
)