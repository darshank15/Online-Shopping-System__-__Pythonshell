import pickle
import os

class Product :
   
    def __init__(self,name,group,subgroup,price) :  

        if not os.path.isfile("productdb"):
            self.__id=1
        else :
            inFile=open("productdb","rb")
            dictobj=pickle.load(inFile)
            inFile.close()
            self.__id=max(dictobj, key=int)+1

        self._name = name
        self._group=group
        self._subgroup=subgroup
        self._price=price

    def getId(self) :
        return self.__id
    def setName(self,name) :
        self._name=name
    def getName(self) :
        return self._name
    def setGroup(self,group) :
        self._group=group
    def getGroup(self) :
        return self._group
    def setSubgroup(self,subgroup) :
        self._subgroup=subgroup
    def getSubgroup(self) :
        return self._subgroup
    def setPrice(self,price) :
        self._price=price
    def getPrice(self) :
        return self._price

class Admin :
    __idcount=1
    def __init__(self,name) :
        self.__id=Admin.__idcount
        self.__name = name
        Admin.__idcount = Admin.__idcount + 1

    def getId(self) :
        return self.__id
    def setName(self,name) :
        self.__name=name
    def getName(self) :
        return self.__name

    def viewProducts(self) :
        if not os.path.isfile("productdb"):
            print "ProductList Empty  !!! "
            return 0
        else :
            inFile=open("productdb","rb")
            dictobj=pickle.load(inFile)
            inFile.close()
            print "*****************Details of all Product******************"
            for key, value in dictobj.iteritems():
                print "Id : ", value.getId()
                print "Name :" ,value.getName()
                print "Group :" ,value.getGroup()
                print "Subgroup :" ,value.getSubgroup()
                print "Price :" ,value.getPrice()
                print ""
            print "**********************************************************"
            return 1

    def addProducts(self) :
        
        if os.path.isfile("productdb"):
            inFile=open("productdb","rb")
            dictobj=pickle.load(inFile)
            inFile.close()
        else :
            dictobj = {}

        name = raw_input("Enter Name : ")
        group = raw_input("Enter group : ")
        subgroup = raw_input("Enter subGroup : ")
        try :
            price = int(raw_input("Enter price : "))
        except :
            print "Price must be of Integer Type"
            return

        p = Product(name,group,subgroup,price)
        
        outFile = open("productdb","wb")
        dictobj[p.getId()]=p
        pickle.dump(dictobj,outFile)
        outFile.close()

    def deleteProducts(self) :
        if os.path.isfile("productdb") :
            try:
                iddel=int(raw_input("Enter ID of product you want to delete : "))
            except :
                print "Not Valid ID "
                return
            inFile=open("productdb","rb")
            dictobj=pickle.load(inFile)
            inFile.close()
            if iddel in dictobj: #check ID exist in dictionary
                del dictobj[iddel]
                if len(dictobj) == 0 : #After deletion of record, if dict empty then delete its dump file
                    try :
                        os.remove("productdb")
                    except:
                        pass
                else :                  #else updated dict dumped
                    outFile = open("productdb","wb")
                    pickle.dump(dictobj,outFile)
                    outFile.close()
            else:
                print "Product doesn't found with given ID : ",iddel
        else: # if productdb in not exist i.e. product list empty
            print "ProductList Empty for deletion !!! "
    
    def modifyProducts(self) :
        if os.path.isfile("productdb") :
            try:
                idmod=int(raw_input("Enter ID of product you want to Modify : "))
            except:
                print "Not Valid ID "
                return 
            inFile=open("productdb","rb")
            dictobj=pickle.load(inFile)
            inFile.close()
            if idmod in dictobj: #check ID exist in dictionary
                newname = raw_input("Enter New Name : ")
                newgroup = raw_input("Enter New group : ")
                newsubgroup = raw_input("Enter New subGroup : ")
                newprice = raw_input("Enter New price : ")
                oldobj=dictobj[idmod]
                oldobj.setName(newname)
                oldobj.setGroup(newgroup)
                oldobj.setSubgroup(newsubgroup)
                oldobj.setPrice(newprice)
                dictobj[idmod]=oldobj
                outFile = open("productdb","wb")
                pickle.dump(dictobj,outFile)
                outFile.close()
            else:
                print "Product doesn't found with given ID : ",idmod
        else: # if productdb in not exist i.e. product list empty
            print "ProductList Empty for modify !!! "
    
    def makeShipment(self) :
        pass
    def confirmDelivery(self):
        pass

