# file_path = "LICENSE"
#
#
# try:
#     file_obj = open(file_path, mode='r', encoding='utf-8')
#     print(f"{file_obj=}, {type(file_obj)=}")
#     print(f"{file_obj.closed=}")
#     print(f"{file_obj.encoding=}")
#
#     file_content = file_obj.read()
#     print(f"{file_content=}, {type(file_content)=}")
#
    # file_obj.close()
#     print(f"{file_obj=}, {type(file_obj)=}")
#     print(f"{file_obj.closed=}")
#
# except FileNotFoundError:
#     print(f"You should create a file at {file_path=}")
###########################################################################
# file_path = "LICENSE"
#
# try:
#     with open(file_path, mode='r', encoding='utf-8') as fh:
#         data = fh.read()
#
#         print(f"{data=}, {type(data)=}")
#         print(f"{fh=}, {type(fh)=}")
#         print(f"{fh.encoding=}")
#         print(f"{fh.closed=}")
#
#     print(f"{fh=}, {type(fh)=}")
#     print(f"{fh.closed=}")
#
# except FileNotFoundError:
#     print(f"You should create a file at {file_path=}")
###########################################################################
# sample_data = "sample strings\nfor sample file"
# file_path = "write_sample.txt"
#
#
# with open(file_path, mode='wt+', encoding='utf-8') as fh:
#     fh.write(sample_data)
###########################################################################
# file_path = "write_sample.txt"
#
# try:
#     with open(file_path, 'r+') as fh:
#         while data := fh.readline():
#             print(f"{data=}")
#
#         print(f"last {data=}")
#
# except FileNotFoundError:
#     print(f"You should create a file at {file_path=}")
###########################################################################
# file_path = "write_sample.txt"
#
# try:
#     with open(file_path) as fh:
#         lines = fh.readlines()
#         print(f"{lines=}")
#
# except FileNotFoundError:
#     print(f"You should create a file at {file_path=}")
###########################################################################
# file_path = "write_sample_1.txt"
# lines = ['new file\n', 'new method\n', 'new result\n']
#
# try:
#     with open(file_path, 'w') as fh:
#         fh.writelines(lines)
#
# except FileNotFoundError:
#     print(f"You should create a file at {file_path=}")
###########################################################################
# file_path = "LICENSE"
#
#
# with open(file_path, "rb") as fh:
#     first_three_symbols = fh.read(3)
#
#     print(f"{first_three_symbols=}")
#     print(f"{fh.tell()=}")
#
#     fh.seek(2, 0)  # whence is 0 by default
#     print(f"{fh.tell()=}")
#
#     data = fh.readline()
#     print(f"{data=}")
#
#     fh.seek(5, 1)
#     some_five_symbols = fh.read(5)
#     print(f"{some_five_symbols=}")
#
#     fh.seek(-10, 2)
#     file_end = fh.read()
#     print(f"{file_end=}")
###########################################################################
# import json
#
#
# some_object = {
#     "list": [1, 2, 3],
#     "bool": True,
#     "none": None,
#     "string": "string",
#     "tuple": (1, 2, 3),
#     "dict": {"a": 1, "b": 2},
# }

# json_string = json.dumps(some_object)
# print(f"{type(json_string)=}, {json_string=}")
#
# restored_object = json.loads(json_string)
# print(f"{type(restored_object)=}, {restored_object=}")
#
# with open("statham.json", "w") as fh:
#     json.dump(some_object, fh, indent=4, sort_keys=True)
#
# with open("statham.json", "r") as fh:
#     data = json.load(fh)
#     print(f"{data=}, {type(data)=}")
###########################################################################
import csv


# with open('table.csv', 'w', newline='') as fh:
#     writer_obj = csv.writer(fh)
#     writer_obj.writerow(["You", "just", "used", "csv", "module"])
#     writer_obj.writerow(["You", "just", "again used", "csv", "module"])
###########################################################################
# with open('table.csv', 'a', newline='') as fh:
#     writer_obj = csv.writer(fh)
#     writer_obj.writerows([
#         ["So", "you", "studying", "csv", "module"],
#         ["one", "more", "row", "to", "csv"],
#         ["again", "new", "record", "to", "file"],
#     ])
###########################################################################
# with open('table.csv', 'r') as fh:
#     reader_obj = csv.reader(fh)
#
#     for row in reader_obj:
#         print(f"{type(row)=}, {row=}")
###########################################################################
# with open('demographic.csv', 'w', newline='') as fh:
#     fieldnames = ['name', 'age']
#     writer = csv.DictWriter(fh, fieldnames=fieldnames)
#     writer.writeheader()
#
#     writer.writerow({'name': 'Asterisk', 'age': 27})
#     writer.writerow({'name': 'Tor', 'age': 69})
#     writer.writerow({'name': 'Jerry', 'age': 18})
###########################################################################
with open('demographic.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(
            f"{row=}, {type(row)=}, "
            f"{row['name']=}, {row['age']=}"
        )