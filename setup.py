# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name='flask_platform',
    version='0.1.0',
    description='Part of assessment 2 for comp30670',
    long_description=readme,
    author='Martin Casey',
    author_email='martin.casey@ucdconnect.ie',
    url='https://github.com/MartinC20xx/flask_platform',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    #include_package_data=True, 
    zip_safe=False,
    install_requires=['Flask'],
    
    #entry_points={
          #"console_scripts":['comp30670_flask_platform=flask_platform:app.py']})

    )
