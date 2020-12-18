#!/usr/bin/env python
from setuptools import setup
    
setup(name='munexus',
      version='0.1',
      description='A Python hack for the nexus python API that does read ISIS muon data.',
      author='Roberto De Renzi',
      author_email='roberto.derenzi@unipr.it',
      url='https://github.com/RDeRenzi/munexus',
      packages=['munxs',
                'napy.py',
                'tree.py',
                'unit.py',
                ],
      include_package_data=True,
      package_dir={'munxs': 'munxs' },
      install_requires=[
            'numpy >= 1.6',
      ],
      long_description='A Python hack for the nexus python API that does read ISIS muon data\nby fixing some bytes - string conversion\nand two other python3 issues.\nIt does not fix all.\nWorking methods:\nNeXusTree(filename,'r')\ngetgrouppath(bytes(path))\nreadpath(bytes(path))'
      license = 'MIT',
      classifiers=[
            'Development Status :: 1 - Beta',
            'Intended Audience :: Users',
            'Topic :: Physics',
            'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
],
      install_requires=['numpy,libnexus.so'],
)
