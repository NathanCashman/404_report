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
kibana_mac = []
combined_data = []

# pull the lineport from the kibana file as we want to preserve this to replace the one provided in OSS' report
with open(kibana_file) as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    lineCount = 0
    for row in data:
        if lineCount == 0:
            lineCount += 1
        else:
            kibana_mac.append(row[6])

# pull required data from the OSS file and combine this with the lineport from kibana that we gathered earlier
with open(oss_file) as oss_file_csv:
    odata = csv.reader(oss_file_csv, delimiter=',')
    lineCount = 0
    i = 0
    for row in odata:
        if lineCount == 0:
            lineCount += 1
        else:
            combined_data.append([row[0], row[1], row[2], row[3], row[4], row[5], kibana_mac[i]])
            lineCount += 1
            i += 1

# create new file and write required data to it
with open('/Users/nathancashman/Documents/testing.csv', mode='w', newline='') as outfile:
    outfile_writer = csv.writer(outfile)
    outfile_writer.writerow(['Mac', 'DeviceProfileType', 'Company', 'Company enddate', 'defaultdomain', 'ServerName',
                             'LinePort', 'Device enddate', 'Completed', 'Batch Number', 'Error'])
    for item in combined_data:
        outfile_writer.writerow(item)

print(f'{lineCount} lines processed.')
