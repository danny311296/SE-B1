from utils import *

class Filter:
    def __init__(self):
        self.l = ['min_price','max_price','min_area','max_area']
        
    def basic_filter(self,data,db):
        d = {}
        extra_conditions = []
        tags = []
        for key,value in data.items():
            if(data[key]):
                if(key.startswith('tag')):
                    tags.append(key.split('_')[1])
                elif(key not in self.l):
                    if(key != 'type' or (key == 'type' and value!='Any')):
                        d[key] = value
                else:
                    if(key=='min_price'):
                        extra_conditions.append(" cost " + ">=" + value)
                    elif(key=='max_price'):
                        extra_conditions.append(" cost " + "<=" + value)
                    elif(key=='min_area'):
                        extra_conditions.append(" area " + ">=" + value)
                    elif(key=='max_area'):
                        extra_conditions.append(" area " + "<=" + value)
                        
        query_string = db.query_string_from_dict('properties',d)
        if('where' not in query_string.split() and len(extra_conditions) > 0):
            if(len(extra_conditions)==1):
                query_string += " where " + extra_conditions[0]
            else:    
                query_string += " where " + " and ".join(extra_conditions)
        elif(len(extra_conditions) > 0):
            if(len(extra_conditions)==1):
                query_string +=  " and " + extra_conditions[0]
            else:    
                query_string += " and " + " and ".join(extra_conditions)
        print(query_string)
        if(len(tags)==0):
            return db.execute_query_string(query_string)
        else:
            return self.checkTags(db.execute_query_string(query_string),tags,db)
        
    def checkTags(self,property_items,input_tags,db):
        items = []
        for property_item in property_items:
            tags = db.query('tags',pid=property_item['pid'],cols=['tag'])
            tags_list = generate_tag_list(tags)
            print(tags_list)
            if(all(i in tags_list for i in input_tags)):
                items.append(property_item)
        return items
            