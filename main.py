import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sorting_algorithms import BubbleSort, MergeSort, InsertionSort, QuickSort
import sys
import random

# when this file is itself is ran, not by importing.
if __name__ == '__main__':
	ms_speed = 180  #interval in millisec by which animation will run.
	li = []
	step_cnt = 0 
	try:
		N = int(input("Enter no. of elements to be sorted: "))
		choice = int(input("Choice(1:select randomly, 2:input manually): "))
		if choice == 1:
			li = random.sample(range(0, 2*N), N) #selects N random nums from range(0, 2N)
		elif choice == 2:
			for i in range(N):
				num = input("Enter {}th element: ".format(i+1))
				li.append(int(num))
		else:
			sys.exit("Invalid input!")

		algo_dict = {1:'Bubble Sort', 2:'Merge Sort', 3:'Insertion Sort', 4:'Quick Sort'}
		algo = int(input('Choose Sorting Algorithm:\n{}: '.format(algo_dict)))
		if algo == 1:
			generator_func = BubbleSort(li)
		elif algo == 2:
			generator_func = MergeSort(li, 0, N-1)
		elif algo == 3:
			generator_func = InsertionSort(li)
		elif algo == 4:
			generator_func = QuickSort(li, 0, N-1)
		else:
			sys.exit("Invalid input!")

	except Exception as e:
		raise e
