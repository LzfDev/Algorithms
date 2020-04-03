# 归纳证明
def quicksock(arr):
	print('do...', arr)
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]
		less = [i for i in arr[1:] if i <= pivot]
		greater = [i for i in arr[1:] if i > pivot]
		return quicksock(less) + [pivot] + quicksock(greater)

print(quicksock([10, 2, 4, 7, 5]))