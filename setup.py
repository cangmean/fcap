from setuptools import setup, find_packages

version = '0.1'

setup(
    name="flask-cap",
    version=version,
    packages=find_packages(),
    package_data={
        'flask_cap': ['templates/*']
    },
    include_package_data=True,
    author='cangmean',
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'cap = flask_cap.cli:main'
        ]
    }
)