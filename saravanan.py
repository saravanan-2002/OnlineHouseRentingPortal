class User:
    def __init__(self):
        pass
    def rent_user(self):
        pass
class Owner(User):
    def __init__(self,data):
        User.__init__(self)
        self.data=data 
    def post(self): 
        print("Enter locatity:",end=" ")
        locatity_input=input().strip()
        print("Enter city:",end=" ")
        city_input=input().strip()
        print("Enter square_feet:",end=" ")
        square_feet_input=input().strip()
        print("Enter type:",end=" ")
        type_input=input().strip()
        print("Enter rent:",end=" ")
        rent_input=input().strip()
        print("Enter owner_id:",end=" ")
        owner_id_input=input().strip()
        data[locatity_input]=[city_input,square_feet_input,type_input,rent_input,owner_id_input]
    def remove(self):
        print("Enter name for removal:",end=" ")
        remove_input=input().strip()
        data.pop(remove_input)
        
class Tenant(User):
    def __init__(self):
        User.__init__(self)
        
class Approver:
    def __init__(self):
        obj_owner=Owner()
        
    def request_approval(self):  
        pass
class Admin:
    def __init__(self):
        pass
    
    def sys_control(self):  
        pass
    def view_report(self):  
        pass
class System:
    def __init__(self,data):
        self.data=data 
        for i,k in self.data.items():
            print(i,"-->",end=' ')
            print(*k,sep=',')

data={"Kodambakkam":["Chennai",798,"2BHK",6000,1],"Goripalayam":["Madurai",560,"1BHK",5500,1],"Anna Nagar":["Chennai", 1200,"3BHK",15000,2]}
    
def input_():
    input_role=input().strip()
    if input_role=="user":
        input_role_=input().strip()
        return input_role_
    else:    
        return input_role
if __name__=='__main__':
    input_type=input_()
    if input_type=="owner" or input_type=="tenant":
        obj=System(data)
        if input_type=="owner":
            print("post/remove")
            obj_own=Owner(data)
            input_mode=input().strip()
            if input_mode=="post":
                obj_own.post()
            elif input_mode=="remove":
                obj_own.remove()
                
        if input_type=="tenant":
            request_input=input().strip()
            print("Your request waiting for Approval")
print(data)