from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
  name = 'numpy_to_image',
  ext_modules = cythonize("numpy_to_image.pyx"),
  include_dirs=[numpy.get_include()]
)