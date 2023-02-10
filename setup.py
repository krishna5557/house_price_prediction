from setuptools import setup,find_packages
from typing import List



def get_requirements_list()->List[str]:
    """
    description:  This function is going to return requirements from 
    requirements.txt file

    return: This function returns list in string format
    
    """
    with open("requirements.txt") as re:
        return re.readlines()
    

setup(
        name="Housing-Predictor",
        version="0.0.1",
        author="Krishnakanth",
        description="this is the 1st machine learning project",
        packages=find_packages(),
        install_requires=get_requirements_list()
      )




