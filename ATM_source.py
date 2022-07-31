import random
class accHolder:
        branch = 'City Main Branch'
        Address = ''' 34A/32, XYZ Complex opposite ,City Of New York - 700000'''
        BankNo = 7387
        BankName = "Finance Bank"
        IFSC = 'MFA935000BA'
        MICR = 8977385280313
        cash = 0
        accNo = None
        Name = None
        mob = None
        def __init__(self,accNo,Name,mob,cash):
                self.accNo = accNo
                self.Name = Name
                self.mob = mob
                self.cash = cash
        def AtmCard(self):
                self.pinValueEncode = encode().getEnc()

        def Depo(self,amount):
                self.cash += amount
                
        def With(self,amount):
                self.cash -= amount

class encode:
	def __init__(self):
		self.__pin = randint(1000,9999)
		print(self.__pin)
		self.__l = [randint(1,9) for i in range(4)]
		self.__encValue = self.__enc(self.__pin,self.__l)
	def __enc(self,pin,l):
		s = ''
		for i,j in zip(str(pin),l):
			s = s + str(ord(i)*j) + '-1'
		return s
	def getEnc(self):
		return self.__encValue
	def check(self,pin):
		if 1000 <= pin <= 9999 and self.__encValue == self.__enc(pin,self.__l):
			return True
		return False

	
        
def wit(cash,ba):
        am=int(input("Enter the withdrawal amount\n"))
        if(cash>=am):
                if(am%100==0 and 50000>=am and am<=ba):
                        print("Before transaction:",cash)
                        cash-=am;
                        ba-=am
                        print("transaction successful")
                elif(50000<am):
                        print("Allow only below 50000 rupees transaction")
                        cash,ba=wit(cash,ba)
                elif(ba<am):
                        print("Don't have money in ATM\nOnly ",ba,"are available")
                        cash,ba=wit(cash,ba)
                else:
                        print("Enter the amount in 100's multiples Only");
                        cash,ba=wit(cash,ba)
        else:
                print("Don't have an Enough money in your account");
        return cash,ba
def dep(cash):
        am=int(input("Enter the deposit amount\n"))
        if(am%100==0):
                print("Before transaction:",cash)
                cash+=am
                print("transaction successful")
        else:
                print("Enter the amount in 100's multiples Only");
                cash,am=dep(cash)
        return cash,am
def otp(mo):
        m=int(input("Enter the mobile number"))
        if(mo==m):
                otp=random.randint(1000,9999)
                print("\t\t\tOTP is ",otp,"\n")
                return otp
        else:
                print("Enter the valid mobile number only")
                return 10

n=int(input("\t\tWelcome to india's 1 ATM\n Enter the Number \n for withdrawal    -1\n for deposit       -2\n for change the pin-3\n for Cancel\t   -4\n for check balance -Anyone NO\n "));
ba=40500
di=[1234,5678,8900,7890,0]
ac=(32211309280001410,32214309287009023,32211389270103002,322738782938009)
na=["Name A","Name B","Name C","Name D"]
cash=[20100.87,51490.43,1700.66,98000.32]
mo=[9787813846,9876543210,9000000000,8000000000]
while(4!=n):
        pin=int(input("Enter the ATM pin number:"))
        i=0
        while(i<len(di)):
                if(pin==di[i]):
                        print("Account HOLDER Name:",na[i],"\tAccount Number:",ac[i])
                        if(n==1):
                                cash[i],ba=wit(cash[i],ba)
                        elif(n==2):
                                cash[i],am=dep(cash[i]);
                                ba+=am
                        elif(n==3):
                                otp=otp(mo[i])
                                if(10!=otp):
                                        ot=int(input("Enter the OTP:"))
                                        if(ot==otp):
                                                pinn=int(input("\nEnter the New ATM pin:"))
                                                if(1000<=pinn and 9999>=pinn):
                                                        di[i]=pinn
                                                        print("\npin number is changed successfully");
                                                        break
                                                else:
                                                        print("\nEnter the  pin in only 4 digt's Only");
                                                        continue
                                        else:
                                                print("OTP is wrong.Enter the valid OTP");
                                                break
                                else:
                                        break
                        print("\nAvailable balance:{0:.2f}".format(cash[i]));
                        break
                elif(0==di[i]):
                        print("Pin number is wrong & Enter corect pin number");
                i+=1;
        n=int(input("\t\tWelcome to india's 1 ATM\n Enter the Number \n for withdrawal    -1\n for deposit       -2\n for change the pin-3\n for Cancel\t   -4\n for check balance -Anyone NO\n "));
#print("Balance in ATM",ba)
print("\n\t\tThank you for used me")
        
