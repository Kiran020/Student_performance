from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='Student_performance',  # Replace with your package name
    version='0.1',
    author='kiran',
    author_email='herodekiran123@gmail.com',
    packages=find_packages(),  # Automatically discover packages in the directory
    install_requires=get_requirements('requirements.txt'),  # Pass the file path of requirements.txt
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify minimum Python version
)
