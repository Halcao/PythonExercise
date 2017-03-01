import xlwt
import json
import sys

def main():
	f = open(sys.argv[1], 'r')
	data = json.loads(f.read())
	workbook = xlwt.Workbook(encoding='utf-8')
	worksheet = workbook.add_sheet('my worksheet')
	for line in data:
		worksheet.write(int(line)-1, 0, label=line)
		for index, item in enumerate(data[line]):
			worksheet.write(int(line)-1, index+1, label = item)
	workbook.save('Excel_test.xls')


if __name__ == '__main__':
	main()
