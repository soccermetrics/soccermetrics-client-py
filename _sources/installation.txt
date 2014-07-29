.. _installation:

Installation
============

The Soccermetrics API Python client library depends on the
`Requests <http://docs.python-requests.org/en/latest/>`_ and
`easydict <http://pypi.python.org/pypi/easydict/>`_ libraries.  You can install
the client library within a virtual environment on your computer, or install
it system-wide.

Python 2.6+ is required.

It's not required, but `autoenv <https://github.com/kennethreitz/autoenv>`_ is
very nice to have.

Virtual Environment Install
---------------------------

We recommend installing ``soccermetrics-client-py`` within a virtual environment
using ``virtualenv``.  That way you can run different versions of Python
installations and libraries without dealing with conflicting dependencies.

We also recommend installing `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/en/latest/>`_.
As it says on the label, it is a wrapper around `virtualenv` that manages the virtual
environments on your machine and allows you to customize pre- and post-activation
(and deactivation) behavior, such as setting environment variables or opening your text editor.

Here is a link to `a nice tutorial on Virtualenv <http://simononsoftware.com/virtualenv-tutorial/>`_.
And `a tutorial on virtualenvwrapper <http://sccr.mx/1pZ5Xtx>`_ as well.

To install ``virtualenv`` on MacOS or Linux, create a folder and run one of these
two commands as ``sudo``:

.. sourcecode:: bash

    $ sudo easy_install virtualenv

or

.. sourcecode:: bash

    $ sudo pip install virtualenv

If you are on Windows, `this link <http://flask.pocoo.org/docs/installation/#windows-easy-install>`_
will show you how to install ``pip`` and ``distribute``, which you will use to
install ``virtualenv``.

Download `the current zipped version of the source code`_ from GitHub, unzip the
folder and run:

.. sourcecode:: bash

    $ make install

System-Wide Install
-------------------

If you want to install ``soccermetrics-client-py`` system-wide -- not recommended
because of possible library conflicts -- download
`the current zipped version of the source code`_ from GitHub, unzip the
folder and run:

.. sourcecode:: bash

    $ make install

.. _`the current zipped version of the source code`: https://github.com/soccermetrics/soccermetrics-client-py/archive/master.zip
