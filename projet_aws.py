#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
import os
 
def upload_files(path):
    
    #ouverture d'une session aws
    session = boto3.Session(
        aws_access_key_id='AKIAJIBCU4UTCFRAGDAA',
        aws_secret_access_key='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',
        region_name='Paris'
    )
    s3 = boto3.resource('s3')
    
    #creation d'un nouveau compartiment
    s3.create_bucket(Bucket='amal88', CreateBucketConfiguration={'LocationConstraint': 'eu-west-3'})

    bucket = s3.Bucket('amal88')
    
    #chargement et stockage des données
    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                bucket.put_object(Key=full_path[len(path)+1:], Body=data)
                

if __name__ == "__main__":
    path= input('Entrez le chemin complet de vos données:\n')
    upload_files(path)


# In[ ]:





# In[ ]:




