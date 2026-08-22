from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path: str)-> List[str]:
    with open(file_path) as obj:
        requirements = obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='credit_card_fraud_detection_project',
    version= '0.0.1',
    author='namitha9eshan',
    author_email='namithaeshanpethiyagoda@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
)