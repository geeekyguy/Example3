#File Creation Tutorial
import random
import datetime
rand1=random.randrange(1000000000,9999999999)
rand2=random.randrange(1000000000,9999999999)
rand3=random.randrange(100000000000,999999999999)
rand4=random.randrange(10000,99999)
MS=int(10000)
IMSI=int(10000)
IMSI2=int(50000)
ICCID=(2000000)
numn=int(14000413)
numm=int(14000414)
char=str("7BA0201FD064394D18A0C9333003CAF5")
country_code=input("Enter the Country Code\n")
SIMS=input("Enter the Numer of SIMS\n")
#count=int(SIMS)    
datetimestr=str(datetime.datetime.now())
cc=str(country_code)
Filename=cc+"_"+datetimestr
f=open(Filename+".txt","w")
f.write("****************************************\n")
f.write("*      HEADER DESCRIPTION \n")
f.write("****************************************\n")
f.write("\n")
f.write("Customer:        Lycamobile\n")
f.write("Batch:           1643\n")
f.write("Quantity:        25000\n")
f.write("Type:            Plug-IN\n")
f.write("Profile:         03.10\n")
f.write("Config_Code:     LYC0317\n")
f.write("Graph_ref:       01.00\n")
f.write("Address1:        Lycamobile\n")
f.write("Address2:\n")
f.write("Address3:\n")
f.write("\n")
f.write("***************************************\n")
f.write("*          INPUT VARIABLES\n")
f.write("***************************************\n")
f.write("Var_In : MSISDN\n")
f.write("var_in_list:\n")
f.write("IMSI:  784457157150000\n")
f.write("IMSI2: 544454647570000\n")
f.write("Ser_nb:4574747477477800010\n")
f.write("***************************************\n")
f.write("*          OUTPUT VARIABLES\n")
f.write("***************************************\n")
f.write("Var_Out: IMSI/IMSI2/ICCID/MSISDN/PIN1/PUK1/PIN2/PUK2/KI/ADM1/ACC1/ACC2\n")


for i in range(SIMS):
    a1=str(rand4)
    a=str(MS)
    b1=str(rand1)
    b=str(IMSI)
    c1=str(rand2)
    c=str(IMSI2)
    d1=str(rand3)
    d=str(ICCID)
    e=str(numn)
    fi=str(numm)
    IMSIFULL=b1+b
    IMSI2FULL=c1+c
    ICCID_FULL=d1+d
    MSISDN_FULL=cc+a1+a
    #print(MSISDN_FULL)
    f.write("\n")
    f.write(IMSIFULL+" "+IMSI2FULL+" "+ICCID_FULL+" "+MSISDN_FULL)
    f.write(" 1234 ")
    f.write(e)
    f.write(" 1235")
    f.write(" "+fi)
    f.write(" "+char)
    f.write(" 80A2812C72EDCA5C")
    f.write(" 0001")
    f.write(" 0002")
    MS=MS+1
    IMSI=IMSI+1
    IMSI2=IMSI2+1
    ICCID=ICCID+10   
    numn=numn+1
    numm=numm+1 


f.close()

print("\n**************FILE GENERATED SUCCESSFULLY**************")
