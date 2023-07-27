import os


os.environ["VERSION_NUM_LAST"] = "100.1"
print(os.environ["VERSION_NUM_LAST"])
with open("version.txt", "w") as file:
    file.write("100.1")
