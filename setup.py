from setuptools import find_packages,setup
from typing import list

HYPHEN_E_DOT = '-e'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will returns the 
    list of get_requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name='MLProject',
    version='0.0.1',
    author='Pratik',
    author_email='pratikdevkota200@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)