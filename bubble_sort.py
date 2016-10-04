import random
from datetime import datetime


def randomNumArrayGen(max, length):
	arr = []
	for count in range(length):
		arr.append(int(round(random.random()*max)))
	return arr

def bubbleSort():
	unsorted = randomNumArrayGen(10000,100)
	endCheck = 1

    #FOR TIMING
    # var d = new Date();
    # var startTime = d.getTime();
    #END TIMING

	for i in range(0,len(unsorted)):
		for n in range(0,(len(unsorted) - endCheck)):
			if unsorted[n] > unsorted[n+1]:
				temp = unsorted[n]
				unsorted[n] = unsorted[n+1]
				unsorted[n+1] = temp
		endCheck+=1
    
    # FOR TIMING
    # var fdate = new Date();
    # console.log("BUBBLE SORT: " + (fdate.getTime() - startTime) + "ms");
    # END TIMING
	return unsorted


now1 = datetime.now().microsecond
print bubbleSort()
now2 = datetime.now().microsecond
print(str(now2 - now1) + " microseconds")

 