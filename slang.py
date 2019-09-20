#!/usr/bin/python
import sys
import os
import re
pos_words = {}

def load_list(filename,dic):
   f = open(filename)
   for line in f.readlines():
      if not line.startswith('#'):
         dic[line.strip()] = True
   f.close()
   
def polnem(twtt):
   list = twtt.split('\n')
   features = ''
   features += str(len(list)-1 )+','
   text = ' '.join(list[1:])
   m = re.match(r'<A=(\d)>',list[0])
   #polarity number
   return m.group(1)
 
 
def feat16(text,pol):
   
   list_word = twtt.split()
   count = 0;
   for word in list_word:
      w = word.split('/')[0].lower()
      if w in pos_words:
         print w +"   "+ pol
         if pol == '4':
            pos_words[w]+=1
         else:
            pos_words[w]-=1

if __name__ == "__main__":

   if len(sys.argv) <2 or len(sys.argv)>4 :
      print "Usage: %s <input filename> <arff file> [<max number>]" %(sys.argv[0])
      sys.exit(0)
      
   if not os.path.exists(sys.argv[1]):
      print sys.argv[1] + " not exists"
      sys.exit(0)
   load_list("positive_words.txt",pos_words) 
   max_twt = 0
   
   if len(sys.argv)==4:
      max_twt = int(sys.argv[3])
   twtt_file = open(sys.argv[1],'r') 
   count = 0
   twtt = twtt_file.readline()
   while count < max_twt or max_twt == 0:
      while True:
         line = twtt_file.readline()
         if not line or line.startswith('<A='):
            break
         twtt += line
      
      pol = polnem(twtt)
      feat16(twtt,pol)

      if not line:
         break
      twtt = line
      count += 1

   
   twtt_file.close()
   print pos_words
   
   