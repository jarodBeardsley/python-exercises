'''
Author: Jarod Beardsley
Version 07/01/2021

Take-home assesment to write a program in Python that reads two CSVs, bandwidth.csv and netbitrate.csv and 
prints the joined information contained within.
'''

import csv

######################
# Main Program       #
######################
if __name__ == '__main__':
  with open('netbitrate.csv') as nbr:
    netbitrate = csv.reader(nbr, delimiter=',', quotechar='|')
    i = 0
    for nline in netbitrate:
      with open('bandwidth.csv') as bw:
        bandwidth = csv.reader(bw, delimiter=','< quotechar='|')
        for bline in bandwidth:
          if bline[0] == nline[1] and bline[1] == nline[2] and i>0:
            utilization = float(nline[3])/int(bline[2])
            print(nline[0] + " " + bline[0] + " " + bline[1] + " " + str(utilization)
      i += 1
      
