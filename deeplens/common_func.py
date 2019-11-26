from django.db import models
index_dic={}
base='value'
for i in range(14):
    index_dic[base+str(i+1)]=round((i/146),4)

