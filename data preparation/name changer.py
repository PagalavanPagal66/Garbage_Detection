
import os
os.getcwd()
collection = "Garbage blob dataset/"
for i, filename in enumerate(os.listdir(collection)):
  print(filename)
  os.rename(collection + "/" + filename, collection + "/garbage_blog" + str(i) + ".jpg")