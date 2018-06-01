import os
from setuptools import setup, find_packages


setup(
  name = 'sitemapper',
  packages = ['sitemapper'],
  version = '1.0.0',
  description = '''
  A tool for generating xml sitemaps from a list of urls.
  ''',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author = 'Marco Montagna',
  author_email = 'marcojoemontagna@gmail.com',
  url = 'https://github.com/mmontagna/sitemapper',
  keywords = ['sitemaps', 'sitemap index', 'sitemap generator'],
  classifiers=(
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
  ),
  package_data={'': ['LICENSE']},
  include_package_data=True,
  python_requires=">=2.7",
  license=open('LICENSE').read(),
  install_requires=[

  ],
  entry_points = {
    'console_scripts': [
      'sitemapper=sitemapper.__main__:main'
      ]
  },
)
