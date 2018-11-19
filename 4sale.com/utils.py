def generate_property_dict(data):
    d = {'title': 'Property for ' + data['type'] + ' at ' + data['address'],
         'type': data['type'],
         'locality': data['locality'],
         'city': data['city'],
         'pincode': data['pincode'],
         'address': data['address'],
         'short_description': data['short_description'],
         'bedrooms': int(data['bedrooms']),
         'bathrooms': int(data['bathrooms']),
         'patio': int(data['patio']),
         'area': float(data['area']),
         'cost': float(data['cost']),
         'latitude': float(data['lat']),
         'longitude': float(data['lng'])}
    return d
def deco_generate_property_analytics_dict(fun):
    fun.d={}
    return fun

@deco_generate_property_analytics_dict
def generate_property_analytics_dict(dict1, dict2):
    for place in dict1:
        fun.d[place + '1'] = dict1[place][place + '1']['name']
        fun.d[place + '2'] = dict1[place][place + '2']['name']
    for place in dict2:
        fun.d['distance_' + place + '1'] = dict2[place][place + '1']['distance']
        fun.d['distance_' + place + '2'] = dict2[place][place + '2']['distance']
        fun.d['time_' + place + '1'] = dict2[place][place + '1']['time']
        fun.d['time_' + place + '2'] = dict2[place][place + '2']['time']
        fun.d['message_' + place + '1'] = dict2[place][place + '1']['message']
        fun.d['message_' + place + '2'] = dict2[place][place + '2']['message']
    return d

def deco_generate_tag_list(fun):
    fun.tag_list = []
    return fun

@deco_generate_tag_list
def generate_tag_list(tags):
    for tag in tags:
        for k, v in tag.items():
            fun.tag_list.append(v)
    return fun.tag_list

def deco_normalize(fun):
    fun.output_string = ''
    return fun

@deco_normalize
def normalize(string):
    for c in string:
        if(c != '\'' and c != '"'):
            output_string += c
    return output_string


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
