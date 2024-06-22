from bs4 import BeautifulSoup

class BasePage:
    @staticmethod
    def extract_table_content(html, table_id=None, table_class=None):
        """
        Extracts content from a table in the provided HTML.

        Parameters:
        - html (str): HTML content as a string.
        - table_id (str): The id of the table to extract. If None, all tables will be considered.
        - table_class (str): The class of the table to extract. If None, all tables will be considered.

        Returns:
        - List of dictionaries: Each dictionary represents a row with column names as keys.
        """
        soup = BeautifulSoup(html, 'html.parser')

        if table_id:
            table = soup.find('table', id=table_id)
        elif table_class:
            table = soup.find('table', class_=table_class)
        else:
            table = soup.find('table')

        if not table:
            raise ValueError("No table found with the given identifier")

        headers = [th.text.strip() for th in table.find('tr').find_all('th')]
        rows = []

        for row in table.find_all('tr')[1:]:  # Skip the header row
            cells = row.find_all('td')
            if len(cells) == len(headers):  # Ensure the row matches the header length
                row_data = {headers[i]: cells[i].text.strip() for i in range(len(headers))}
                rows.append(row_data)

        return rows
