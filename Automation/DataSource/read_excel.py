import xlrd

class read_excel():
    def get_data_from_excel(file_path,sheet_name):
        # create an empty ist tp get data
        rows = []
        # open excel workboook
        book = xlrd.open_workbook(file_path)
        # get excel sheet
        sheet = book.sheet_by_name(sheet_name)
        for row_indx in range(1,sheet.nrows):
            rows.append(list(sheet.row_values(row_indx, 0 , sheet.ncols)))

        return rows

