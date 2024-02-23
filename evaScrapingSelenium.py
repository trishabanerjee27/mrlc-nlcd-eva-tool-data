from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import time

def extract_table_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', {'class': 'summary-table'})
    data = []
    headers = [header.text.strip() for header in table.find_all('th')]

    # Extract location info
    location_title, location_specification = extract_location_info(soup)

    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        row_data = {headers[i]: cell.text.strip() for i, cell in enumerate(cells)}
        # Append location info to each row
        row_data['Location Title'] = location_title
        row_data['Location Specification'] = location_specification
        data.append(row_data)

    return data, headers

def extract_location_info(soup):
    location_title = soup.find('h1', {'class': 'location-title'}).text.strip()
    location_specification = soup.find('p', {'class': 'location-specification'}).small.text.strip()
    return location_title, location_specification

def fetch_eva(driver, state, county):
    driver.get("https://www.mrlc.gov/eva/")
    driver.find_element(By.ID, "stateSelector").click()
    driver.find_element(By.CSS_SELECTOR, f"option:nth-child({state})").click()
    driver.find_element(By.ID, "countySelector").click()
    driver.find_element(By.CSS_SELECTOR, f"#countySelector > option:nth-child({county})").click()
    driver.find_element(By.CSS_SELECTOR, ".splash-button").click()
    time.sleep(60)  
    return driver.page_source

driver = webdriver.Firefox()
driver.set_window_size(550, 691)

all_data = []
headers = []

with open('eva_data_extract22.csv', 'w', newline='', encoding='utf-8') as file:
    writer = None

    for i in range(17, 51):
        for j in range(2, 300):
            try:
                page_source = fetch_eva(driver, str(i), str(j))
                table_data, headers = extract_table_data(page_source)
                all_data.extend(table_data)

                if not writer:
                    headers.extend(['Location Title', 'Location Specification'])
                    writer = csv.DictWriter(file, fieldnames=headers)
                    writer.writeheader()

                for row in table_data:
                    writer.writerow(row)

            except Exception as e:
                print(f"Error processing state {i}, county {j}: {e}")
                break

driver.quit()
