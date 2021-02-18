aio-videoindexer
**************************
.. toctree::
   :maxdepth: 2
   :caption: Contents:

Overview
========
An async video indexer package for querying `Microsoft Media Services Video Indexer <https://docs.microsoft.com/en-us/azure/media-services/video-indexer/>`_ in Python.

.. seealso:: See the `original application <https://github.com/sealjay-clj/teams-vid>`_ this package was forked from.

1. Install the package from pip with ``pip install aio-videoindexer``
2. Subscribe to the video indexer API: https://api-portal.videoindexer.ai/
3. Log into your video indexer account: https://www.videoindexer.ai/account/login

.. warning:: This package is in active development, and documentation and examples are missing throughout the application.

Setup Example
=============
Here is an example of the package in use::

   from asyncvideoindexer import AsyncVideoIndexer

   VIDEO_INDEXER_ACCOUNT_ID = "your-account-id"
   VIDEO_INDEXER_KEY = "your-account-key"
   VIDEO_INDEXER_ACCOUNT_LOCATION = "your-account-location"

   async def get_video_indexer():
      video_indexer = await AsyncVideoIndexer.AsyncVideoIndexer.create(
         VIDEO_INDEXER_ACCOUNT_ID,
         VIDEO_INDEXER_KEY,
         VIDEO_INDEXER_ACCOUNT_LOCATION,
      )

Main Class
===================
.. automodule:: AsyncVideoIndexer
  :members:
