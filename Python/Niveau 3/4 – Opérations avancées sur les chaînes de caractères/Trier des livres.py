books = int(input())
book = []

for i in range(books):
   book.append(input())

book.sort()

for i in range(books):
   print(book[i])
