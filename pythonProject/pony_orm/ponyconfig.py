from pony.orm import *

# 1
db = Database()
# 2
db.bind(provider='mysql', host='localhost', user='root', passwd='', db='biblio')



