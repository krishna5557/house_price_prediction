from setuptools import setup,find_packages
from typing import list




def get_requirements_list()->list[str]:
    """
    description:  This function is going to return requirements from 
    requirements.txt file

    return: This function returns list in string format
    
    """
    with open("requirements.txt") as requirements_file:
        return requirements_file.readlines().pop("-e .")
    

setup(
        name="Housing-Predictor",
        version="0.0.2",
        author="Krishnakanth",
        description="this is the 1st machine learning project",
        packages=find_packages(),
        install_requires=get_requirements_list()
      )




