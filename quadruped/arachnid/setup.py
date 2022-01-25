
"""motion package setup"""

import setuptools

setuptools.setup(name='arachnid',
    version='0.1',
    description='Robotic arachnid',
    url='#',
    author='brogrammer',
    install_requires=['numpy', 'robotics'],
    author_email='',
    packages=setuptools.find_packages(exclude=['test']),
    zip_safe=False)
