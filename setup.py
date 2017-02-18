#!/usr/bin/env python3

from setuptools import setup
import os
import codecs
import re

#Copied from wheel package
here = os.path.abspath(os.path.dirname(__file__))
#README = codecs.open(os.path.join(here, 'README.txt'), encoding='utf8').read()
#CHANGES = codecs.open(os.path.join(here, 'CHANGES.txt'), encoding='utf8').read()

with codecs.open(os.path.join(os.path.dirname(__file__), 'tiledimage', '__init__.py'),
                 encoding='utf8') as version_file:
    metadata = dict(re.findall(r"""__([a-z]+)__ = "([^"]+)""", version_file.read()))

setup(name='TiledImage',
      version=metadata['version'],
      description='Tiled image handler',
      #long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        ],
      author='Masakazu Matsumoto',
      author_email='vitroid@gmail.com',
      url='https://github.com/vitroid/TiledImage/',
      keywords=['tiledimage',],
      license='MIT',
      packages=['tiledimage',
                ],
      install_requires=['numpy', 'pylru', ],
      entry_points = {
              'console_scripts': [
                  'pngs2 = tiledimage.pngs2:main',
                  '2pngs = tiledimage.2pngs:main'
              ]
          }
#      entry_points="""
#      [console_scripts]
#      genice = genice.__main__:main
#      """
      )

