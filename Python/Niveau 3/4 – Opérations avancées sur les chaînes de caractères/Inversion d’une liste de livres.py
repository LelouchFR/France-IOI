books = int(input())
book = [] * books
for i in range(books):
    book.append(input())
book = book[::-1]
for i in range(books):
    print(book[i])
