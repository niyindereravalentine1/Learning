class employee:
    def _init_(self,name="",department="",contract="",salary=0):
        self.name=name
        self.department=department
        self.salary=salary
        self.contract=contract
    
    def inserting(self):
        Available_Departments = ["Finance", "IT", "Production", "Sales", "Security"]
        empname=input("enter name:")
        self.name=empname
        empcontract=input("enter contract category casual(c) or permanet(p)")
        if empcontract.upper()=="C".upper():
            worked_hours=float(input("enter hours worked:"))
            payrate=float(input("enter amount per hour:"))
            net_salary=worked_hours*payrate
            print("name:",self.name, "in department:",self.department, "has net salary of",net_salary)
            if worked_hours>40:
                overtime=net_salary*1.5
                print("additional salary:",overtime)
        elif empcontract.upper()=="P".upper():
            gross_salary=float(input("enter gross salary:"))
            self.salary=gross_salary
            tax=0.3
            soc=0.03
            maternity=0.003
            deduction=(self.salary*tax)+(self.salary*soc)+(self.salary*maternity)
            net_salary=gross_salary-deduction
        print("what is your department:")
        print("available department are:")
        for i in range(0,len(Available_Departments)):
            print(i+1,".",Available_Departments[i])
        print("type number corresponding to your department:")
        employedepart=int(input())
        if employedepart==1:
            dept="finance"
            print("your department is",dept)
            print("name:",self.name, "in department:",self.department, "has net salary of",net_salary)
        elif employedepart==2:
            dept="IT"
            print("your department is",dept)
            
            bonus=net_salary*0.025
            total_salary=net_salary+bonus
            print("name:",self.name, "in department:",self.department,"total salary with bonus:",total_salary)
        elif employedepart==3:
            dept="Production"
            print("your department is",dept)
            print("name:",self.name, "in department:",self.department, "has net salary of",net_salary)
        elif employedepart==4:
            dept="Sales"
            print("your department is",dept)
            bonus=net_salary*0.015
            total_salary=net_salary+bonus
            print("name:",self.name, "in department:",self.department,"total salary with bonus:",total_salary)
        elif employedepart==5:
            dept="security"
            print("your department is",dept)
            print("name:",self.name, "in department:",self.department, "has net salary of",net_salary)
        else:
            print("Enter valid department:")
            print("My department is:")
            newdept=input()
            print("you have successful added your department and is now recorded")
            Available_Departments.append(newdept)
            print("available department now are:")
            for i in range(0,len(Available_Departments)):
                print(i+1,".",Available_Departments[i])
            print("name:",self.name, "in department:",self.department, "has net salary of",net_salary)
        
        
def answer():
    a=input("press yes(Y/y) to continue:")
    if a.upper()=="y".upper():
            pass

obj=employee()
answer()
obj.inserting()