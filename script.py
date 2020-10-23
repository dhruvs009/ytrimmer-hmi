import urllib.parse as urlparse
from urllib.parse import parse_qs
import csv

class YTrimmer():
    def __init__(self,filename):
        self.data_csv = []
        with open(filename,'r') as f:
            data_csv_read = csv.reader(f)
            for i in data_csv_read:
                self.data_csv.append(i)
        self.base_url = 'https://www.youtubetrimmer.com/view/?v='
        self.convert_to_csv()
    
    def convert_row(self,row):
        parsed = urlparse.urlparse(row[0])
        vid_hash = parse_qs(parsed.query)['v'][0]
        
        t_start = int(row[1].split(':')[0])*60 + int(row[1].split(':')[1])
        t_end = int(row[2].split(':')[0])*60 + int(row[2].split(':')[1])

        tag = row[3]
        
        return '{0}{1}&start={2}&end={3},{2},{3},{4}'.format(self.base_url,vid_hash,t_start,t_end,tag)

    def convert_to_csv(self):
        for i in self.data_csv:
            print(self.convert_row(i))

YTrimmer('testsheet.csv')