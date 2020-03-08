import json
from datetime import datetime
from elasticsearch import Elasticsearch, helpers

def load_elasticsearch( data_file, index_name):
    client = Elasticsearch("localhost:9200")

    with open(data_file) as f:
        doc_list = json.load(f)

    for i in range(len(doc_list)):
        try:
            doc_list[i]['reduction_amount']= int(doc_list[i]['reduction_amount'])
            doc_list[i]['fine_amount']= int(doc_list[i]['fine_amount'])
        except:
            doc_list[i]['reduction_amount']= 0
            doc_list[i]['fine_amount'] = 0
        doc_list[i]['timestamp'] = datetime.strptime(doc_list[i]['issue_date'],"%m/%d/%Y")
    
    try:
        print("\n Attempting to index the list of docs")
        resp = helpers.bulk(
                client,
                doc_list,
                index = index_name,
                doc_type = "nycdata")
        #print ("helpers.bulk() RESPONSE:", resp)
        #print ("helpers.bulk() RESPONSE:", json.dumps(resp, indent=4))
    
    except Exception as err:
    
        print("Elasticsearch helpers.bulk() ERROR:", err)
    
