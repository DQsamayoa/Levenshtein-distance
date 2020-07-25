from setuptools import setup

setup(name = 'levenshtein',
      version = '0.0.1',
      description = 'Levenshtein distance to get the number of inster, edit and/or substitute',
      url = 'https://github.com/dqsamayoa/py-levenshtein-distance',
      author = 'Victor Samayoa',
      author_email = 'vasamayoa@gmail.com',
      packages = ['levenshtein'],
      classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Levenshtein :: Edit Distance ',
        'Licence :: Apache-2.0'
      ],
      license = 'Apache-2.0',
      include_package_date = True,
      zip_safe = False)