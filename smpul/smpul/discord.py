index = ["blockLetter()"]
def blockLetter(a):
  b = ""
  for i in a:
    if i == " ":
      b += (":black_large_square: ")
    else:
      b += (":regional_indicator_%s: " % i)
  return b