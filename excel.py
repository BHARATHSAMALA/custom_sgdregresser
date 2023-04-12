from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill

# Load the workbook
wb = load_workbook('example.xlsx')

# Select the sheet to work with
ws = wb.active

# Define the color coding
color_codes = {
    'Low': PatternFill(start_color='00FF00', end_color='00FF00', fill_type='solid'),
    'Medium': PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid'),
    'High': PatternFill(start_color='FF0000', end_color='FF0000', fill_type='solid')
}

# Iterate over the rows and columns to apply color coding
for row in ws.iter_rows(min_row=2):
    for cell in row[1:]:
        if cell.value is not None:
            # Calculate the grade based on the cell value
            grade = ''
            if cell.value <= 0.33:
                grade = 'Low'
            elif cell.value > 0.33 and cell.value <= 0.67:
                grade = 'Medium'
            elif cell.value > 0.67:
                grade = 'High'
            # Apply the fill color based on the grade
            cell.fill = color_codes[grade]

# Save the workbook
wb.save('example.xlsx')
