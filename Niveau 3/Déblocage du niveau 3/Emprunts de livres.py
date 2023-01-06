books, days = map(int, input().split())
available = [0] * books

def canTakeIt(book, day, duration):
	result = False
	if available[book] <= day:
		available[book] = day + duration
		result = True
	return result

for day in range(days):
	clients = int(input())
	for _ in range(clients):
		book, duration = map(int, input().split())
		if canTakeIt(book, day, duration):
			print(1)
		else:
			print(0)