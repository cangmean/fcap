from setuptools import setup, find_packages

version = '0.2'

setup(
    name="fcap",
    version=version,
    packages=find_packages(),
    include_package_data=True,
    author='cangmean',
    url='https://github.com/cangmean/fcap',
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'fcap = fcap.cli:main'
        ]
    }
)