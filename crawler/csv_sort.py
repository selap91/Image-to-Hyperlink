import csv


read_file = open('C:/Users/selap/PycharmProjects/ClickURL/data/google_URL.csv', 'r')
new_file = open('C:/Users/selap/PycharmProjects/ClickURL/data/URL.csv', 'w', newline='')

rd = csv.reader(read_file, delimiter=',')
wr = csv.writer(new_file, delimiter=',')

num = 0
for row in rd:
    #print(row[0])
    if row[0][0] == 'D' and num == 0:
        num = 1
    elif row[0][0] == 'D' and num == 1:
        num = 2
    elif row[0][0] != 'D':
        num = 0

    if num == 0 or num == 1:
        if len(row[0]) > 60:
            for i in range(45, 60, 1):
                if row[0][i] == '/':
                    wr.writerow([row[0][0:i+1]])
                    break
                elif i == 59:
                    if row[0][59] == '-':
                        wr.writerow([row[0][0:59]])
                        break
                    else:
                        wr.writerow([row[0][0:60]])
                        break
        else:
            wr.writerow([row[0]])
    elif num == 2:
        continue
