books = int(input())
bfr = ""

for i in range(books):
   book = input()
   if bfr < book:
      print(book)
      bfr = book
