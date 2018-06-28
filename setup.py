from setuptools import setup, find_packages
import fcap

version = fcap.__version__
author = fcap.__author__

setup(
    name="fcap",
    version=version,
    packages=find_packages(),
    include_package_data=True,
    author=author,
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