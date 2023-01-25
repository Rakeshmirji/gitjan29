import XLUtils
path="C:\\Users\\Admin\\Downloads\\testtdata.xlsx"
rows=XLUtils.getRowCount(path,"Sheet1")
for r in range(2,rows+1):
    username=XLUtils.readdata(path,"Sheet1",r,1)
    password=XLUtils.readdata(path,"Sheet1",r,2)
    print(username)
    print(password)
    if username == "hello":
        print("passwordppppppp")
        XLUtils.writedata(path,"Sheet1",r,3,"test is passed")
    else:
        XLUtils.writedata(path, "Sheet1", r, 3, "test is failedd")

