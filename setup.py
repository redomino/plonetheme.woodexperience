from setuptools import setup, find_packages
import os

version = '1.2'

setup(
        name='plonetheme.woodexperience',
        version='1.2',
        description='An installable Diazo theme for Plone 4.1',
        long_description=open('README.rst', 'rb').read()+'\n'+
                         open(os.path.join("docs", "INSTALL.txt")).read()+'\n'+
                         open(os.path.join("docs", "HISTORY.txt")).read(),
        # Get more strings from
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Web Environment',
            'Framework :: Plone',
            'Framework :: Plone :: 4.1',
            'Framework :: Plone :: 4.2',
            'Framework :: Plone :: 4.3',
            'Framework :: Zope2',
            'Framework :: Zope3',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        ],
        keywords='web zope plone theme diazo',
        author='Giacomo Spettoli',
        author_email='giacomo.spettoli@gmail.com',
        url='https://github.com/redomino/plonetheme.woodexperience',
        packages=find_packages(),
        include_package_data=True,
        namespace_packages=[
            'plonetheme'
            ],
        install_requires=[
            'setuptools',
            'plone.app.theming',
            ],
        entry_points={
            'z3c.autoinclude.plugin': 'target = plone',
            }
        )

