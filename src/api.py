from sodapy import Socrata
import os
def get_data(page_size, current_page):
    key = os.environ.get('APP_KEY')
    client = Socrata(
		"data.cityofnewyork.us",
        key
	)	
    output = client.get("nc67-uf89",limit = page_size, offset =page_size*current_page)
    return(output)
