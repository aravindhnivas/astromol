from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='astromol',
    packages=find_packages(),
    package_data={'astromol' : ['bibtex/*.bib']},
    install_requires=[
        'bibtexparser',
        'numpy',
        'rdkit-pypi',
        'matplotlib',
        'colour',
        'seaborn',
        'scipy',
        'datetime',
        'python-pptx',
        'periodictable',
    ],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    version='2021.7.0',
    description='A Database of Molecules Detected in Space',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Brett A. McGuire (Department of Chemistry, Massachusetts Institute of Technology)',
    license='MIT',
)