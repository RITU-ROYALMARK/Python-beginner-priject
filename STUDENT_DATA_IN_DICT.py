# This is a student data in an  ested dict

data_structure = {
                  '001':{'name':'rithin mp','age':'22','email':'rithinmp002@gmail.com'},
                  '002':{'name':'surya s','age':'19','email':'surya2005@gmail.com'},
                  '003':{'name':'amulya rao','age':'25','email':'amulyarao002@gmail.com'},
                  '004':{'name':'sreedin','age':'25','email':'sreedin002@gmail.com'},
                  '005':{'name':'shara','age':'24','email':'shara02@gmail.com'},
                  '006':{'name':'rahul','age':'23','email':'roysl002@gmail.com'},
                  '007':{'name':'jhon whick','age':'26','email':'jhon02@gmail.com'}
                  }

print(f"{'id':<12}{'name':<17}{'age':<15}{'email':<15}")
print('-'*60)

for data in data_structure.keys():
    # the id is to print the id in the dict
    id = data
    # and now for the name
    name = data_structure[data]['name']
    # now age
    age = data_structure[data]['age']
    #now email
    email = data_structure[data]['email']

    print(f"{id:<12}{name:<17}{age:<14}{email:<14}")

