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