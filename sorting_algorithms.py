'''The yield statement suspends functions execution and sends a value back to the caller, but retains 
  	enough state to enable function to resume where it is left off. When resumed, the function continues 
  	execution immediately after the last yield run. This allows its code to produce a series of values over time, 
  	rather than computing them at once '''


def swap(li, i, j):
	if i != j:
		li[i], li[j] = li[j], li[i]