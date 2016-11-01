
# coding: utf-8

# In[25]:

import csv
from datetime import datetime
from datetime import timedelta

class Log():
    
    def __init__(self):

        self.log_list = []
        
    def __str__(self):
        #return "<LogLines size: {0}>".format(self.size)
        return "<Log List: {0}>".format(log_list)
    
    def __repr__(self):
        return self.__str__()

    def add(self, id, created_date, start_time, end_time, volume):
        
        datetime_format = "%Y-%m-%d %H:%M:%S"
        time_format = '%H:%M:%S' 

        created_datetime = datetime.strptime(created_date + ' ' + start_time, datetime_format)

        try: 
            tdelta = datetime.strptime(end_time, time_format) - datetime.strptime(start_time, time_format)
        except:
            print 'Error in transaction line {0}. Either start or end time were in wrong format'.format(id)
            return    
            
        if tdelta.days < 0:
            end_datetime = datetime.strptime(created_date + ' ' + end_time, datetime_format) + timedelta(days=1)
            tdelta = end_datetime - created_datetime
        
        execution_time = tdelta
        
        if volume.isdigit(): size = float(volume)/1024
        else: size = 0
        
        output_obj = {
            'id': id,
            'created_datetime': created_datetime.strftime(datetime_format),
            'execution_time': str(execution_time),
            'size': "{0:.2f}".format(round(size,2))
        }
                
        self.log_list.append(output_obj)    
        print output_obj
               
        

#f = open('UsersImportSimpleSample.csv')
f = open('log.csv')

csv_f = csv.reader(f)
temp_list = []

log_obj = Log()

for ind, row in enumerate(csv_f):
    temp_list.append(row)

    if ind >= 1:
        log_obj.add(row[0], row[1], row[2], row[3], row[4])

    
print temp_list


# In[ ]:



