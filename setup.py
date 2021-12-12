from setuptools import setup, find_packages
import codecs
import os

with open("README.md") as f:
    long_description = f.read()

VERSION = '1.0'
DESCRIPTION = 'Important Packages for Machine Learning. \n Installed in a \'One Click\' '

# Setting up
setup(
    name="CE_AI_D002",
    version=1.0,
    author="pateldarshan098",
    author_email="dvpatelahmedabad@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['spyder', 'pandas', 'numpy', 'statsmodels', 'scipy', 'xgboost', 'matplotlib', 'seaborn', 
                      'scikit-learn',  'pyforest', 'pycaret', 'Flask', 'fastapi',
                      'jupyter', 'imbalanced-learn', 'bokeh', 'kat',
                      'Boruta', 'mlxtend','tensorflow-cpu==2.6.0', 'tensorflow-gpu==2.6.0', 'lightgbm', 'catboost'],
    keywords=['CE_AI_D001', 'Machine Learning in a single file', 'AI', 'ML', 'Machine Learning'],
    url='http://github.com/DeepGajera1012',
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    platforms=["any"],
    zip_safe=True,
)
