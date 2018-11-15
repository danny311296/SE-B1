class Filter:
    def __init__(self):
        self.l = ['min_price','max_price','min_area','max_area']
        
    def basic_filter(self,data,db):
        d = {}
        extra_conditions = []
        for key,value in data.items():
            if(data[key]):
                if(key not in self.l):
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
        return db.execute_query_string(query_string)