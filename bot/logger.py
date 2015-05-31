#!/usr/bin/python
from TC import TC as TC # And TC again
from time import gmtime, strftime
import launcher as bot
import utils

class logger:
  info		= {'logLevel':1, 'colorCode':TC.ICyan,  'prefix':" INFO " }
  out		  = {'logLevel':2, 'colorCode':TC.IWhite, 'prefix':""       }
  debug		= {'logLevel':3, 'colorCode':TC.IBlue,  'prefix':" DEBUG" }
  warn		= {'logLevel':4, 'colorCode':TC.IYellow,'prefix':" WARN " }
  error		= {'logLevel':5, 'colorCode':TC.Red,    'prefix':" ERROR" }
  
  def log(self, logType, text):
    if logType["logLevel"] < self.info["logLevel"] or logType["logLevel"] > self.error["logLevel"]:
      self.log(self.error, "First parameter of \"logger.log\" is incorrect!")
      return false
    text = text.replace(TC.Rst, TC.Rst+TC.IWhite)
    prefix = ""
    if logType["prefix"] != "":
      prefix = TC.IWhite+"["+logType["colorCode"]+logType["prefix"]+TC.IWhite+"] "
    currentTime = "["+strftime("%H:%M", gmtime())+"]"
    printText = TC.IWhite+currentTime+prefix+text+TC.Rst
    plainText = currentTime+"["+logType["prefix"]+"] "+text
    print(printText)
    return
  
  def msg(self, msg):
    #return
    output = ""
    temp = ""
    msgDirection = "?"
    syncFinished = bot.syncFinished
    # if msg.out:
      # msgDirection = ">>>"  #LOCALE.msg.sent
    # else:
      # msgDirection = "<<<"  #LOCALE.msg.received
    if msg.dest.type_name == "user":
      output = output + TC.ICyan + msg.dest.username
    elif msg.dest.type_name == "chat":
      output = output + TC.Cyan + msg.dest.name
    if msg.dest.id == msg.src.id:
      output = output + TC.IGreen + " <> " + TC.Rst
    else:
      output = output + TC.IGreen + " <<< " + TC.ICyan + msg.src.username + TC.Rst
    #output = output + TC.ICyan + msg.src.username + TC.Rst
    # if msg.dest.type_name == "user" and msg.src.type_name == "user":
      # if msg.out:
        # output = output + TC.ICyan + msg.dest.username + TC.Rst
      # else:
        # output = output + TC.ICyan + msg.src.username + TC.Rst
    # elif msg.dest.type_name == "chat":
        # output = output + TC.ICyan + msg.dest.name + TC.IGreen + " <<< " +  TC.ICyan + msg.src.username + TC.Rst
    if not syncFinished:
      output = output+"("+"old"+") "
    if getattr(msg, "fwd_src", None) is not None:
      output = output+TC.IPurple+"[fwd "+TC.ICyan+msg.fwd_src.username+TC.IPurple+"]"+TC.Rst
    if getattr(msg, "reply", None) is not None:
      output = output+TC.IPurple+"[reply "+TC.ICyan+str(msg.reply.src.username)+TC.Rst+": "+TC.Yellow+utils.msgGetSummary(msg.reply, 10)+TC.IPurple+"]"+TC.Rst
    elif getattr(msg, "reply_id", None) is not None:
      output = output+TC.IPurple+"[reply "+TC.ICyan+str(msg.reply_id)+TC.IPurple+"]"+TC.Rst
    output = output+TC.Rst+": "+TC.IYellow+utils.msgGetSummary(msg, 0)+TC.Rst
    
    self.log(self.info, output)
    return
    
    