with open("john.txt", "r") as f: # context manager
    content = f.read()
    print(content)

    # No need to write f.close() because file is already close by default when using with synax

