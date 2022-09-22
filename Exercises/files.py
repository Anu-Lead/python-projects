# import pathlib
#
# from pathlib import Path
#
# new_dir = Path.home() / "new_directory"
# # new_dir.mkdir()
#
# home = pathlib.Path.home()
#
# print(home)
#
# print(new_dir.exists())
#
# print(new_dir.is_dir())
#
# # print(list(home.glob("Goodness of God")))
#
# nested_dir = new_dir / "folder_a" / "folder_b"
# # nested_dir.mkdir()
#
# # nested_dir.mkdir(parents=True)
# # path.mkdir(parents=True, exist_ok=True)
# # file_path = new_dir / "file1.txt"
# # print(file_path.exists())
#
#
# import csv
#
# file_path = Path.home() / "temperatures.csv"
# file = file_path.open(mode="w", encoding="utf-8")
# # with file_path.open(mode="w", encoding="utf-8") as adisa:
#
# writer = csv.writer(file)
#
# daily_temperatures = [
#     [68, 65, 68, 70, 74, 72],
#     [67, 67, 70, 72, 72, 70],
#     [68, 70, 74, 76, 74, 73],
# ]
#
# for temp_list in daily_temperatures:
#     writer.writerow(temp_list)
# file = file_path.open(mode="r", encoding="utf-8")
#
# file_path = file.read()
#
# for temp_list in daily_temperatures:
#     print(temp_list)
#
# file = file_path.open(mode="r", encoding="utf-8")
# reader = csv.reader(file)
#
# for row in reader:
#     print(row)
# file.close()


# with open("temp_file.txt", mode="w", encoding="utf-8") as file_object:
#     print(file_object.tell())
#     file_object.write("Life is Good With Money\n")
#     # print(file_object.seek(10))
#     print(file_object.tell())
#     file_object.write("Life is Good With Money\n")


with open("temp_file.txt", mode="r", encoding="utf-8") as file:
    print(file.read())
    print(file.readline())
    print(file.readlines())

from pathlib import Path

path = Path("./folder/sub-folder/text.txt")

path.parent.mkdir(parents=True, exist_ok=True)
path.touch(exist_ok=True)

print(path.resolve())
