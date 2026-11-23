import os

os.makedirs("/output", exist_ok=True)
pitch = "Imagine typing your app idea and watching it turn into a real, working app in minutes — it's free to enter on make.fun, and the best builds win real cash."
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(pitch)
