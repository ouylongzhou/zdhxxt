


p = ["'"+ str(i) +"'"for i in range(4600, 4700)]

print(p)

sql = "select * from lyy_eqiupment where version in ({})".format(",".join(p))

print(sql)