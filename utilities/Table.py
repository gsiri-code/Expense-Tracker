class Table:
    def __init__(self, *headers):
        self.headers = headers
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def __str__(self):
        # Determine the width of each column
        col_widths = [len(header) for header in self.headers]
        for row in self.rows:
            col_widths = [max(col_widths[i], len(str(item))) for i, item in enumerate(row)]

        # Create a horizontal rule
        hr = '+' + '+'.join(['-' * (width + 2) for width in col_widths]) + '+'

        # Create the header row
        header_row = '|' + '|'.join([f" {self.headers[i].ljust(col_widths[i])} " for i in range(len(self.headers))]) + '|'

        # Create the table rows
        table_rows = [header_row] + [
            '|' + '|'.join([f" {str(row[i]).ljust(col_widths[i])} " for i in range(len(row))]) + '|'
            for row in self.rows
        ]

        return f"{hr}\n" + f"\n{hr}\n".join(table_rows) + f"\n{hr}"

if __name__ == '__main__':
    # Usage:
    table = Table('Name', 'Age', 'City')
    table.add_row(['Alice', '25', 'New York'])
    table.add_row(['Bob', '30', 'Los Angeles'])
    table.add_row(['Charlie', '35', 'Chicago'])

    print(table)
