plexapiplus
===========

A wrapper for [python-plexapi](https://python-plexapi.readthedocs.io) that simplifies some things in using the library. Main focus is on simplifying the action of transcoding media files, and everything leading up to that.

Usage
-----

```python
>>> from plexapiplus import Account # wrapper for plexapi.myplex.MyPlexAccount
>>> acc = Account() # pulling myplex_username/password from config.ini
>>> acc.search("big buck bunny", verbose=True, fetch=True)
Retrieving servers
connected to Example
connected to Example2
{'Big Buck Bunny (2008) [tt1254207]': [Example:Big Buck Bunny:tt1254207, Example2:Big Buck Bunny:tt1254207]}
```
