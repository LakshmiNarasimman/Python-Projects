'''
Created on 23-Oct-2017

@author: bigdata
'''
from algoliasearch import algoliasearch
import json
import csv
import pandas as pd
from collections import OrderedDict
import os, sys
import math
import boto

#help(algoliasearch)
AWS_ACCESS_KEY_ID = 'AKIAJH254LBT4VNVUAQA'
AWS_SECRET_ACCESS_KEY = '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'
def connect_algoliaSearch():
    client = algoliasearch.Client("ODGJXD8XE6", "c3a128d32ef5f9726f97e5666387815d")
    index = client.init_index('products_v3')
    hits = []
    for hit in index.browse_all({"query": "iphone 6 64 gb"}):
        json_string = json.dumps(hit,sort_keys=False)
        dicts= json.loads(json_string, encoding='utf-8')
        json_data = open('/home/bigdata/bigdata_noahdata/Alex_Py/test_write.csv', 'w')
        csvwriter = csv.writer(json_data)
        count = 0
        if count == 0:
            header = dicts.keys()
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(dicts.values())
        
        
   

'''
with open('/home/bigdata/bigdata_noahdata/Alex_Py/your_filename.json', 'w') as f:
    json.dump(hits, f)
'''


def upload_file(s3, bucketname, file_path):

        b = s3.get_bucket(bucketname)

        filename = os.path.basename(file_path)
        k = b.new_key(filename)

        mp = b.initiate_multipart_upload(filename)

        source_size = os.stat(file_path).st_size
        bytes_per_chunk = 5000*1024*1024
        chunks_count = int(math.ceil(source_size / float(bytes_per_chunk)))

        for i in range(chunks_count):
                offset = i * bytes_per_chunk
                remaining_bytes = source_size - offset
                bytes = min([bytes_per_chunk, remaining_bytes])
                part_num = i + 1

                print "uploading part " + str(part_num) + " of " + str(chunks_count)

                with open(file_path, 'r') as fp:
                        fp.seek(offset)
                        mp.upload_part_from_file(fp=fp, part_num=part_num, size=bytes)

        if len(mp.get_all_parts()) == chunks_count:
                mp.complete_upload()
                print "upload_file done"
        else:
                mp.cancel_upload()
                print "upload_file failed"
                
                 

if __name__ == "__main__":
    #s3 = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    #upload_file(s3, "price-alex-test", "/home/bigdata/bigdata_noahdata/Alex_Py/temp.csv")
    connect_algoliaSearch()

#         if len(sys.argv) != 3:
#                 print "usage: python s3upload.py bucketname filepath"
#                 exit(0)
# 
#         bucketname = sys.argv[1]
# 
#         filepath = sys.argv[2]

        