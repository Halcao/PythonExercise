import xlwt
import json
import sys
# usage: python this.py *.json *.xls

def main():
	f = open(sys.argv[1], 'r')
	data = json.loads(f.read())
	workbook = xlwt.Workbook(encoding='utf-8')
	worksheet = workbook.add_sheet('my worksheet')
	for line in data:
		worksheet.write(int(line)-1, 0, label=line)
		worksheet.write(int(line)-1, 1, label = data[line])
	workbook.save(sys.argv[2])


if __name__ == '__main__':
	main()
