books = int(input())

for i in range(books):
    title = input()
    newTitle = title.replace(" ", "")
    if newTitle.lower() == newTitle[::-1].lower():
        print(title)
