from selenium import webdriver
from selenium.webdriver.common.by import By

from WebScrap.base_page import BasePage
import time


class Test:
    def test_table_content(self):
        driver = webdriver.Chrome()

        try:
            # Open the website
            driver.get("https://www.iplt20.com/points-table/men/2024")

            # Wait for the page to load completely
            time.sleep(8)  # Adjust this as needed

            # Get the HTML content of the page
            # html_content = driver.page_source
            # or
            element = driver.find_element(By.XPATH, "//div[@id='pointtable']")
            html_content = element.get_attribute("outerHTML")


            expected_content = [{'POS': '1', '': '', 'TEAM': 'KKR', 'P': '14', 'W': '9', 'L': '3', 'NR': '2', 'NRR': '1.428', 'FOR': '2389/225.0', 'AGAINST': '2135/232.2', 'PTS': '20', 'RECENT FORM': 'NNWWW'}, {'POS': '2', '': '', 'TEAM': 'SRH', 'P': '14', 'W': '8', 'L': '5', 'NR': '1', 'NRR': '0.414', 'FOR': '2605/247.0', 'AGAINST': '2599/256.3', 'PTS': '17', 'RECENT FORM': 'WNWLW'}, {'POS': '3', '': '', 'TEAM': 'RR', 'P': '14', 'W': '8', 'L': '5', 'NR': '1', 'NRR': '0.273', 'FOR': '2334/252.1', 'AGAINST': '2310/257.1', 'PTS': '17', 'RECENT FORM': 'NLLLL'}, {'POS': '4', '': '', 'TEAM': 'RCB', 'P': '14', 'W': '7', 'L': '7', 'NR': '0', 'NRR': '0.459', 'FOR': '2758/269.0', 'AGAINST': '2646/270.1', 'PTS': '14', 'RECENT FORM': 'WWWWW'}, {'POS': '5', '': '', 'TEAM': 'CSK', 'P': '14', 'W': '7', 'L': '7', 'NR': '0', 'NRR': '0.392', 'FOR': '2524/274.4', 'AGAINST': '2415/274.3', 'PTS': '14', 'RECENT FORM': 'LWLWL'}, {'POS': '6', '': '', 'TEAM': 'DC', 'P': '14', 'W': '7', 'L': '7', 'NR': '0', 'NRR': '-0.377', 'FOR': '2573/267.0', 'AGAINST': '2762/275.5', 'PTS': '14', 'RECENT FORM': 'WLWLW'}, {'POS': '7', '': '', 'TEAM': 'LSG', 'P': '14', 'W': '7', 'L': '7', 'NR': '0', 'NRR': '-0.667', 'FOR': '2483/277.5', 'AGAINST': '2521/262.3', 'PTS': '14', 'RECENT FORM': 'WLLLW'}, {'POS': '8', '': '', 'TEAM': 'GT', 'P': '14', 'W': '5', 'L': '7', 'NR': '2', 'NRR': '-1.063', 'FOR': '2040/238.2', 'AGAINST': '2101/218.2', 'PTS': '12', 'RECENT FORM': 'NNWLL'}, {'POS': '9', '': '', 'TEAM': 'PBKS', 'P': '14', 'W': '5', 'L': '9', 'NR': '0', 'NRR': '-0.353', 'FOR': '2487/274.3', 'AGAINST': '2612/277.3', 'PTS': '10', 'RECENT FORM': 'LWLLW'}, {'POS': '10', '': '', 'TEAM': 'MI', 'P': '14', 'W': '4', 'L': '10', 'NR': '0', 'NRR': '-0.318', 'FOR': '2568/268.5', 'AGAINST': '2660/269.3', 'PTS': '8', 'RECENT FORM': 'LLWLL'}]

            actual_content = BasePage.extract_table_content(html_content)
            # print(actual_content)
            assert actual_content == expected_content, f"Expected {expected_content}, but got {actual_content}"

        finally:
            # Close the browser
            driver.quit()

