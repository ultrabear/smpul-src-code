import time
import sys


index = ["tprint()", "num()"]
def tprint(a,b):
  for i in a:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(b)
  print("")
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