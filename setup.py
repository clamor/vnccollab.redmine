from setuptools import setup, find_packages
import os

version = open('version.txt').read()

setup(name='vnccollab.redmine',
      version=version,
      description="VNC Collaboration Redmine AddOn.",
      long_description=open(os.path.join("docs", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Programming Language :: Python",
          "Operating System :: OS Independent",
      ],
      keywords='redmine',
      author='Jose Dinuncio',
      author_email='jose.dinuncio@vnc.biz',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['vnccollab'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'textile',
          'pyactiveresource',
          'five.grok',
          'plone.api',
          'collective.customizablePersonalizeForm',
          'vnccollab.common'
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
