plexapiplus
===========

A wrapper for [python-plexapi](https://python-plexapi.readthedocs.io) that simplifies some things in using the library. More additions planned.

Usage
-----

```python
>>> from plexapiplus import Account # wrapper for plexapi.myplex.MyPlexAccount
>>> acc = Account() # pulling myplex_username/password from config.ini
>>> for resource, server in acc.servers():
>>>   print(resource, server)
>>> 
<MyPlexResource:Example> <PlexServer:https://127-0-0-1>
```
