employee={'Alex':1500,'John':1200,'Peter':1400}
def test(employee):
    new = {'Buck':200,'bob':3000}
    employee.update(new)
    print("Insude the funtion",employee)
    return
test(employee)
print("Outside the function:",employee)
