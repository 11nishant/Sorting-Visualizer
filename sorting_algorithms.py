'''The yield statement suspends functions execution and sends a value back to the caller, but retains 
  	enough state to enable function to resume where it is left off. When resumed, the function continues 
  	execution immediately after the last yield run. This allows its code to produce a series of values over time, 
  	rather than computing them at once '''


def swap(li, i, j):
	if i != j:
		li[i], li[j] = li[j], li[i]
		

def BubbleSort(li):
	swapped = False #flag in case if list is already sorted.
	for i in range(len(li) - 1):
		for j in range(len(li) - 1 - i):
			if li[j] > li[j + 1]:
				swap(li, j, j+1)
				swapped = True
				yield li #so that any update in data can be visualized at each iteration.
		if not swapped:  #when list is already sorted.
			break