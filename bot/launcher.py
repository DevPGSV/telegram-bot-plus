#!/usr/bin/python
import tgl
import pprint
from functools import partial
from logger import logger
logger = logger()
import utils
import traceback
import sys
#from TC import TC as TC # And TC again

our_id = 0
pp = pprint.PrettyPrinter(indent=4)
syncFinished = False

def on_binlog_replay_end():
  syncFinished = True
  return

def on_get_difference_end():
  return

def on_our_id(id):
  our_id = id
  return

def msg_cb(success, msg):
  pp.pprint(success)
  pp.pprint(msg)

HISTORY_QUERY_SIZE = 100

def history_cb(msg_list, peer, success, msgs):
  print(len(msgs))
  msg_list.extend(msgs)
  print(len(msg_list))
  if len(msgs) == HISTORY_QUERY_SIZE:
    tgl.get_history(peer, len(msg_list), HISTORY_QUERY_SIZE, partial(history_cb, msg_list, peer))


def cb(success):
  print(success)

def on_msg_receive(msg):
  if not syncFinished:
    print ("RET - 1")
    return;
  pp.pprint(utils.msg2dict(msg))
  if msg.dest.id == our_id: # direct message
    peer = msg.src
  else: # chatroom
    peer = msg.dest
  if msg.text.startswith("!ping"):
    peer.send_msg("PONG!")
  return

def on_secret_chat_update(peer, types):
  return "on_secret_chat_update"

def on_user_update(peer, what_changed):
  return

def on_chat_update(peer, what_changed):
  return

# Set callbacks
tgl.set_on_binlog_replay_end(on_binlog_replay_end)
tgl.set_on_get_difference_end(on_get_difference_end)
tgl.set_on_our_id(on_our_id)
tgl.set_on_msg_receive(on_msg_receive)
tgl.set_on_secret_chat_update(on_secret_chat_update)
tgl.set_on_user_update(on_user_update)
tgl.set_on_chat_update(on_chat_update)
