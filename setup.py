from setuptools import setup,find_packages
setup(
    name = 'mypackage',
    version = '0.1', 
    packages= find_packages(exclude=['tests*']),
    description ='EDSA example' ,
    licence = 'MIT',
    long_description = open('README.md').read(), 
    author= 'Nditsheni',
    author_email= '', 
    url= 'https://github.com/<username>/<package-name>', 
    install_requires = 'numpy'
      
    
)