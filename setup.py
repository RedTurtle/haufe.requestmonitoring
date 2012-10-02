import os
from setuptools import setup, find_packages

version = '0.3.0'

setup(name='haufe.requestmonitoring',
      version=version,
      description="Zope 2 request monitoring",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Zope2",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Logging",
        ],
      keywords='zope long-running-request monitor logging',
      author='Haufe Mediengruppe',
      author_email='info@zopyx.com',
      maintainer='Andreas Jung',
      maintainer_email='info@zopyx.com',
      license='ZPL',
      url='http://github.com/collective/haufe.requestmonitoring',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['haufe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Zope2',
          'zope.app.appsetup',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
