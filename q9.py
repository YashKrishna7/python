def example(filename):
    ext=filename.split(".")[-1]
    if ext=="pdf":
        return 'pdf*'
    else:
        return ext
print(example("document.pdf"))
print(example("image.jpg"))
    