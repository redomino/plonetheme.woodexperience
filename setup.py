from setuptools import setup, find_packages
import os

version = '1.2'

setup(
        name='plonetheme.woodexperience',
        description='Wood experience, is an installable Diazo theme for Plone 4',
        long_description=open('README.rst', 'rb').read()+'\n'+
                         open(os.path.join("docs", "INSTALL.txt")).read()+'\n'+
                         open(os.path.join("docs", "HISTORY.txt")).read(),
        version=version,
        author='Giacomo Spettoli',
        author_email='giacomo.spettoli@gmail.com',
        maintainer='Leonardo Caballero',
        maintainer_email='leonardocaballero@gmail.com',
        url='https://github.com/redomino/plonetheme.woodexperience',
        license='GPL',
        keywords='web zope plone theme diazo woodexperience',
        packages=find_packages(),
        include_package_data=True,
        namespace_packages=[
            'plonetheme'
            ],
        install_requires=[
            'setuptools',
            'plone.app.theming',
            ],
        # Get more strings from
        # https://pypi.org/pypi?:action=list_classifiers
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: Web Environment",
            "Framework :: Plone",
            "Framework :: Plone :: 4.1",
            "Framework :: Plone :: 4.2",
            "Framework :: Plone :: 4.3",
            "Framework :: Plone :: Theme",
            "Framework :: Zope2",
            "Framework :: Zope3",
            "Intended Audience :: Developers",
            "Intended Audience :: End Users/Desktop",
            "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Topic :: Internet",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
        entry_points={
            'z3c.autoinclude.plugin': 'target = plone',
            }
        )
