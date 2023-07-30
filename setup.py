from setuptools import setup, find_packages

setup(
    name="diffdock_pip",
    version="0.1",
    author="Giacomo Corso",
    author_email="author@domain.com", 
    description="Description of the DiffDock project",
    url="https://github.com/johnyang101/diffdockpackage",
    packages=find_packages(),
    # install_requires=[
    #     'numpy',
    #     'torch',
    #     'torch-geometric',
    #     'matplotlib',
    #     # Add other dependencies as per the environment.yml
    # ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
