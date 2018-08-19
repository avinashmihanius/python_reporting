import xlsxwriter
import sys
import json
import pprint

class FileManagement():
    def __init__(self):
        self.json_file_name = "response.json"
        self.excel_file_name = "output.xlsx"
        self.array_first_name = []
        self.array_last_name = []
        self.array_total = []

    def read_file(self):
        try:
            with open(self.json_file_name, 'r') as data_file:
                data = json.load(data_file)
                pprint.pprint(data)
                for meta_data in data["data"]:
                    total=int(meta_data["id"])
                    self.array_total.append(total)
                    pprint.pprint("total={0}".format(total))

        except:
            print("Unexpected error :", sys.exc_info()[0])
            raise

    def write_to_excel(self):
        workbook = xlsxwriter.Workbook(self.excel_file_name)
        worksheet = workbook.add_worksheet()
        for index, value in enumerate(self.array_total):
            worksheet.write(index, 0, self.array_total[index])
        workbook.close()

if __name__ == "__main__":
    fileManagement = FileManagement()
    fileManagement.read_file()
    fileManagement.write_to_excel()