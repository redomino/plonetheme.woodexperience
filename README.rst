=========================
plonetheme.woodexperience
=========================

A Diazo_ theme to make the `woodexperience`_ theme from freelayoutsworld.com easily available in `Plone`_.


Introduction
============

*plonetheme.woodexperience* Theme is an installable Plone_ Theme using the **theming** and **packaging** 
features available in `plone.app.theming`_.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest versión (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/redomino/plonetheme.woodexperience/raw/master/plonetheme/woodexperience/static/preview.png


Features
========

- It's an installable Plone_ Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- Also it's a simple Diazo_ package (Zip file).
- It's have support for clean uninstallation.


Installation
============


Buildout
--------

If you are a **developer user**, you might enjoy installing it via buildout.

For install ``plonetheme.woodexperience`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.woodexperience


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.woodexperience',
    ],


Zip file
--------

If you are an **end user**, you might enjoy installation via zip file import.

1. Download a `zip file <https://github.com/redomino/plonetheme.woodexperience/raw/master/plonetheme.woodexperience.zip>`_.
2. Import the theme from the Diazo theme control panel.


Enabling the theme
^^^^^^^^^^^^^^^^^^

Browse to ``http://yoursite/Plone/@@theming-controlpanel`` click on ``Enable`` on ``Plonetheme Redmusic`` theme from the Diazo control panel. That's it!


Contribute
==========

- Issue Tracker: https://github.com/redomino/plonetheme.woodexperience/issues
- Source Code: https://github.com/redomino/plonetheme.woodexperience


License
=======

The project is licensed under the GPLv2.

Credits
-------

- Giacomo Spettoli, (giacomo.spettoli at gmail dot com).
- Leonardo J. Caballero G. (leonardocaballero at gmail dot com).

.. _`Plone`: http://plone.org
.. _`woodexperience`: http://www.freelayoutsworld.com/free-layouts/preview/648876299/
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`Diazo`: http://diazo.org
