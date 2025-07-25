from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
def get_requiremnts(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        #the replace is requiments.txt consists text in line by one , we combine with spaces(" ")
        requirements = [req.replace("\n", " ") for req in requirements] 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
setup(
    name = "ml_project",
    version=  "0.0.1",
    author = "Sridhar Goudu",
    description = "A simple ML model package",
    packages = find_packages(),
    install_requires = [
        "numpy",
        "pandas",
        "seaborn",
        "scikit-learn"
    ],
)