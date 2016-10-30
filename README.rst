plonetheme.woodexperience
=========================


Introduction
------------

The ``plonetheme.woodexperience`` package uses the *theming & packaging* features
available in `plone.app.theming`_ to make the theme `woodexperience`_ easily
available in Plone 4.x version.

.. image:: https://raw.github.com/redomino/plonetheme.woodexperience/master/screenshot.png
   :alt: A plonetheme.woodexperience product theme screenshot


Installation
------------


Add Plone site
~~~~~~~~~~~~~~

Install Plone 4.x with `plone.app.theming`_ and create a Plone site (if you have not already)
with Diazo theming configured.


Zip file
~~~~~~~~

If you are an end user, you might enjoy installation via zip file import.

1. Download the zip file: https://raw.githubusercontent.com/redomino/plonetheme.woodexperience/master/woodexperience.zip
2. Import the theme from the Diazo theme control panel.


Buildout
~~~~~~~~

If you are a developer, you might enjoy installation via buildout.

Add ``plonetheme.woodexperience`` to your ``plone.recipe.zope2instance`` section's *eggs* parameter e.g.::

    [instance]
    eggs =
        Plone
        …
        plonetheme.woodexperience

and then running "bin/buildout"


Select theme
~~~~~~~~~~~~

Select and enable the theme from the Diazo control panel. That's it!


Contribute
----------

* Issue Tracker: https://github.com/redomino/plonetheme.woodexperience/issues

* Source Code: https://github.com/redomino/plonetheme.woodexperience

* Wiki: https://github.com/redomino/plonetheme.woodexperience/wiki


Authors
-------

This product was developed by:

* Giacomo Spettoli aka giacomo for `Redomino team`_.


Collaborations
~~~~~~~~~~~~~~

* Leonardo J. Caballero G. aka macagua

* Full Name aka nickname

For an updated list of all the contributors visit: https://github.com/redomino/plonetheme.woodexperience/graphs/contributors


Support
-------

If you are having issues, please let us know via `our Issue Tracker`_.


License
-------

This package is GPL version 2.


.. _`woodexperience`: http://www.freelayoutsworld.com/free-layouts/preview/648876299/
.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`Redomino team`: http://redomino.com/
.. _`our Issue Tracker`: https://github.com/redomino/plonetheme.woodexperience/issues

