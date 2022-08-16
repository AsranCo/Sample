import os

for root, dirs, files in os.walk("/home/ali/snap", topdown=False):
    for name in files:
        print(os.path.join(root, name))
