# To get value from key
Employee = {
    "ID":"1112768","City":"Monaco","Income(annual)":1200000
}
print(Employee.get("ID"))
print(Employee.get("IDs")) #will return None if key not found
print(Employee.get("IDs","Key Not Found"))#custom message if key not found
#To get all the keys in the dictionary
print(Employee.keys())
print(list(Employee.keys()))
#To get all the values in the dictionary
print(Employee.values())
print(list(Employee.values()))
#To get all the items(key : value pair) in the dictionary
print(Employee.items())
print(list(Employee.items()))
Orange={
  "color":"orange","vitamin":"D","properties":"zesty"
}
#deleting
p = Orange.pop("properties")
print(p)
print(Orange)
# print(Orange.pop("F")) will return error KeyError
print(Orange.pop("a","Not Found"))
print(Orange.popitem())#will remove last item
#Clear 
print(Orange.clear())
print(Orange)
# 1112768
# None
# Key Not Found
# dict_keys(['ID', 'City', 'Income(annual)'])
# ['ID', 'City', 'Income(annual)']
# dict_values(['1112768', 'Monaco', 1200000])
# ['1112768', 'Monaco', 1200000]
# dict_items([('ID', '1112768'), ('City', 'Monaco'), ('Income(annual)', 1200000)])
# [('ID', '1112768'), ('City', 'Monaco'), ('Income(annual)', 1200000)]
# zesty
# {'color': 'orange', 'vitamin': 'D'}
# Not Found
# ('vitamin', 'D')
# None
#{}