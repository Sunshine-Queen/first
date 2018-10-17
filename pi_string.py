filename='pi_digits.txt'

with open(filename) as file_object:
    lines=file_object.readlines()

pi_string=''
for line in lines:
    # pi_string+=line.rstrip()
    # 删除每行末尾的换行符
    pi_string+=line.strip()
print(pi_string)
print(len(pi_string))
