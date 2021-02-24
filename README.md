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
>>> acc.search("joy of painting", verbose=True)
{'The Joy of Painting (1983) [79167]': [Example:The Joy of Painting:79167], 'Meadow Lake (1983) [79167/2/1]': [Example:Meadow Lake:79167/2/1], 'Ebony Sunset (1983) [79167/1/3]': [Example:Ebony Sunset:79167/1/3], 'A Walk in the Woods (1983) [79167/1/1]': [Example:A Walk in the Woods:79167/1/1]}
>>> show = _["The Joy of Painting (1983) [79167]"][0].result
>>> with open("joyofpainting.m3u8", "w") as f:
...   f.write(acc.getM3U8(show.episodes()))
```
