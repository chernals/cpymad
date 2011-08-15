#!/usr/bin/python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sourcefiles=["madx.pyx"] # this can be a list of both c and pyx source files..
pythonsrc=["cpymad","cpymad.models","jpymad","jpymad.tools" "pymad"] # list of python modules to include
data=['models/*.json'] # list of data files to include..
libs=['madx', "X11", "z", "pthread", "c", "stdc++"]
includedirs=['/usr/local/include/madX',
             '/usr/include/madX',
             '/afs/cern.ch/user/y/ylevinse/.local/include']

madmodule=Extension('madx',
                    define_macros = [('MAJOR_VERSION', '0'),
                                     ('MINOR_VERSION', '1')],
                    include_dirs = includedirs,
                    libraries = libs,
                    sources = sourcefiles
                    )

setup(
    name='PyMAD',
    version='0.1',
    description='Interface to Mad-X, using Cython or Py4J through JMAD',
    cmdclass = {'build_ext': build_ext},
    ext_modules = [madmodule],
    author='PyMAD developers',
    author_email='pymad@cern.ch',
    license = 'CERN Standard Copyright License',
    requires=['Cython','numpy','Py4J'],
    packages = pythonsrc,
    package_data={'cpymad': data},
    )