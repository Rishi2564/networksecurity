from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """This function will return the list of requirements"""
    requirements_lst:List[str]=[]
    try:
         with open("requirements.txt") as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                if requirements !='-e .':
                    requirements_lst.append(requirements)
         
    except FileNotFoundError:
        print("File not found")
    return requirements_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Rishabh Pradhan",
    author_email="rishabhpradhan2005@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)