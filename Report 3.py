import numpy as np
import os
os.system("cls")
aaa=1;
while (aaa==1):
 aaa=1
 os.system("cls")
#MAIN CONSOLE
 print("Welcome to the Physical Properties of UF6 Portal")
 print(" We have data of the following properties:\n 1.Vapour Pressure\n 2.Density\n 3.Viscosity\n ")
 print(" Please select the number corresponding to the property you want to find:")
 q=input("")
#PROPERTY SELECTION
 if q<1 or q>4 :
    print("Please enter a value from 1 to 4 only")
 elif (q==1):
    #VAPOUR PRESSURE STARTS
    os.system("cls")
    print("Welcome to the Vapor Pressure Portal")
    print("Do you want to find out the vapour pressure for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n")
    n=input("")
    if n<1 or n>2:
      print ("Please enter a value from 1 to 2 only")
    elif n==1 :
    #VAPOUR PRESSURE SINGLE TEMP
     dum=0;
     while dum==0 :
      print(" Enter the temperature in degree Celsius(between -273.15 to 232.6)")
      s=input("")
      t=s+273.15;
      p=0;
      if s<=-273.150     : 
       print(" Temperature less than absolute zero")
       dum=0
      elif s<=0 :
       p= pow(10,((-2751/t)-(75*(np.exp(-2560/t)))-(1.01*np.log10(t))+13.797))
       pp=p*1.0135/760/1000
       print " Vapour pressure of UF6 at temperature",s, "degree Celsius is:"
       print "", pp, " milli Bar"
       print("(From Llewellyns equation)")
       print("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
       dum=1
      elif s<=64 :
       p=pow(10,(6.3853+.0075377*s-(942.76/(s+183.416))))
       pp=p*1.0135/760/1000
       print " Vapour pressure of UF6 at temperature",s, "degree Celsius is:"
       print "", pp, " milli Bar"
       print(" (From modified Antoine equation)")
       print("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
       dum=1
      elif s<=116 :
       p=pow(10,(6.99464-(1126.288/(s+221.963))))
       pp=p*1.0135/760/1000
       print " Vapour pressure of UF6 at temperature",s, "degree Celsius is:"
       print "", pp, " milli Bar"
       print("(From modified Antoine equation)")
       print("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
       dum=1
      elif s<=232.6 :
       p=10^(7.69069-(1683.165/(s+302.148)))
       pp=p*1.0135/760/1000
       print " Vapour pressure of UF6 at temperature",s, "degree Celsius is:"
       print "", pp, " milli Bar"
       print ("(From modified Antoine equation)")
       print("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
       dum=1
      elif s>232.6:
       print "Temperature above the critical point"
    elif n==2 :
    #VAPOUR PRESSURE RANGE OF TEMP
     dum=0;
     while dum==0:
      print(" Enter the lower temperature in degree Celsius(between -273.15 to 232.6)")
      t1=input("")
      if t1<-273.15 or t1>232.6:
       print("Enter temperature in correct range")
      elif t1>-273.15 :
       dum=1
     hum=0
     while hum==0:
      print(" Enter the higher temperature in degree Celsius(between -273.15 to 64.02)")
      t2=input("")
      if t2<-273.15 or t2>232.6:
       print("Enter temperature in correct range")
       hum=0
      elif t2<t1 :
       print("Temperature should be higher than earlier input")
       hum=0
      elif t2>t1 :
       hum=1;
     print(" Enter step size in degree Celsius")
     t3=input("")
     nn=(t2-t1)/t3
     nnn=abs(nn)
     for x in range (1,nnn):  
      s=t1+x*t3
      t=s+273.15
      if s<=-273.150     : 
       print("Temperature",s," degree Celsius is less than absolute zero")
      elif s<=0 :
       p=pow(10,((-2751/t)-(75*(np.exp(-2560/t)))-(1.01*np.log10(t))+13.797))
       pp=p*1.0135/760/1000
       print " Vapour pressure of UF6 at temperature",s, "degree Celsius is:"
       print "", pp, " milli Bar"
      elif s<=64 :
       p=pow(10,(6.3853+.0075377*s-(942.76/(s+183.416))))
       pp=p*1.0135/760/1000
       print " Vapour pressure of UF6 at temperature",s, "degree Celsius is:"
       print "", pp, " milli Bar"
      elif s<=116 :
       p=pow(10,(6.99464-(1126.288/(s+221.963))))
       pp=p*1.0135/760/1000
       print " Vapour pressure of UF6 at temperature",s, "degree Celsius is:"
       print "", pp, " milli Bar"
      elif s<=232.6 :
       p=pow(10,(7.69069-(1683.165/(s+302.148))))
       pp=p*1.0135/760/1000
       print " Vapour pressure of UF6 at temperature",s, "degree Celsius is:"
       print "", pp, " milli Bar"
      elif s>232.6:
       print "Temperature is above the critical point"
       print("(From modified Antoine equation)")
       print("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
 elif q==2:
  os.system("cls")
  print("Welcome to the Density Portal")
  print(" 1. Solid\n 2. Liquid\n 3. Gas\n")
  print(" Please enter the number corresponding to the state of UF6:")
  i=input("")
  if i<1 or i>3:
   print("Please enter a value from 1 to 3 only")
  elif i==1:
   #SOLID DENSITY
   print("Do you want to find out the density for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n")
   n=input("")
   if n<1 or n>2:
    print("Please enter a value from 1 to 2 only")
   elif n==1: 
    #SOLID DENSITY SINGLE TEMP CALCULATION
    dum=0;
    while dum==0:
     print(" Enter the temperature in degree Celsius(between -273.15 to 64.02)")
     t=input("")
     if t<-273.15:
      print("Temperature less than absolute zero")
     elif t>64.02 :
      print("Temp greater than triple point")
     elif t>-273.15: 
      dum=1;
      s=t+273.15;
      if t<=64.02 :
       d=((-.0038278)*(s)+6.214799)*1000;
       print "\n The density of solid UF6 at temperature",t," degrees centrigrade is",d," kg/(m)^3"
       print"(From data from British Data Sheets; Wechsler and Hoge and Hoard and Stroupe)"
       print("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
   elif n==2 :
    #SOLID DENSITY RANGE OF TEMP CALCULATION
    dum=0;
    while dum==0:
     print(" Enter the lower temperature in degree Celsius(between -273.15 to 64.02)")
     t1=input("")
     if t1<-273.15:
      print("Temperature less than absolute zero")
     elif t1>64.02: 
      print("Temperature greater than triple point")
     elif t1>-273.15: 
      dum=1
    hum=0;
    while hum==0:
     print(" Enter the higher temperature in degree Celsius(between -273.15 to 64.02)")
     t2=input("")
     if t2<-273.15: 
      print(" Enter the lower temperature in degree Celsius(between -273.15 to 64.02)")
     elif t2>64.02: 
      print("Temperature greater than triple point")
     elif t2<t1: 
      print("Please enter temperature highter than first temperature")
     elif t2>t1: 
      hum=1;
    print(" Enter step size in degree Celsius")
    t3=input("")
    nn=(t2-t1)/t3
    nnn=abs(nn)
    for x in range (1,nnn):  
     t=t1+x*t3
     s=t+273.15;
     if t<-273.15: 
      print("Temperature  ",t,"  degrees Celsius is less than the absolute temperature")
     elif t<=64.02: 
      d=(-.0038278)*(s)+6.214799;
      dd=1000*d;
      print("\n The density of solid UF6 at temperature",t, "degrees centrigrade is",dd," kg/(m)^3\n")
     elif t>64.02:  
      print("Temperature  ",t,"  degrees Celsius is greater than the triple point temperature")
      print("(From data from British Data Sheets; Wechsler and Hoge and Hoard and Stroupe)")
  elif i==2:
   #LIQUID DENSITY
   print("Do you want to find out the density for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n")
   n=input("")
   if n<1 or n>2 : 
    print("Please enter a value from 1 to 2 only")
   elif n==1: 
    #LIQUID DENSITY SINGLE TEMP CALCULATION
    dum=0;
    while dum==0:
     print(" Enter the temperature in degree Celsius(between 64.02 to 409.58)")
     t=input("")
     if t<64.02 or t>409.58:
      dum=0
     elif t>64.02 or t<409.58: 
      dum=1;
      s=t+273.15;
      d=(3.63-5.805*pow(10,-3)*(t-64.025)-1.36*pow(10,-5)*pow((t-64.025),2)*1000)
      print("\n The density of liquid UF6 at temperature",s,"degrees centrigrade is",d," kg/(m)^3")
      print("(From Hoge and Wechsler equation)")
      print("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
   elif n==2:
    #LIQUID DENSITY RANGE OF TEMP CALCULATION
    dum=0;
    while dum==0:
     print(" Enter the lower temperature in degree Celsius(between 64.02 to 409.58)")
     t1=input("")
     if t1<64.02 or t1>409.58:
      dum=0
     elif t1>64.02 or t1<=409.58:
      dum=1
    hum=0;
    while hum==0:
     print(" Enter the higher temperature in degree Celsius(between 64.02 to 409.58)")
     t2=input("")
     if t2<64.02 or t2>409.58 or t2<t1:
      hum=0
     elif t2>t1:
      hum=1
    print(" Enter step size in degree Celsius")
    t3=input("")
    nn=(t2-t1)/t3
    nnn=abs(nn)
    for x in range (1,nnn):  
     t=t1+x*t3
     s=t+273.15;
     if t<-273.15: 
      print("Temperature  ",t,"  degrees Celsius is less than the absolute temperature")
     elif t<64.02: 
      print("Temperature  ",t,"  degrees Celsius is less than the triple point temperature")
     elif t<=409.58: 
      d=(3.63-5.805*pow(10,-3)*(t-64.025)-1.36*pow(10,-5)*pow((t-64.025),2)*1000)
      print("\n The density of liquid UF6 at temperature",t," degrees centrigrade is",d,"kg/(m)^3")
     elif t>409.58:
      print("Temperature   ",t,"  degrees Celsius not in scope of equation")
      print("(From Hoge and Wechsler equation)")
      print("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
  elif i==3: 
   #GAS DENSITY
   print("Do you want to find out the density for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n")
   n=input("")
   if n<1 or n>2 : 
    print("Please enter a value from 1 to 2 only")
   elif n==1: 
    #GAS DENSITY SINGLE TEMP CALCULATION
    print("Please enter the pressure in mm Hg")
    k=input("")
    p=k/760;
    l=((1.3769*10^(6)*p)^(1/3))-273.15
    ll=l-.1*l;
    dum=0;
    while dum==0:
     print("Enter the temperature in degree Celsius (greater than ",ll," degrees Celsius)")
     t=input("")
     if t<ll:
      dum=0
     elif t>=ll: 
      dum=1;
     s=t+273.15;
     if t<=ll :
      print("Temperature  ",t,"  degrees Celsius is less than the temperature limit")
     elif t>ll: 
      d=((4.291*p)/(s*(1+(-1.3769*pow(10,6)*p/pow(s,3)))))*1000
      print("\n The density of gaseous UF6 at temperature",t,"degrees centrigrade is",d," g/cc")
      print("(From Weinstock equation)")
      print("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
      #GAS DENSITY RANGE OF TEMP CALCULATIONS
   elif n==2 :
    print("Please enter the pressure in mm Hg")
    k=input("")
    p=k/760;
    l=pow((1.3769*pow(10,6)*p),(1/3))-273.15
    ll=l-.1*l;
    dum=0;
    while dum==0:
     print("Enter the lower temperature in degree Celsius (greater than ",ll," degrees Celsius)")
     t1=input("")
     if t1<ll: 
      dum=0
     elif t1>=ll: 
      dum=1
    hum=0;
    while hum==0:
     print(" Enter the higher temperature in degree Celsius")
     t2=input("")
     if t2<ll or t2<t1:
      hum=0
     elif t2>t1: 
      hum=1;
    print(" Enter step size in degree Celsius")
    t3=input("")
    nn=(t2-t1)/t3
    nnn=abs(nn)
    for x in range (1,nnn):  
     t=t1+x*t3
     s=t+273.15
     if t<=ll: 
      print("Temperature  ",t,"  degrees Celsius is less than the lower limit temperature")
     elif t>ll: 
      d=((4.291*p)/(s*(1+(-1.3769*pow(10,6)*p/pow(s,3)))))*1000;
      print("\n The density of gaseous UF6 at temperature %f degrees centrigrade is %f kg/(m)^3",t,d)
      print("(From Weinstock equation)")
      print("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
  #DENSITY ENDS
  #VISCOSITY STARTS
 elif q==3 :
  os.system("cls")
  print("Welcome to the viscosity portal")
  print(' Select the number corresponding to the state of UF6\n 1.Gas\n 2.Liquid\n')
  i=input("")
  if i<1 or i>2:
   print("Please enter a value from 1 to 2 only")
  elif i==1 :
   #GAS
   print(' Do you want to find out the viscosity for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n')
   n=input("")
   if n<1 or n>2:
    print("Please enter a value from 1 to 2 only")
   elif n==1 :
    #GAS SINGLE TEMP CALCULATION
    dum=0;
    while dum==0:
     print(" Enter the temperature in degree Celsius(greater than -273.15)")
     t=input("")
     if t<=-273.15 :
      dum=0
     elif t>-273.15 :
      dum=1
    s=t+273.15;
    if t<=-273.15 :
     print"Temperature  ",t,"  degrees Celsius is less than the absolute temperature"
    elif t>=-273.15 :
     u=(2.1*(pow(s,.779)*pow(10,-6)))
     print "The viscosity of the UF6 vapours at",t," degree Celsius is", u, "Poise"
     print("(From Llewellyns equation)")
     print('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
   elif n==2 :
    #GAS RANGE OF TEMP CALCULATION
    dum=0;
    while dum==0:
     print(" Enter the lower temperature in degree Celsius (greater than -273.15)")
     t1=input("")
     if t1<=-273.15 :
      dum=0
     elif t1>-273.15 :
      dum=1
    hum=0;
    while hum==0:
     print(" Enter the higher temperature in degree Celsius (greater than -273.15)")
     t2=input("")
     if t2<=-273.15 or t2<t1 :
        hum=0
     elif t2>t1 :
        hum=1;
    print(" Enter step size in degree Celsius")
    t3=input("")
    nn=(t2-t1)/t3
    nnn=abs(nn)
    for x in range (1,nnn):  
     t=t1+x*t3
     s=t+273.15
     if t<-273.15 :
      print("Temperature  ",t,"  degrees Celsius is less than the absolute temperature")
     elif t>=-273.15 :
      u=(2.1*(pow(s,.779)*pow(10,-6)))
      print" The viscosity of the UF6 vapours at",t, "degree Celsiusis",u,"Poise\n"
     print("(From Llewellyns equation)")
     print('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
     
  elif i==2 :
   #LIQUID VISCOSITY
   print(' Do you want to find out the viscosity for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n')
   n=input("")
   if n<1 or n>2 :
    print("Please enter a value from 1 to 2 only")
   elif n==1 :
    #LIQUID VISCOSITY SINGLE TEMP CALCULATION
    dum=0;
    while dum==0:
     print(" Enter the temperature in degree Celsius(greater than 64.02)")
     t=input("")
     if t<=64.02 :
      dum=0
     elif t>64.02 :
      dum=1
    s=t+273.15;
    if t<=64.02 :
     print("Temperature  ",t,"  degrees Celsius is less than the triple point temperature")
    elif t>64.02 :
     u=(.1271*pow(10,-3)*np.exp(1217/s))
     print' The viscosity of the UF6 liquid at',t, 'degrees Celsius is',u,'Poise'
     print("(From Cohens equation)")
     print('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
   elif n==2 :
    #LIQUID VISCOSITY   RANGE OF TEMP CALCULATION
    dum=0;
    while dum==0:
     print(" Enter the lower temperature in degree Celsius (greater than 64.02)")
     t1=input("")
     if t1<=64.02 :
      dum=0
     elif t1>64.02 :
      dum=1
    hum=0;
    while hum==0:
     print(" Enter the higher temperature in degree Celsius (greater than 64.02)")
     t2=input("")
     if t2<64.02 or t2<t1:
        hum=0
     elif t2>t1 :
        hum=1;
    print(" Enter step size in degree Celsius")
    t3=input("")
    nn=(t2-t1)/t3
    nnn=abs(nn)
    for x in range (1,nnn):  
     t=t1+x*t3
     s=t+273.15
     if t<=-140 :
      print("Temperature  ",t, "  degrees Celsius is less than the absolute temperature")
     elif t>-140 :
      u=(.1271*10^(-3)*np.exp(1217/s))
      print' The viscosity of the UF6 liquid at',t,'degrees Celsius is',u,' Poise\n'
     print("(From Cohens equation)")
     print('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
 print "Do you want to continue?\n 1.Yes\n 2.No"
 hp=input("")
 if hp==1 :
  aaa=1
 elif hp==2 :
  aaa=2   