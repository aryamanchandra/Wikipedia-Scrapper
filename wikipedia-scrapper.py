import wikipediaapi

wikipedia_en = wikipediaapi.Wikipedia("en")

url = input("Enter wikipedia url ")

initialrem = ["https://en.wikipedia.org/wiki/", "!", " ", "*"]

for i in initialrem:
    url = url.replace(i, "")


page = wikipedia_en.page(url)
summary = page.summary
title = page.title

L = list((f"{title} \n", f"{summary}"))

with open(f"{title}.txt", "w", encoding="utf-8") as files:
    for i in L:
        file = files.write(i)
    files.close()

print("Task Complete")

