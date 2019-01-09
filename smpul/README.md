
# smpul.py
## V0.3.2

A neat small package to speed up your coding

check out the [github page](https://github.com/ultrabear/smpul-src-code) for source code

### FUNCTIONS:
* smpul
  * tree
    * r(*filename*) **reads from a file and returns the contents**
	* w(*filename*, *content*) **writes to a file**
	* a(*filename*, *content*) **appends to a file**
  * math
    * mm(*numberlist*) **returns the mean and median of a list of numbers in a dictionry, call with "mean" and "median"**
  * text
    * tprint(*content*, *timeBetweenChrs*) **prints a string and for each item in it waits a specified amout of time before printing the the next**
    * num(*number*) **takes any number and formats it with commas to show thousands place and so forth**
  * discord
    * blockLetter(*content*) **returns discords custom blockletter emoji syntax for any string of alphabetic chrs**

### CHANGELOG:
* 0.3.2
  * added a changelog
  * improved the text.num function to support float vartype
  * improved the tree.r function to not break when file is nonexistant, returns Null instead
  * improved smpul.index to return a dictionary containing every function instead of a list

note: type index at any point in the module to get a list of the avalible options

-Alex