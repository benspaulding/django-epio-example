=================================
 An Example ep.io Django Project
=================================

.. contents::

What is this?
-------------

.. note:: ep.io_ has shutdown_, so this isn’t exactly useful anymore. :(

.. _shutdown: https://www.ep.io/blog/epio-closing-down/

ep.io_ is a painless, powerful Python/Django hosting service. This is a
simple example of how to set up an application using their free plan.
It includes:

* Getting Django running
* Handling static media (with contrib.static and django_compressor)
* Handling content media
* Using PostgreSQL for a database
* Caching and sessions with Redis
* Building a search index with Haystack

In addition to these instructions, useful comments have been added
throughout the ``epio.ini`` and ``example/settings.py`` files.

.. _ep.io: https://www.ep.io/

Getting Started
---------------

Documentation & Support
~~~~~~~~~~~~~~~~~~~~~~~

The ep.io documentation_ is quite thorough. (Though I do wish it had a
built-in search feature. But Googling with ``site:www.ep.io My Query``
works just fine for now.) What is not answered in the docs can often be
quickly answered in the ep.io Freenode IRC channel, `#epio`_.

Please read through the `Quickstart Guide`_ to get some context.

.. _documentation: https://www.ep.io/docs/
.. _#epio: irc://irc.freenode.net/epio
.. _Quickstart Guide: https://www.ep.io/docs/quickstart/

Request an ep.io invite
~~~~~~~~~~~~~~~~~~~~~~~

ep.io is currently invite-only. If you like what you see in the docs,
`request an invite`__. Once you receive your invitation, you can
proceed with the rest of this example.

__ ep.io_

Install epio client
~~~~~~~~~~~~~~~~~~~

As you saw in the `Quickstart Guide`_, there is an epio client. Install
it::

    $ pip install epio

Upload ssh key
~~~~~~~~~~~~~~

Uploading your public key allows you to talk with epio using the client.
Run the following::

    $ epio upload_ssh_key

Further explanation can be found in the in `Creating/Associating an account`_.

.. _Creating/Associating an account: https://www.ep.io/docs/quickstart/#creating-associating-an-account

Deploying This Project as an ep.io App
--------------------------------------

Now that you have got all that stuff read and done, you can get on with
this quick and painless part.

Create ep.io app
~~~~~~~~~~~~~~~~

First, create an app in the `control panel`_ or by using the `epio
create`_ command. Name it whatever you like.

::

    $ epio create testapp

.. _control panel: https://www.ep.io/control/
.. _epio create: https://www.ep.io/docs/client/#create

Clone this repo
~~~~~~~~~~~~~~~

Clone this repo onto your local machine::

    $ git clone git://github.com/benspaulding/django-epio-example.git
    $ cd django-epio-example

Change app name in ``.epio-app``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ep.io knows where you want this project deployed to by the app name
provided in ``.epio-app``. Simply open that file and change ``testapp``
to the name that you gave your app.

Run ``epio upload``
~~~~~~~~~~~~~~~~~~~

Deploy this project to ep.io by running::

    $ epio upload

This will upload the code to ep.io, and ep.io will then install all of
the packages defined in the ``requirements.txt`` file, get the web
instance running, start up Redis, and append database settings to
``settings.py``.

Didn’t that just feel good?

You can also upload to ep.io via version control system, such as git. It
is super-handy, and you should use it in the future. See `VCS Support`_.

.. _VCS Support: https://www.ep.io/docs/vcss/

Run ``epio django syncdb``
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can `run Django management commands`_ through the ``epio`` client.
You need to run syncdb, so do it now::

    $ epio django syncdb

Create a superuser just like you normally would.

.. _run Django management commands: https://www.ep.io/docs/client/#django

You can now visit `testapp.ep.io/admin/`_ to see the site.

.. _testapp.ep.io/admin/: https://testapp.ep.io/admin/

Run ``epio django collectstatic``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You now have Django up and running, but the admin and other static media
is not working. To get it where it needs to be, run::

    $ epio django -- collectstatic --noinput

We have static media. Yay! Verify at `testapp.ep.io/admin/`_

Run ``epio django rebuild_index``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We now need to build our search index. Simply run::

    $ epio django -- rebuild_index --noinput

We use ``--noinput`` simply because we have no previous indexes, so we
don’t need it asking us if we are sure we want to wipe out the old and
start new.

Though we are using Whoosh_, ep.io is working on `Solr support`_.

.. _Whoosh: https://bitbucket.org/mchaput/whoosh/
.. _Solr support: https://www.ep.io/docs/services/solr/

Onward & Upward
---------------

Did you just see how painless getting a full Django project running can
be? Now have a look through the ``epio.ini`` and ``example/settings.py``
files for some more explanation and links to documentation.