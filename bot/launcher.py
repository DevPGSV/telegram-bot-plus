#!/usr/bin/python
import tgl
import pprint
from functools import partial
from logger import logger
logger = logger()
import utils
import traceback
import sys
from TC import TC as TC # And TC again
import emoji
import pluginManager as plugins

our_id = 0
pp = pprint.PrettyPrinter(indent=4)
syncFinished = False
binlog_done = False

def on_binlog_replay_end():
    global binlog_done
    print("SYNC!!!")
    binlog_done = True
    _TC_OUTPUT_TEST()
    return

def on_get_difference_end():
    global syncFinished
    syncFinished = True
    _TC_OUTPUT_TEST
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
    #pp.pprint(utils.msg2dict(msg))
    logger.msg(msg)
    if msg.dest.id == our_id: # direct message
        peer = msg.src
    else: # chatroom
        peer = msg.dest
    if msg.text is not None and msg.text.startswith("!ping"):
        peer.send_msg("PONG!")
    elif msg.text is not None and msg.text.startswith("!emoji"):
        peer.send_msg("Emojis: \n" + emoji.emojize(':white_check_mark: :smile: :laughing: :blush: :smiley: :x: :heavy_check_mark:', use_aliases=True).encode('UTF-8'))
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


def _TC_OUTPUT_TEST():
    logger.log(logger.debug, "Testeando cosas:")
    logger.log(logger.debug, " Colores:")
    logger.log(logger.debug, "  Font:")
    logger.log(logger.debug, "   OSCURO: "+TC.Black+"negro "+TC.Red+"rojo "+TC.Green+"verde "+TC.Yellow+"amarillo "+TC.Blue+"azul "+TC.Purple+"morado "+TC.Cyan+"cyan "+TC.White+"blanco")
    logger.log(logger.debug, "   CLARO : "+TC.IBlack+"negro "+TC.IRed+"rojo "+TC.IGreen+"verde "+TC.IYellow+"amarillo "+TC.IBlue+"azul "+TC.IPurple+"morado "+TC.ICyan+"cyan "+TC.IWhite+"blanco")
    logger.log(logger.debug, "  Background:")
    logger.log(logger.debug, "   OSCURO: "+TC.OnBlack+"negro "+TC.OnRed+"rojo "+TC.OnGreen+"verde "+TC.OnYellow+"amarillo "+TC.OnBlue+"azul "+TC.OnPurple+"morado "+TC.OnCyan+"cyan "+TC.OnWhite+"blanco")
    logger.log(logger.debug, "   CLARO : "+TC.OnIBlack+"negro "+TC.OnIRed+"rojo "+TC.OnIGreen+"verde "+TC.OnIYellow+"amarillo "+TC.OnIBlue+"azul "+TC.OnIPurple+"morado "+TC.OnICyan+"cyan "+TC.OnIWhite+"blanco")
    logger.log(logger.debug, " Estilos:")
    logger.log(logger.debug, "   "+TC.Rst+TC.Bold+"Bold "+TC.Rst+TC.Undr+"Undr "+TC.Rst+TC.Inv+"Inv "+TC.Rst+TC.Reg+"Reg "+TC.Rst+TC.RegF+"RegF "+TC.Rst+TC.RegB+"RegB")
    logger.log(logger.debug, " Emoji:")
    logger.log(logger.debug, emoji.emojize('   :white_check_mark: :smile: :laughing: :blush: :smiley: :x: :heavy_check_mark:', use_aliases=True))
    print(sys.version_info)
    return
