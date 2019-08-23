#!/usr/bin/python

import sys

# Create a HashMap from a list of integers with the Key being
# the data from the list and the Value is a count of the times
# that data appears in the list
def createHmap(datalist):
  countHmap = {}
  for d in datalist:
    if d not in countHmap:
      countHmap[d] = 1
    else:
      count = countHmap[d]
      count += 1
      countHmap[d] = count

  return (countHmap)

# Create a HashMap from the countHmap. The Keys of the new HashMap
# are the values of the input map. The values for each key is a list
# of the countHmap keys. The Key represents the number of times an
# input value appears in the input list.
def createFreqHmap(hm):
  fhmap = {}
  keys = hm.keys()

  for k in keys:
    fvalKey = hm[k]
    if fvalKey not in fhmap:
      fhmap[fvalKey] = [k]
    else:
      ilist = fhmap[fvalKey]
      ilist.append(k)
      fhmap[fvalKey] = ilist

  return (fhmap)

def prtFinal(hm):
  keys = hm.keys();

  # k is the number of times the numbers in its list appear in the input
  for k in keys:
    list = hm[k]
    list.sort()
    for l in list:
      for t in range(0,k):
        print l,
  print('\n')
  

def main(data):
  for n in range(0, len(data)):
    print("\n\nInput data:   {}".format(data[n]))
    hmap = createHmap(data[n])
    print("data hmap:    {}".format(hmap))
    freqMap = createFreqHmap(hmap)
    print("data FreqMap: {}".format(freqMap))
    prtFinal(freqMap)

# Take an input list of integers, and process them to produce
# maps that:
# - show the number of times an input number appears in the input list
# - show the list of input numbers for the number of times they appear
# e.g.
# Input data:   [1, 2, 3, 4, 2, 3, 4, 3, 4, 4, 5, 6, 6, 7, 7, 7]
# data hmap:    {1: 1, 2: 2, 3: 3, 4: 4, 5: 1, 6: 2, 7: 3}
# data FreqMap: {1: [1, 5], 2: [2, 6], 3: [3, 7], 4: [4]}
# 1 5 2 2 6 6 3 3 3 7 7 7 4 4 4 4 

if __name__ == '__main__':
  inLists = []
  dl1 = [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,3,4,5,6,7,8,7,6,5,4,5,6,7,6,5];
  dl2 = [9,1,8,2,7,3,6,4,5,2,8,3,7,4,6,5,3,7,4,6,5,4,6,5,5,5,6,1,3,4,8,3];
  if len(sys.argv) > 1:
    # Some sanity checks to verify input is a list of integers
    inL = sys.argv[1]
    # List needs at least [],
    if '[' not in inL or ']' not in inL or \
        inL[0] != '[' or inL[len(inL)-1] != ']':
      print('\nInvalid list input: {}\n'.format(inL))
      sys.exit(1)

    inLstr = inL.strip('[]').split(',')
    try:
        inList = map(int, inLstr)
    except ValueError:
      # All elements must be integer
      print('\nInvalid list input: {}\n'.format(inL))
      sys.exit(1)

    inLists.append(inList)

  else:
    inLists.append(dl1)
    inLists.append(dl2)

  main(inLists)
