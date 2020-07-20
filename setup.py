import fnmatch
from setuptools import find_packages, setup, Extension
from setuptools.command.build_py import build_py as build_py_orig
from Cython.Build import cythonize


extensions = [
    # Module's name for the package
    Extension('levenshtein.*', ['levenshtein/*.py'])
]

# Excluding the __init__.py files from the compiling fo Cython
cython_excludes = ['**/__init__.py']

# Defining a function to filter the files that should not be compiled.
def not_cythonized(tup):
    (package, module, filepath) = tup
    return any(
        fnmatch.fnmatchcase(filepath, pat = pattern) for pattern in cython_excludes
    ) or not any(
        fnmatch.fnmatchcase(filepath, pat = pattern)
        for ext in extensions
        for pattern in ext.sources
    )

# Defining a specific class to create the compilation.
class build_py(build_py_orig):
    def find_modules(self):
        modules = super().find_modules()
        return list(filter(not_cythonized, modules))

    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        return list(filter(not_cythonized, modules))

setup(name = 'levenshtein',
      version = '0.0.1',
      description = 'Levenshtein distance to get the number of inster, edit and/or substitute',
      url = 'https://github.com/dqsamayoa/levenshtein-distance',
      author = 'Victor Samayoa',
      author_email = 'vasamayoa@gmail.com',
      classifiers = [
        'Development Status :: 3 - Alpha'
        'Programming Language :: Python :: 3.7',
        'Topic :: Levenshtein :: Edit Distance ',
        'Licence :: MIT'
      ],
      license = 'MIT',
      packages = find_packages(),
      ext_modules = cythonize(extensions, exclude = cython_excludes, language_level = '3'),
      cmdclass = {'build_py': build_py},
      include_package_date = True,
      zip_safe = False)