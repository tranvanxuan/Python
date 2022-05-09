csv_mapping_list = []

with open("data.csv") as my_data:
    line_count = 0  # tao bien dem dong
    for line in my_data:  # duyet qua du lieu
        # tao 1 list, use Comprehension , 	[ f(x) for x in iterable if condition ]
        # val.strip () cat khoang trang 2 ben neu co
        # val moi gia tri trong dong duoc ngan cach boi dau ,
        row_list = [val.strip() for val in line.split(",")]
        if line_count == 0:  # vong lap dau tien
            header = row_list  # lay ra ten cac khoa cua dict
        else:
            row_dict = {}  # tao tu dien
            for i, key in enumerate(header):
                row_dict[key] = row_list[i]
            csv_mapping_list.append(row_dict)
        line_count += 1
# print(csv_mapping_list)

# CSV reader solution
import csv

csv_mapping_list = []
with open("data.csv") as my_data:
    csv_reader = csv.reader(my_data, delimiter=",")
    line_count = 0
    for line in csv_reader:
        if line_count == 0:
            header = line
        else:
            row_dict = {key: value for key, value in zip(header, line)}
            csv_mapping_list.append(row_dict)
        line_count += 1

# CSV DictReader solution
import csv

with open("data.csv") as my_data:
    csv_mapping_list = list(csv.DictReader(my_data))
print(csv_mapping_list)
