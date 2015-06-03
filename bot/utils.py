#!/usr/bin/python

from inspect import getmembers
import tgl
import pprint
pp = pprint.PrettyPrinter(indent=4)

def msg2dict(obj, rec = 3):
    dict = {}
    if not type(obj) == tgl.Msg:
        return dict
    for k,v in [(x, getattr(obj, x)) for x in dir(obj) if not x.startswith('__')]:
        if not str(type(v)) == "<type 'builtin_function_or_method'>":
            #print(k)
            if type(v) == tgl.Peer:
                dict[k] = peer2dict(v, rec - 1)
            elif type(v) == tgl.Msg and rec > 0:
                dict[k] = msg2dict(v, rec - 1)
            else:
                dict[k] = v
    return dict

def peer2dict(peer, rec = 3):
    dict = {}
    if not type(peer) == tgl.Peer:
        return dict
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

def msgGetSummary(msg, truncate = 0):
    if getattr(msg, "text", None) is not None:
        return (msg.text[:truncate] + '...') if (len(msg.text) > truncate and truncate is not 0) else msg.text
    elif getattr(msg, "media", None) is not None:
        return "Media: " + str(msg.media["type"])
    elif getattr(msg, "service", None) is not None and msg.service:
        return "Service"
    else:
        return ":O"