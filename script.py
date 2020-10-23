import urllib.parse as urlparse
from urllib.parse import parse_qs
import csv
from copy import deepcopy

class YTrimmer():
    def __init__(self,filename,annotator_name,converted_filename,sort_index):
        self.converted_filename = converted_filename
        self.sort_index = sort_index
        self.annotator_name = annotator_name
        self.data_csv = []
        with open(filename,'r') as f:
            data_csv_read = csv.reader(f)
            for i in data_csv_read:
                self.data_csv.append(i)
        self.base_url = 'https://www.youtubetrimmer.com/view/?v='

    def convert_row(self,row):
        parsed = urlparse.urlparse(row[2])
        vid_hash = parse_qs(parsed.query)['v'][0]
        
        t_start = int(row[3].split(':')[0])*60 + int(row[3].split(':')[1])
        t_end = int(row[4].split(':')[0])*60 + int(row[4].split(':')[1])
        
        return row[:2] + ['{0}{1}&start={2}&end={3}'.format(self.base_url,vid_hash,t_start,t_end), t_start, t_end] + [self.annotator_name] + row[5:]

    def convert_rows(self,data_csv):
        converted_data = deepcopy(data_csv)
        for i in range(len(data_csv)):
            converted_data[i] = self.convert_row(self.data_csv[i])
        converted_data.sort(key=lambda x: x[self.sort_index])
        return converted_data
    
    def write_converted_csv(self,converted_data,converted_filename):
        with open(converted_filename,'w') as f:
            data_csv_write = csv.writer(f)
            data_csv_write.writerows(converted_data)
    
    def convert(self):
        self.converted_data = self.convert_rows(self.data_csv)
        self.write_converted_csv(self.converted_data, self.converted_filename)

if __name__ == '__main__':
    filename = input("Path to file to convert: ")
    annotator_name = input("Annotator Name: ")
    converted_filename = input("Path to converted file: ")
    converter = YTrimmer(filename, annotator_name, converted_filename, -1)
    converter.convert()