#Adding 
Book1 = {
    "Title":"Lightning in the Storm" , "Author":"NoName"
}
print(Book1)
Book1["Price"] = 23
print(Book1)
#Updating
Book1["Author"] = "Sebistan Crambling"
print(Book1)
#Deleting
del Book1["Price"]
print(Book1)