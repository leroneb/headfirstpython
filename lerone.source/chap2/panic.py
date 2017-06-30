phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.pop()
plist.pop()
plist.pop()
plist.pop()
plist.remove("D")
plist.remove("'")
plist.insert(2,' ')
plist.pop(4)
plist.insert(4, plist.pop())

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)