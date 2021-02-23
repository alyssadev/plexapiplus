plexapiplus
===========

A wrapper for [python-plexapi](https://python-plexapi.readthedocs.io) that simplifies some things in using the library. More additions planned.

Usage
-----

```python
>>> from plexapiplus import Account # wrapper for plexapi.myplex.MyPlexAccount
>>> acc = Account() # pulling myplex_username/password from config.ini
>>> for server in acc.servers():
>>>   print(server)
>>> 
<MyPlexServerShare:12345678:Example>
<MyPlexServerShare:23456:Example2>
<MyPlexServerShare:123123:Example3>
```
