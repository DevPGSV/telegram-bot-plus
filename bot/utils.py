#!/usr/bin/python

from inspect import getmembers
import tgl

def msg2dict(obj):
  dict = {}
  for k,v in [(x, getattr(obj, x)) for x in dir(obj) if not x.startswith('__')]:
    if not str(type(v)) == "<type 'builtin_function_or_method'>":
      if type(v) == tgl.Peer:
        dict[k] = peer2dict(v)
      else:
        dict[k] = v
  return dict

def peer2dict(peer):
  dict = {}
  peerAttr = dir(peer)
  for x in peerAttr:
    if not x.startswith('__'):
      #dict[x] = "-"
      #print(x)
      #import ipdb; ipdb.set_trace()
      #print(peer.type_name)
      if peer.type_name == "user":
        if not x == "user_list":
          v = getattr(peer, x, None)
          if v is not None and not str(type(v)) == "<type 'builtin_function_or_method'>" and not type(v) == tgl.Peer:
            dict[x] = v
      elif peer.type_name == "chat":
        if not x == "user_status" and not x == "first_name" and not x == "last_name" and not x == "phone" and not x == "username" and not x == "user_id" and not x == "user":
          v = getattr(peer, x, None)
          if v is not None and not str(type(v)) == "<type 'builtin_function_or_method'>" and not type(v) == tgl.Peer:
            dict[x] = v
      else:
        dict[x] = "unknown"
  return dict
