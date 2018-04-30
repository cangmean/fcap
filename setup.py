from setuptools import setup, find_packages

version = '0.2'

setup(
    name="flask-cap",
    version=version,
    packages=find_packages(),
    include_package_data=True,
    author='cangmean',
    url='https://github.com/cangmean/flask-cap',
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'flask-cap = flask_cap.cli:main'
        ]
    }
)