import sys
import subprocess, os

hex = sys.argv[1]
lilend = ''

# assign all chars in hex to array
hexChars = list(hex)

#make the output string

for i in range(4, 0, -1):
  leftDig = hexChars[2*(i-1)]
  rightDig = hexChars[2*i-1]
  lilend += r'\x'+str(leftDig)+str(rightDig)

print lilend
