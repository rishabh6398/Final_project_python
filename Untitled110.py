
class gym():
    global list_of_users
    list_of_users=[]
    global data
    data=dict()
    global data2
    data2=dict()
    global BMI_dict 
    BMI_dict=dict()
    BMI_dict['0-18.5']={'Mon': 'Chest' , 'Tue': 'Biceps' , 'Wed': 'Rest' , 'Thu': 'Back' , 'Fri': 'Triceps' , 'Sat': 'Rest' , 'Sun': 'Rest'}
    BMI_dict['18.5-25']={'Mon': 'Chest' , 'Tue': 'Biceps' , 'Wed': 'Cardio/Abs' , 'Thu': 'Back' , 'Fri': 'Triceps' , 'Sat': 'Legs' , 'Sun': 'Rest'}
    BMI_dict['25-30']={'Mon': 'Chest' , 'Tue': 'Biceps' , 'Wed': 'Cardio/Abs' , 'Thu': 'Back' , 'Fri': 'Triceps' , 'Sat': 'Legs' , 'Sun': 'Cardio'}
    BMI_dict['>30']={'Mon': 'Chest' , 'Tue': 'Biceps' , 'Wed': 'Cardio/Abs' , 'Thu': 'Back' , 'Fri': 'Triceps' , 'Sat': 'Cardio' , 'Sun': 'Cardio'}
    def welcome(self):
        print('====================================')
        print('       GYM Membership APP           ')
        print('====================================')
        print("HELLO, Welcome to GYM Membership App!!")
        print('Are you a GYM Manager or a Member')
        print('Press:1-If you are a manager.')
        print('Press:2-If you are a member.')
        key=(input('Enter the no.:'))
        if key=="1":
            self.Manager_login()
        elif key=="2":
            self.Member_login()
        else:
            print('Choose only 1 or 2')
            self.welcome()
            
    def Manager_login(self):
        print('Manager only!! Please login to continue')
        Username=input('Enter Your Username:' )
        Password=input('Enter Your Password: ')
        print('Welcome', Username)
        self.Manager_purpose()
        
    def Member_login(self):
        print('Hello Member!! Please login to continue')
        Username=input('Enter Your Username:' )
        self.Username=Username
        Password=input('Enter Your Password: ')
        if Username in list_of_users:
            print('Welcome', Username)
            self.Member_purpose()
        else:
            print('You are not a registered member. Please contact the superuser.')
        
    def Manager_purpose(self):
        print('The following are the options')
        print('1:Create Member') 
        print('2:View Member')
        print('3:Delete Member')
        print('4:Update Member') 
        print('5:Create Regimen')
        print('6:View Regimen')
        print('7:Delete Regimen')
        print('8:Update Regimen')
        print('9:Exit')
        key=input('Enter the no.: ')
        if key=='1':
            self.create_member()
        elif key=='2':
            self.view_member()
        elif key=='3':
            self.delete_member()
        elif key=='4':
            self.update_member()
        elif key=='5':
            self.create_regimen()
        elif key=='6':
            self.view_regimen()
        elif key=='7':
            self.delete_regimen()
        elif key=='8':
            self.update_regimen()
        elif key=='9':
            self.exit()
        else:
            print('Please select only from above options')
            self.Member_purpose()
            
    def Member_purpose(self):
        print('Choose from the below options')
        print('Press 1:My regimen') 
        print('Press 2:My profile')
        print('Press 3: Exit')
        key=input('Enter the no.: ')
        if key=='1':
            self.My_regimen()
        elif key=='2':
            self.My_profile()
        elif key=='3':
            self.exit()
        else:
            print('Please select only from above options')
            self.Member_purpose()
    def My_regimen(self):
        try:
            print(data2[self.Username]['Regimen'])
            self.Member_purpose()
        except:
            print('Regimen is not valid for thie membership')
            self.Member_purpose()
    def My_profile(self):
        print(data2[self.Username])
        self.Member_purpose()
        
            
            
        
    def create_member(self):
        d=dict()
        print("Fill the following details of a memeber to register")
        d['Name']=input('Enter the name: ')
        d['Age']=input('Enter the Age: ')
        d['Gender']=input('Enter the Gender: ')
        d['Mobile_no']=input('Enter the mobile no.: ')
        d['Email']=input('Enter the Email id: ')
        d['BMI']=input('Enter the BMI: ')
        d['Membership']=input('Enter the duration:')
        data[d['Mobile_no']]=d
        data2[d['Name']]=d
        
        list_of_users.append(d["Name"])
        
        print('The member is now registered.')
        print('To go back to main menu , press any key')
        key=input()
        self.Manager_purpose()
        
    def view_member(self):
        try:
            mobile_num=input('Enter the mobile no.')
            print(data[mobile_num])
            self.Manager_purpose()
        except:
            print('The given contact no. is not registered')
            print('Press 1 to re-enter the contact no.')
            print('Press 2 to go to main menu')
            key=input('Enter the no.: ')
            if key=='1':
                self.view_member()
            elif key=='2':
                self.Manager_purpose()
            else:
                print('The no. is out of range')
    def delete_member(self):
        try:
            mobile_num=input('Enter the mobile no.')
            del data[mobile_num]
            print('The member registered with contact no.', mobile_num, 'is deleted')
            self.Manager_purpose()
        except:
            print('The given contact no. is not registered')
            print('Press 1 to re-enter the contact no.')
            print('Press 2 to go to main menu')
            key=input('Enter the no.: ')
            if key=='1':
                self.delete_member()
            elif key=='2':
                self.Manager_purpose ()
            else:
                print('The no. is out of range')
        
    def update_member(self):
        try:
            mobile_num=input('Enter mobile no.')
            print(data[mobile_num])
            change_to=input('Change the membership to:')
            data[mobile_num]['Membership']=change_to
            print('The new membership details are')
            print(data[mobile_num])
            self.Manager_purpose ()
        except:
            print('The enetered mobile no. is not registered')
            print('Press 1 to re-enter the contact no.')
            print('Press 2 to go to main menu')
            key=input('Enter the no.: ')
            if key=='1':
                self.update_member()
            elif key=='2':
                self.Manager_purpose ()
            else:
                print('The no. is out of range')
    def create_regimen(self):
        try:
            mobile_num=input('Enter the contact no:')
            BMI=data[mobile_num]['BMI']
            name=data[mobile_num]['Name']
            if 0<int(BMI)<18.5:
                data[mobile_num]['Regimen']=BMI_dict['0-18.5']
                data2[name]['Regimen']=BMI_dict['0-18.5']
            elif 18.5<=int(BMI)<25:
                data[mobile_num]['Regimen']=BMI_dict['18.5-25']
                data2[name]['Regimen']=BMI_dict['18.5-25']
            elif 25<=int(BMI)<30:
                data[mobile_num]['Regimen']=BMI_dict['25-30']
                data2[name]['Regimen']=BMI_dict['25-30']
            elif int(BMI)>30:
                data[mobile_num]['Regimen']=BMI_dict['>30']
                data2[name]['Regimen']=BMI_dict['>30']
            print('The regimen is created ')
            self.Manager_purpose ()
        except:
            print('The enetered mobile no. is not registered')
            print('Press 1 to re-enter the contact no.')
            print('Press 2 to go to main menu')
            key=input('Enter the no.: ')
            if key=='1':
                self.create_regimen()
            elif key=='2':
                self.Manager_purpose ()
            else:
                print('The no. is out of range')
    def view_regimen(self):
        try:
            mobile_num=input('Enter the contact no:')
            print('The regimen is:')
            print(data[mobile_num]['Regimen'])
            self.Manager_purpose ()
        except:
            print('The enetered mobile no. has no regimen created')
            print('Press 1 to re-enter the contact no.')
            print('Press 2 to go to main menu')
            key=input('Enter the no.: ')
            if key=='1':
                self.view_regimen()
            elif key=='2':
                self.Manager_purpose ()
            else:
                print('The no. is out of range')
        
    def delete_regimen(self):
        try:
            mobile_num=input('Enter the contact no:')
            del data[mobile_num]['Regimen']
        
            print('The regimen has been deleted')
            
            self.Manager_purpose ()
        except:
            print('The enetered mobile no. has no regimen created')
            print('Press 1 to re-enter the contact no.')
            print('Press 2 to go to main menu')
            key=input('Enter the no.: ')
            if key=='1':
                self.view_regimen()
            elif key=='2':
                self.Manager_purpose ()
            else:
                print('The no. is out of range')
    def update_regimen(self):
        mobile_num=input('Enter mobile no. :')
        print('The following are the details:')
        print(data[mobile_num])
        name=data[mobile_num]['Name']
        BMI=input("Change the BMI to:")
        data[mobile_num]['BMI']=BMI
        if 0<int(BMI)<18.5:
            data[mobile_num]['Regimen']=BMI_dict['0-18.5']
            data2[name]['Regimen']=BMI_dict['0-18.5']
        elif 18.5<=int(BMI)<25:
            data[mobile_num]['Regimen']=BMI_dict['18.5-25']
            data2[name]['Regimen']=BMI_dict['18.5-25']
        elif 25<=int(BMI)<30:
            data[mobile_num]['Regimen']=BMI_dict['25-30']
            data2[name]['Regimen']=BMI_dict['25-30']
        elif int(BMI)>30:
            data[mobile_num]['Regimen']=BMI_dict['>30']
            data2[name]['Regimen']=BMI_dict['>30']
        print('The regimen is updated ')
        print(data[mobile_num]['Regimen'])
        self.Manager_purpose ()
        
        
    def exit(self):
        pass

obj=gym() 
obj.welcome()


# In[ ]:




