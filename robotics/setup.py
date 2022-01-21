
"""motion package setup"""

import setuptools

setuptools.setup(name='robotics',
    version='0.1',
    description='Robotics',
    url='#',
    author='brogrammer',
    install_requires=['numpy'],
    author_email='',
    packages=setuptools.find_packages(exclude=['test']),
    zip_safe=False)
