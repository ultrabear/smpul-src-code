# this is version 0.4
import sys
import time
name = "smpul"
versions = [2.7, 3.6, 3.7]
pyversion = sys.version_info[0]
if pyversion == 3:
  import statistics
  
  class tree:
    index = ["w()", "a()", "r()"]
    def w(a, b):
      c = open(a, "w+"); c.write(b); c.close()
    def a(a, b):
      c = open(a, "a+"); c.write(b); c.close()
    def r(a):
      try:
        c = open(a, "r"); b = c.read(); c.close(); return b
      except:
        return "Null"

  class math:
    index = ["mm()"]
    def mm(a):
      try:
        b = statistics.mean(a)
        c = statistics.median(a)
        return {"mean":b, "median":c}
      except:
        return "Null"
      
  class text:
    index = ["tprint()", "num()"]
    def tprint(a,b):
      for i in a:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(b)
      print(" ")
    def num(num):
      try:
        fnum = str(float(num)).split("."); flip = (fnum[0])[::-1]; floa = True
      except:
        return "Null"
      comp = ""
      for i in range(len(flip)):
        comp += flip[i]
        if (i+1)%3 == 0 and not(i+1 == len(flip)):
          comp += ","
      if fnum[1] != "0":
        comp = (fnum[1])[::-1] + "." + comp
      return comp[::-1]

  class discord:
    index = ["blockLetter()"]
    def blockLetter(a):
      b = ""
      for i in a:
        if i == " ":
          b += (":black_large_square: ")
        else:
          b += (":regional_indicator_%s: " % i)
      return b
  
  index = {"tree":tree.index, "math":math.index, "text":text.index, "discord":discord.index}

# the great divide -----------------------------------------------------------------------------------------------------


elif pyversion == 2:
  import tree
  import discord
  import text
  index = {"tree":tree.index, "text":text.index, "discord":discord.index}
else:
  print("ERR: unsupported python version\nDirectly supported versions found using smpul.versions")