class Customer :
   
    def __init__(self,name,address,phoneNo) :

        if not os.path.isfile("customerdb"):
            self.__id=1
        else :
            inFile=open("customerdb","rb")
            custdict=pickle.load(inFile)
            inFile.close()
            self.__id=max(custdict, key=int)+1

        self._name = name
        self._address = address
        self._phoneNo = phoneNo
        

    def getId(self) :
        return self.__id
    def setName(self,name) :
        self._name=name
    def getName(self) :
        return self._name
    def setAddress(self,name) :
        self._name=name
    def getAddress(self) :
        return self._address
    def setPhoneNo(self,phoneNo) :
        self._phoneNo=phoneNo
    def getPhoneNo(self) :
        return self._phoneNo
    
    def buyProducts(self):
        
        if not os.path.isfile("paymentdb"):
            print "You haven't done any Payment yet !!! "
            return 0
        else :
            inFile=open("paymentdb","rb")
            paydict=pickle.load(inFile)
            inFile.close()

            if self.__id in paydict :
                paylist=paydict[self.__id]
                for payobj in paylist:
                    print "Card Type : ", payobj.getCardType()
                    print "Card Number : ", payobj.getCardNo()
                    print "Bought Product list : ", payobj.getName()
                    print ""
            else :
                print "You haven't done any Payment yet !!!"

    def viewProducts(self):
        if not os.path.isfile("productdb"):
            print "No Product Found !!! "
            return 0
        else :
            inFile=open("productdb","rb")
            dictobj=pickle.load(inFile)
            inFile.close()
            print "*****************Details of all Product******************"
            for key, value in dictobj.iteritems():
                print "Id : ", value.getId()
                print "Name :" ,value.getName()
                print "Group :" ,value.getGroup()
                print "Subgroup :" ,value.getSubgroup()
                print "Price :" ,value.getPrice()
                print ""
            print "**********************************************************"
            return 1
    
    def makePayment(self):

        if not os.path.isfile("cartdb"):
            print "your cart is empty !!! "
            return 0
        else :
            inFile=open("cartdb","rb")
            cartdict=pickle.load(inFile)
            inFile.close()

            if self.__id not in cartdict :
                print "your cart is empty !!!"
            else :
                cardtype = raw_input("Enter Card Type : ")
                cardno = raw_input("Enter Card Number : ")
                cartobj=cartdict[self.__id]
                
                allprodlistname=""
                for item in cartobj.getProductList() :
                    allprodlistname = allprodlistname + item.getName() + ","

                #print "allitemname : ",allprodlistname
                payobj=Payment(self.__id, allprodlistname, cardtype, cardno)

                if os.path.isfile("paymentdb"):
                    inFile=open("paymentdb","rb")
                    paydict=pickle.load(inFile)
                    inFile.close()
                else :
                    paydict = {}
                
                if self.__id in paydict :
                    oldpaylist=paydict[self.__id]
                    oldpaylist.append(payobj)
                    paydict[self.__id]=oldpaylist
                else :
                    paylist=[]
                    paylist.append(payobj)
                    paydict[self.__id]=paylist
                
                del cartdict[self.__id]
                outFile = open("cartdb","wb")
                pickle.dump(cartdict,outFile)
                outFile.close()
                
                outFile = open("paymentdb","wb")
                pickle.dump(paydict,outFile)
                outFile.close()

    def addToCart(self):

        try :
            productaddid = int(raw_input("Enter Product ID you want to add into the cart : "))
        except:
            print "Invalid Product ID"
            return
        
        if not os.path.isfile("productdb"):
            print "No Product Found !!! "
            return
        else :
            inFile=open("productdb","rb")
            proddict=pickle.load(inFile)
            inFile.close()
            if productaddid in proddict :

                if os.path.isfile("cartdb"):
                    inFile=open("cartdb","rb")
                    cartdict=pickle.load(inFile)
                    inFile.close()
                else :
                    cartdict = {}
                
                if self.__id in cartdict :

                    prodobj=proddict[productaddid]
                    cartobj=cartdict[self.__id]
                    cartobj.setTotal(cartobj.getTotal()+prodobj.getPrice())
                    cartobj.setNumOfProducts(cartobj.getNumOfProducts()+1)
                    oldlist=cartobj.getProductList()
                    oldlist.append(prodobj)
                    cartobj.setProductList(oldlist)
                    cartdict[self.__id]=cartobj

                else :
                    prodList=[]
                    prodobj=proddict[productaddid]
                    prodList.append(prodobj)
                    cartobj=Cart(1,prodList,prodobj.getPrice())
                    cartdict[self.__id]=cartobj

                outFile = open("cartdb","wb")
                pickle.dump(cartdict,outFile)
                outFile.close()
            else :
                print "Given PID not exist"

    def viewCart(self):
        if not os.path.isfile("cartdb"):
            print "your cart is empty !!! "
            return 0
        else :
            inFile=open("cartdb","rb")
            cartdict=pickle.load(inFile)
            inFile.close()

            if self.__id in cartdict :
                cartobj=cartdict[self.__id]
                print "numOfProducts : ", cartobj.getNumOfProducts()
                print "Total :" ,cartobj.getTotal()
                print "ProductList"
                plist =  cartobj.getProductList()
                for item in plist:
                    print "\tID : ",item.getId()
                    print "\tProductName : ",item.getName()
                    print "\tPrice : ",item.getPrice()
                    print ""
            else :
                print "your cart is empty !!!"
    
    def deleteFromCart(self):
        
        if not os.path.isfile("productdb"):
            print "No Product Found !!! "
            return
        else :
            if not os.path.isfile("cartdb"):
                    print "Your cart is empty  !!!"
                    return 
            try :
                productaddid = int(raw_input("Enter Product ID you want to remove from cart : "))
            except:
                print "Invalid Product ID"
                return

            inFile=open("productdb","rb")
            proddict=pickle.load(inFile)
            inFile.close()
            if productaddid not in proddict :
                print "Given PID not exist"
            else :
                inFile=open("cartdb","rb")
                cartdict=pickle.load(inFile)
                inFile.close()
                
                if self.__id in cartdict :
                    prodobj=proddict[productaddid]
                    cartobj=cartdict[self.__id]
                    oldlist=cartobj.getProductList()
                    flag=0
                    for item in oldlist:
                        if productaddid == item.getId() :
                            oldlist.remove(item)
                            flag=flag+1
                    
                    if flag :

                        if len(oldlist) == 0 : #After deletion of record, if list empty then cartdict
                            del cartdict[self.__id]
                            if len(cartdict) == 0 :
                                try :
                                    os.remove("cartdb")
                                    return
                                except:
                                    return
                        else :
                            cartobj.setProductList(oldlist)
                            cartobj.setTotal(cartobj.getTotal()-(flag*prodobj.getPrice()))
                            cartobj.setNumOfProducts(cartobj.getNumOfProducts()-flag)
                            cartdict[self.__id]=cartobj

                        outFile = open("cartdb","wb")
                        pickle.dump(cartdict,outFile)
                        print "cartsize :",len(cartdict)
                        outFile.close()
            
                    else:
                        print "These Product ID not exist in your cart"
                        return 
                    
                else :
                    print "your cart is empty !!!"

