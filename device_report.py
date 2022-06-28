import csv
import sys

# Check that two files have been provided, otherwise print guide on usage and exit
if len(sys.argv) < 3:
    print("usage: python device_report.py [kibana_file] [oss_file]")
    print("example: python device_report.py /home/ncashman/kibana_404_28Jun.csv /home/ncashman/oss_404_28Jun.csv")
    sys.exit(0)

# set file variables from the OSS and Kibana reports for manipulation
kibana_file = sys.argv[1]
oss_file = sys.argv[2]

with open(kibana_file) as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    lineCount = 0
    for row in data:
        if lineCount == 0:
            lineCount += 1
        else:
            print(row[0])
