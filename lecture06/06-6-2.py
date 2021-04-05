import os


for(path, dir, files) in os.walk("F:/python/projects/python_study/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == ".py":
            print("%s /%s" % (path, filename))

