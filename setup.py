from setuptools import setup

from my_pip_package import __version__

setup(
    name='utils(1).py',
    version=__version__,

    #url='https://github.com/MichaelKim0407/tutorial-pip-package',
    url = 'https://github.com/VinodVasan/vinod'
    author='Vinod Vasan',
    author_email='vinodvsn03@gmail.com',

    py_modules=['utils'],
)
