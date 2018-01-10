|icon| PUBGIS |Build status| |Github All Releases| |PyPI|
=========================================================

PUBGIS (PUBG Geographic Information System) analyzes gameplay from
`PUBG`_ (either live or video) and tracks your position during the game.
You can view this information later to see your path throughout the
game.

PUBGIS works by continuously scanning the minimap in the corner of the
game (seen below) and matching that to a location on the world map. If
you want more details about how PUBGIS works, check out the
`Theory of Operation`_ wiki page

Note (1/10/18):  Since the 1.0 Update of PUBG, the UI has changed significantly.  Because PUBGIS uses the displayed UI map, this means that PUBGIS needs to be updated to properly detect & parse the new map.  I haven't had time to do this work yet, but I'm hoping to find time in the future.  In the meantime, contributions are welcome :)  [See `Issue#43`_ for the latest]

Installation
------------

PUBGIS is a self-contained executable. Download the latest version
`here`_, no installation required!

Examples
--------

.. image:: https://github.com/andrewzwicky/PUBGIS/raw/master/docs/composite_example.png

Quick-Start
-----

When PUBGIS is started, you'll see this:

.. figure:: https://github.com/andrewzwicky/PUBGIS/raw/master/docs/example_setup.jpg
   :scale: 45 %

1. Select a video file (only tested with .mp4 currently)

2. Adjust the output file if needed.

3. Click Process!

4. For more deatils about all the options, read the `Usage`_ wiki page.

**NOTE:**  PUBGIS live recording does not currently work when running PUBG Fullscreen (Fullscreen (Windowed) is OK). I'm tracking `Issue#41`_. Sorry for the inconvenience.

Development
-----------

PUBGIS is written in Python (3.6). If you'd like to use PUBGIS as a
python package, you can install it using ``pip``

::

    pip install pubgis

and run it using:

::

    python -m pubgis

To learn more about extending or contributing to PUBGIS, check out the
`Development`_ page.

License
-------

This project is licensed under the GPLv3 License - see the `LICENSE.md`_
file for details

.. _PUBG: https://www.playbattlegrounds.com/main.pu
.. _`Theory of Operation`: https://github.com/andrewzwicky/PUBGIS/wiki/Theory-of-Operation
.. _Usage: https://github.com/andrewzwicky/PUBGIS/wiki/Usage
.. _here: https://github.com/andrewzwicky/PUBGIS/releases/latest
.. _Issue#41: https://github.com/andrewzwicky/PUBGIS/issues/41
.. _Issue#43: https://github.com/andrewzwicky/PUBGIS/issues/43
.. _Development: https://github.com/andrewzwicky/PUBGIS/wiki/Development
.. _LICENSE.md: LICENSE.md

.. |icon| image:: pubgis/images/icons/navigation_32.png
.. |Build status| image:: https://ci.appveyor.com/api/projects/status/sbooipngsjk1kx46/branch/master?svg=true
   :target: https://ci.appveyor.com/project/andrewzwicky/pubgis/branch/master
.. |Github All Releases| image:: https://img.shields.io/github/downloads/andrewzwicky/PUBGIS/total.svg
   :target: https://github.com/andrewzwicky/PUBGIS/releases/latest
.. |PyPI| image:: https://img.shields.io/pypi/v/PUBGIS.svg
   :target: https://pypi.python.org/pypi/PUBGIS