class Guest :
    __idcount=1
    def __init__(self) :
        self.__guestNum=Guest.__idcount
        Guest.__idcount = Guest.__idcount + 1

    def getGuestNum(self) :
        return self.__guestNum
    
    def viewProducts(self) :
        
        if not os.path.isfile("productdb"):
            print "ProductList Empty  !!! "
            return 0
        else :
            inFile=open("productdb","rb")
            dictobj=pickle.load(inFile)
            inFile.close()
            print "*****************Details of all Product******************"
            for key, value in dictobj.iteritems():
                print "Id : ", value.getId()
                print "Name :" ,value.getName()
                print "Group :" ,value.getGroup()
                print "Subgroup :" ,value.getSubgroup()
                print "Price :" ,value.getPrice()
                print ""
            print "**********************************************************"
            return 1
    
    def getRegistered(self) :  

        if os.path.isfile("customerdb"):
            inFile=open("customerdb","rb")
            custdict=pickle.load(inFile)
            inFile.close()
        else :
            custdict = {} 

        name = raw_input("Enter Name : ")
        address = raw_input("Enter Address : ")
        phoneNum = raw_input("Enter PhoneNum : ")
        c= Customer(name,address,phoneNum)
        print "Succefully Registered with ID : ",c.getId()
        outFile = open("customerdb","wb")
        custdict[c.getId()]=c
        pickle.dump(custdict,outFile)
        outFile.close()

