import csv
import sys

# Check that two files have been provided, otherwise print guide on usage and exit
if len(sys.argv) < 2:
    print("usage: python device_report.py [kibana_file] [oss_file]")
    print("example: python device_report.py /home/ncashman/kibana_404_28Jun.csv /home/ncashman/oss_404_28Jun.csv")
    sys.exit(0)

# set file variables from the OSS and Kibana reports for manipulation
kibana_file = sys.argv[1]
# oss_file = sys.argv[2]
kibana_mac = []

# pull the lineport from the kibana file as we want to preserve this to replace the one provided in OSS' report
with open(kibana_file) as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    lineCount = 0
    for row in data:
        if lineCount == 0:
            lineCount += 1
        else:
            kibana_mac.append(row[6])

with open('/Users/nathancashman/Documents/testing.csv', mode='w', newline='') as outfile:
    outfile_writer = csv.writer(outfile)
    for item in kibana_mac:
        outfile_writer.writerow([item])