class Cart :
    __idcount=1
    def __init__(self,numOfProducts,productList,total):
        self.__id=Cart.__idcount
        self._numOfProducts=numOfProducts
        self._productList=productList
        self._total=total
        Cart.__idcount = Cart.__idcount + 1

    def getId(self) :
        return self.__id

    def setNumOfProducts(self,numOfProducts) :
        self._numOfProducts=numOfProducts
    def getNumOfProducts(self) :
        return self._numOfProducts
    
    def setProductList(self,productList) :
        self._productList=productList
    def getProductList(self) :
        return self._productList
    
    def setTotal(self,total) :
        self._total=total
    def getTotal(self) :
        return self._total

class Payment :
    def __init__(self,customerid,name,cardType,cardNo):
        self.__name = name 
        self.__id=customerid
        self.__cardType=cardType
        self.__cardNo=cardNo

    def getId(self) :
        return self.__id
    
    def getName(self) :
        return self.__name
    def setName(self,name) :
        self.__name=name

    def setCardType(self,cardType) :
        self.__cardType=cardType
    def getCardType(self) :
        return self.__cardType
    
    def setCardNo(self,cardNo) :
        self.__cardNo=cardNo
    def getCardNo(self) :
        return self.__cardNo
    

a1 = Admin("darshanAdmin")
g1 = Guest()
while 1:
    print "1.Admin"
    print "2.Customer"
    print "3.Guest"
    print "4.Quit"
    try :
        unserinput = int(raw_input("\nEnter Your Choice : "))
    except :
        print "Please Enter valid input"
        continue
    if unserinput==1 :
        #Admin
        while 1:
            print "\n*** Admin Mode ***"
            print "1.View Product"
            print "2.Add Product"
            print "3.Delete Product"
            print "4.Modify Product"
            print "5.Quit from Admin"
            try :
                admininput = int(raw_input("\nEnter Your Choice : "))
            except :
                print "Invalid Admin choice"
                continue
            if admininput==1 :
                a1.viewProducts()
            elif admininput==2 :
                a1.addProducts()
            elif admininput==3 :
                a1.deleteProducts()
            elif admininput==4 :
                a1.modifyProducts()
            elif admininput==5 :
                break
            else :
                print "Invalid Admin choice"
            
    elif unserinput==2 :
        #Customer mode
        if not os.path.isfile("customerdb") :
            print "No customer Record Exist, Please Register first"
        else :
            try :
                custid = int(raw_input("Enter Customer ID : "))
            except :
                print "Please enter valid(integer) Customer ID "
                continue

            inFile=open("customerdb","rb")
            custdict=pickle.load(inFile)
            inFile.close()
            if custid not in custdict :
                print "Customer ID not exist"
            else :
                c1 = custdict[custid]
                while 1:
                    print "\n*** Customer Mode ***"
                    print "1.View Product "
                    print "2.Buy Product "
                    print "3.Make Payment"
                    print "4.Add to Cart "
                    print "5.Delete from cart "
                    print "6.View Cart"
                    print "7.Quit from Customer"
                    try :
                        custinput = int(raw_input("\nEnter Your Choice : "))
                    except :
                        print "Invalid Customer choice"
                        continue
                    if custinput==1 :
                        c1.viewProducts()
                    elif custinput==2 :
                        c1.buyProducts()
                    elif custinput==3 :
                        c1.makePayment()
                    elif custinput==4 :
                        c1.addToCart()
                    elif custinput==5 :
                        c1.deleteFromCart()
                    elif custinput==6 :
                        c1.viewCart()
                    elif custinput==7 :
                        break
                    else :
                        print "Invalid Customer choice"
    elif unserinput==3 :
        #Guest mode
        while 1 :
            print "\n*** Guest Mode ***"
            print "1.View Product"
            print "2.Get Register"
            print "3.Quit from Guest"
            try :
                guestinput = int(raw_input("\nEnter Your Choice : "))
            except :
                print "Invalid Guest choice"
                continue
            if guestinput==1 :
                g1.viewProducts()
            elif guestinput==2 :
                g1.getRegistered()
            elif guestinput==3 :
                break
            else :
                print "Invalid Guest choice"

    elif unserinput==4 :
        #quit
        break
    else :
        print "Not Valid command"
