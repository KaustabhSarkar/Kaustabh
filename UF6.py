import scipy
import numpy
import matplotlib.pyplot as plt
import os
os.system('cls')
aaa=1;
while (aaa==1):
 os.system('cls')
#MAIN CONSOLE
 disp("Welcome to the Physical Properties of UF6 Portal")
 mprintf(' We have data of the following properties:\n 1.Vapour Pressure\n 2.Density\n 3.Viscosity\n 4.Thermal conductivity\n')
 mprintf(' Please select the number corresponding to the property you want to find:')
 q=input("")
#PROPERTY SELECTION
if (q<1):
    printf("Please enter a value from 1 to 4 only")
elif (q==1):
    #VAPOUR PRESSURE STARTS
    clc
    disp("Welcome to the Vapor Pressure Portal")
    mprintf('Do you want to find out the vapour pressure for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n')
    n=input("")
    if n<1 :
     printf("Please enter a value from 1 to 2 only")
elif n==1 :
    #VAPOUR PRESSURE SINGLE TEMP
    dum=0;
    while dum==0 :
     mprintf(" Enter the temperature in degree Celsius(between -273.15 to 232.6)")
     s=input("")
    if s<-273.15 :
     mprintf("\n")
     clc(1)
elif s>232.6 :
        mprintf("\n")
        clc(1)
elif s>-273.15 :
        dum=1;
        end
end
t=s+273.15;
p=0;
if s<=-273.150     : 
    mprintf(" Temperature less than absolute zero")
elif s<=0 :
    p= pow(10,((-2751/t)-(75*(exp(-2560/t)))-(1.01*log10(t))+13.797))
    pp=p*1.0135/760/1000
    mprintf(' Vapour pressure of UF6 at temperature %f degree Celsius is:\n%f milli Bars',s,pp)
    disp("(From Llewellyns equation)")
    mprintf("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
elif s<=64 :
    p=pow(10,(6.3853+.0075377*s-(942.76/(s+183.416))))
    pp=p*1.0135/760/1000
    mprintf(' Vapour pressure of UF6 at temperature %f degree Celsius is:\n%f milli Bars',s,pp)
    disp("(From modified Antoine equation)")
    mprintf("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
elif s<=116 :
    p=pow(10,(6.99464-(1126.288/(s+221.963))))
    disp("Vapour pressure of UF6 at temperature   "+string(s)+"   degree Celsius is  "+string(p)+"   mm Hg")
    disp("(From modified Antoine equation)")
    mprintf("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
elif s<=232.6 :
    p=10^(7.69069-(1683.165/(s+302.148)))
    pp=p*1.0135/760/1000
    mprintf(' Vapour pressure of UF6 at temperature %f degree Celsius is:\n%f milli Bars',s,pp)
    print ("(From modified Antoine equation)")
    mprintf("\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt")
elif s>232.6:
    print "Temperature above the critical point"
    end
elif n==2 :
    #VAPOUR PRESSURE RANGE OF TEMP
    dum=0;
    while dum==0:
     mprintf(" Enter the lower temperature in degree Celsius(between -273.15 to 232.6)")
     t1=input("")
     if t1<-273.15 :
      mprintf("\n")
      clc(1)
     elif t1>232.6 :
        mprintf("\n")
        clc(1)
     elif t1>-273.15 :
        dum=1
end
end
hum=0
while hum==0:
    mprintf(" Enter the higher temperature in degree Celsius(between -273.15 to 64.02)")
    t2=input("")
    if t2<-273.15 :
        mprintf("\n")
        clc(1)
    elif t2>232.6 :
        mprintf("\n")
        clc(1)
    elif t2<t1 :
        mprintf("\n")
        clc(1)
    elif t2>t1 :
        hum=1;
    end
    end
    mprintf(" Enter step size in degree Celsius")
    t3=input("")
    for s in range (t1,t2,t3):
     t=s+273.15;
     if s<=-273.150     : 
      mprintf("Temperature %f degree Celsius is less than absolute zero\n",s)
     elif s<=0 :
      p=pow(10,((-2751/t)-(75*(exp(-2560/t)))-(1.01*log10(t))+13.797))
      pp=p*1.0135/760/1000
      mprintf("Vapour pressure of UF6 at temperature %f degree Celsius is: %f milli Bars\n",s,pp)
     elif s<=64 :
      p=pow(10,(6.3853+.0075377*s-(942.76/(s+183.416))))
      pp=p*1.0135/760/1000
      mprintf(' Vapour pressure of UF6 at temperature %f degree Celsius is: %f milli Bars\n',s,pp)
     elif s<=116 :
      p=pow(10,(6.99464-(1126.288/(s+221.963))))
      pp=p*1.0135/760/1000
      mprintf(' Vapour pressure of UF6 at temperature %f degree Celsius is: %f milli Bars\n',s,pp)
     elif s<=232.6 :
      p=pow(10,(7.69069-(1683.165/(s+302.148))))
      pp=p*1.0135/760/1000
      mprintf(' Vapour pressure of UF6 at temperature %f degree Celsius is: %f milli Bars\n',s,pp)
     elif s>232.6:
      print "Temperature is above the critical point"
end
end
disp("(From modified Antoine equation)")
mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
#VAPOUR PRESSURE RANGE OF TEMP GRAPH
mprintf('\n\n Do you want a graphical representation of the data ?\n 1.Yes\n 2.No\n Please enter a value corresponding to your choice')
z=input("")
if z<1 :
 print("Please enter a value from 1 to 2 only")
elif z==1 :
 k=0;
 m=t1
 while m<=t2:
  m=m+t3;
  k=k+1;
  end
  x=zeros(1,k)
  for g in range(1,k):
   x(1,g)=t1+(g-1)*t3
   end
  D=zeros(1,k)
  DD=[1:k]
  for f=1:k
if x(1,f)<=0 :
    D(1,f)=10^((-2751/(x(1,f)+273.15))-(75*(%e^(-2560/(x(1,f)+273.15))))-(1.01*log10(x(1,f)+273.15))+13.797)
    DD(1,f)=D(1,f)*1.0135/760/1000
elif x(1,f)<=64 :
    D(1,f)=10^(6.3853+.0075377*x(1,f)-(942.76/(x(1,f)+183.416)))
    DD(1,f)=D(1,f)*1.0135/760/1000
elif x(1,f)<=116 :
    D(1,f)=10^(6.99464-(1126.288/(x(1,f)+221.963)))
    DD(1,f)=D(1,f)*1.0135/760/1000
elif x(1,f)<=232.6 :
    D(1,f)=10^(7.69069-(1683.165/(x(1,f)+302.148)))
    DD(1,f)=D(1,f)*1.0135/760/1000
    end
    end
    clf
    plot(x,DD)
    xlabel('Temperature (in degree Celsius)'),ylabel('Vapour Pressure (in milli Bar)'),title(['Variation in the vapour pressure UF6 with temperature'])
    elif z>2 :
    mprintf("Enter a value from 1 to 2 only")
    end
elif n>2 :
    printf("Please enter value from 1 to 2 only")
#VAPOUR PRESSURE ENDS
end

15 :
    mprintf("\n")
    clc(1)
elif t>64.02 :
        mprintf("\n")
        clc(1)
    elif t>-273.15 :
        dum=1;
    end
    end
s=t+273.15;
if t<-273.15 :
    disp("Temperature  "+string(t)+"  degrees Celsius is less than the absolute temperature")
elif t<=64.02 :
    d=((-.0038278)*(s)+6.214799)*1000;
    mprintf('\n The density of solid UF6 at temperature %f degrees centrigrade is %f kg/(m)^3',t,d)
    disp("(From data from British Data Sheets; Wechsler and Hoge and Hoard and Stroupe)")
    mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
else disp("Temperature  "+string(t)+"  degrees Celsius is greater than the triple point temperature")
    end
elif n==2 :
    #SOLID DENSITY RANGE OF TEMP CALCULATION
    dum=0;
    while dum==0;
    mprintf(" Enter the lower temperature in degree Celsius(between -273.15 to 64.02)")
    t1=input("")
    if t1<-273.15 :
    mprintf("\n")
    clc(1)
elif t1>64.02 :
        mprintf("\n")
        clc(1)
    elif t1>-273.15 :
    dum=1
end
end
hum=0;
while hum==0;
    mprintf(" Enter the higher temperature in degree Celsius(between -273.15 to 64.02)")
    t2=input("")
    if t2<-273.15 :
        mprintf("\n")
        clc(1)
    elif t2>64.02 :
        mprintf("\n")
        clc(1)
    elif t2<t1 :
        mprintf("\n")
        clc(1)
        elif t2>t1 :
        hum=1;
    end
    end
    mprintf(" Enter step size in degree Celsius")
    t3=input("")
    for t=t1:t3:t2
s=t+273.15;
if t<-273.15 :
    disp("Temperature  "+string(t)+"  degrees Celsius is less than the absolute temperature")
elif t<=64.02 :
    d=(-.0038278)*(s)+6.214799;
    dd=1000*d;
    mprintf('\n The density of solid UF6 at temperature %f degrees centrigrade is %f kg/(m)^3\n',t,dd)
elif t>64.02 : 
    d=(-.0038278)*(s)+6.214799;
    dd=1000*d;
 mprintf('\n The density of solid UF6 at temperature %f degrees centrigrade is %f kg/m)^3\n',t,dd)
    disp("Temperature  "+string(t)+"  degrees Celsius is greater than the triple point temperature")
    end
end
    disp("(From data from British Data Sheets; Wechsler and Hoge and Hoard and Stroupe)")
    #SOLID DENSITY RANGE OF TEMP GRAPH
    mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
    mprintf('\n\n Do you want a graphical representation of the data ?\n 1.Yes\n 2.No\n Please enter a value corresponding to your choice')
    z=input("")
    if z<1 :
        mprintf("Please enter a value from 1 to 2 only")
    elif z==1 :
         k=0;
     m=t1
    while m<=t2
        m=m+t3;
        k=k+1;
    end
    x=zeros(1,k)
    for g=1:k
        x(1,g)=t1+(g-1)*t3
    end
    D=zeros(1,k)
    for f=1:k
        if x(1,f)<-273.15 :
            D(1,f)=0
elif x(1,f)>=-273.15 :
    D(1,f)=((-.0038278)*(x(1,f)+273.15)+6.214799)*1000;
    end
    end
    clf
    plot(x,D)
    xlabel('Temperature (in degree Celsius)'),ylabel('Density (in kg/(m)^3)'),title(['Variation in the density of Solid UF6 with temperature'])
elif z>2 :
    mprintf("Enter a value from 1 to 2 only")
    end
elif n>2 :
    mprintf("Enter a value from 1 to 2 only")
    end
elif i==2 :
    #LIQUID DENSITY
    mprintf('Do you want to find out the density for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n')
    n=input("")
    if n<1 :
    printf("Please enter a value from 1 to 2 only")
elif n==1 :
    #LIQUID DENSITY SINGLE TEMP CALCULATION
    dum=0;
    while dum==0;
    mprintf(" Enter the temperature in degree Celsius(between 64.02 to 409.58)")
    t=input("")
    if t<64.02 :
    mprintf("\n")
    clc(1)
elif t>409.58 :
        mprintf("\n")
        clc(1)
    elif t>64.02 :
        dum=1;
    end
    end
s=t+273.15;
if t<-273.15 :
    disp("Temperature  "+string(t)+"  degrees Celsius is less than the absolute temperature")
elif t<64.02 :
    disp("Temperature  "+string(t)+"  degrees Celsius is less than the triple point temperature")
    elif t<=409.58 :
    d=(3.63-5.805*10^(-3)*(t-64.025)-1.36*10^(-5)*(t-64.025)^2)*1000
    mprintf('\n The density of liquid UF6 at temperature %f degrees centrigrade is %f kg/(m)^3',t,d)
   disp("(From Hoge and Wechsler equation)")
   mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
elif t>409.58
    disp("Temperature not in scope of equation")
    end
elif n==2 :
    #LIQUID DENSITY RANGE OF TEMP CALCULATION
    dum=0;
    while dum==0;
    mprintf(" Enter the lower temperature in degree Celsius(between 64.02 to 409.58)")
    t1=input("")
    if t1<64.02 :
    mprintf("\n")
    clc(1)
elif t1>409.58 :
        mprintf("\n")
        clc(1)
    elif t1>64.02 :
    dum=1
end
end
hum=0;
while hum==0;
    mprintf(" Enter the higher temperature in degree Celsius(between 64.02 to 409.58)")
    t2=input("")
    if t2<64.02 :
        mprintf("\n")
        clc(1)
    elif t2>409.58 :
        mprintf("\n")
        clc(1)
    elif t2<=409.58 :
        hum=1;
    end
end
    mprintf(" Enter step size in degree Celsius")
    t3=input("")
    for t=t1:t3:t2
s=t+273.15;
if t<-273.15 :
    disp("Temperature  "+string(t)+"  degrees Celsius is less than the absolute temperature")
elif t<64.02 :
    disp("Temperature  "+string(t)+"  degrees Celsius is less than the triple point temperature")
    elif t<=409.58 :
    d=(3.63-5.805*10^(-3)*(t-64.025)-1.36*10^(-5)*(t-64.025)^2)*1000
    mprintf('\n The density of liquid UF6 at temperature %f degrees centrigrade is %f kg/(m)^3',t,d)
elif t>409.58
    disp("Temperature   "+string(t)+"  degrees Celsius not in scope of equation")
    end
end
disp("(From Hoge and Wechsler equation)")
   mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
   #LIQUID DENSITY RANGE OF TEMP GRAPH
   mprintf('\n\n Do you want a graphical representation of the data ?\n 1.Yes\n 2.No\n Please enter a value corresponding to your choice')
    z=input("")
    if z<1 :
        mprintf("Please enter a value from 1 to 2 only")
    elif z==1 :
         k=0;
     m=t1
    while m<=t2
        m=m+t3;
        k=k+1;
    end
    x=zeros(1,k)
    for g=1:k
        x(1,g)=t1+(g-1)*t3
    end
    D=zeros(1,k)
    for f=1:k
        if x(1,f)<-273.15 :
            D(1,f)=0;
elif x(1,f)<64.02 :
D(1,f)=0;
    elif x(1,f)<=409.58 :
D(1,f)=(3.63-5.805*10^(-3)*(x(1,f)-64.025)-1.36*10^(-5)*(x(1,f)-64.025)^2)*1000
elif x(1,f)>409.58
D(1,f)=(3.63-5.805*10^(-3)*(x(1,f)-64.025)-1.36*10^(-5)*(x(1,f)-64.025)^2)*1000;
    end
    end
    clf
    plot(x,D)
    xlabel('Temperature (in degree Celsius)'),ylabel('Density (in kg/(m)^3)'),title(['Variation in the density of Liquid UF6 with temperature'])
    elif z>2 :
    mprintf("Enter a value from 1 to 2 only")
    end
   elif n>2 :
    printf("Please enter a value from 1 to 2 only")
   end
elif i==3 :
    #GAS DENSITY
    mprintf('Do you want to find out the density for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n')
    n=input("")
    if n<1 :
    printf("Please enter a value from 1 to 2 only")
elif n==1 :
    #GAS DENSITY SINGLE TEMP CALCULATION
    mprintf('Please enter the pressure in mm Hg')
    k=input("")
    p=k/760;
     l=((1.3769*10^(6)*p)^(1/3))-273.15
    ll=l-.1*l;
        dum=0;
    while dum==0;
    disp("Enter the temperature in degree Celsius (greater than "+string(ll)+" degrees Celsius)")
    t=input("")
    if t<ll :
    mprintf("\n")
    clc(1)
    elif t>=ll :
        dum=1;
    end
    end
s=t+273.15;
if t<=ll :
     disp("Temperature  "+string(t)+"  degrees Celsius is less than the temperature limit")
     elif t>ll :
    d=(4.291*p)/(s*(1+(-1.3769*10^(6)*p/s^3)));
    mprintf('\n The density of gaseous UF6 at temperature %f degrees centrigrade is %f g/cc',t,d)
    disp("(From Weinstock equation)")
    mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
    end
    #GAS DENSITY RANGE OF TEMP CALCULATIONS
elif n==2 :
    mprintf('Please enter the pressure in mm Hg')
    k=input("")
    p=k/760;
    l=((1.3769*10^(6)*p)^(1/3))-273.15
    ll=l-.1*l;
        dum=0;
    while dum==0;
    disp("Enter the lower temperature in degree Celsius (greater than "+string(ll)+" degrees Celsius)")
    t1=input("")
    if t1<ll :
    mprintf("\n")
    clc(1)
elif t1>=ll :
    dum=1
end
end
hum=0;
while hum==0;
    mprintf(" Enter the higher temperature in degree Celsius")
    t2=input("")
    if t2<ll :
        mprintf("\n")
        clc(1)
    elif t2<=t1 :
        mprintf("\n")
        clc(1)
    elif t2>t1 :
        hum=1;
    end
end
    mprintf(" Enter step size in degree Celsius")
    t3=input("")
    for t=t1:t3:t2
s=t+273.15;
if t<=ll :
     disp("Temperature  "+string(t)+"  degrees Celsius is less than the lower limit temperature")
     elif t>ll :
    d=((4.291*p)/(s*(1+(-1.3769*10^(6)*p/s^3))))*1000;
    mprintf('\n The density of gaseous UF6 at temperature %f degrees centrigrade is %f kg/(m)^3',t,d)
    end
end
disp("(From Weinstock equation)")
    mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
    #GAS DENSITY RANGE OF TEMP GRAPH
     mprintf('\n\n Do you want a graphical representation of the data ?\n 1.Yes\n 2.No\n Please enter a value corresponding to your choice')
    z=input("")
    if z<1 :
        mprintf("Please enter a value from 1 to 2 only")
    elif z==1 :
         k=0;
     m=t1
    while m<=t2
        m=m+t3;
        k=k+1;
    end
    x=zeros(1,k)
    for g=1:k
        x(1,g)=t1+(g-1)*t3
    end
    D=zeros(1,k)
    for f=1:k
        if x(1,f)<=ll :
            D(1,f)=0
        elif x(1,f)>ll :
        D(1,f)=(4.291*p)/((x(1,f)+273.15)*(1+(-1.3769*10^(6)*p/(x(1,f)+273.15)^3)))
    end
    end
    clf
    plot(x,D)
    xlabel('Temperature (in degree Celsius)'),ylabel('Density (in kg/(m)^3)'),title(['Variation in the density of Gaseous UF6 with temperature'])
    elif z>2 :
    mprintf("Enter a value from 1 to 2 only")
    end
elif n>2 :
        printf("Please enter a value from 1 to 2 only")
        end
elif i>3 :
    printf("Please enter a value from 1 to 3 only")
#DENSITY ENDS
end
#VISCOSITY STARTS
elif q==3 :
clc
#PHASE
disp("Welcome to the viscosity portal")
mprintf(' Select the number corresponding to the state of UF6\n 1.Gas\n 2.Liquid\n')
i=input("")
if i<1 :
printf("Please enter a value from 1 to 2 only")
elif i==1 :
    #GAS
    mprintf(' Do you want to find out the viscosity for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n')
    n=input("")
    if n<1 :
    printf("Please enter a value from 1 to 2 only")
elif n==1 :
    #GAS SINGLE TEMP CALCULATION
    dum=0;
    while dum==0;
    mprintf(" Enter the temperature in degree Celsius(greater than -273.15)")
    t=input("")
    if t<=-273.15 :
    mprintf("\n")
    clc(1)
    elif t>-273.15 :
    dum=1
end
end
s=t+273.15;
if t<=-273.15 :
disp("Temperature  "+string(t)+"  degrees Celsius is less than the absolute temperature")
elif t>=-273.15 :
    u=(2.1*(s^.779)*10^(-6))
    mprintf(' The viscosity of the UF6 vapours at %f degree Celsius is\n%f Poise',t,u)
    disp("(From Llewellyns equation)")
    mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
    end
elif n==2 :
    #GAS RANGE OF TEMP CALCULATION
    dum=0;
    while dum==0;
    mprintf(" Enter the lower temperature in degree Celsius (greater than -273.15)")
    t1=input("")
    if t1<=-273.15 :
    mprintf("\n")
    clc(1)
    elif t1>-273.15 :
    dum=1
end
end
hum=0;
while hum==0;
    mprintf(" Enter the higher temperature in degree Celsius (greater than -273.15)")
    t2=input("")
    if t2<=-273.15 :
        mprintf("\n")
        clc(1)
    elif t2<t1 :
        mprintf("\n")
        clc(1)
    elif t2>t1 :
        hum=1;
    end
    end
    mprintf(" Enter step size in degree Celsius")
    t3=input("")
    for t=t1:t3:t2
        s=t+273.15;
        if t<-273.15 :
disp("Temperature  "+string(t)+"  degrees Celsius is less than the absolute temperature")
elif t>=-273.15 :
    u=(2.1*(s^.779)*10^(-6))
    mprintf(' The viscosity of the UF6 vapours at %f degree Celsiusis %f Poise\n',t,u)
    end
end
    disp("(From Llewellyns equation)")
    mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
    #GAS VISCOSITY RANGE OF TEMP GRAPH
    mprintf('\n\n Do you want a graphical representation of the data ?\n 1.Yes\n 2.No\n Please enter a value corresponding to your choice')
    z=input("")
    if z<1 :
        mprintf("Please enter a value from 1 to 2 only")
    elif z==1 :
         k=0;
     m=t1
    while m<=t2
        m=m+t3;
        k=k+1;
    end
    x=zeros(1,k)
    for g=1:k
        x(1,g)=t1+(g-1)*t3
    end
    D=zeros(1,k)
    for f=1:k
        if x(1,f)<-273.15 :
            D(1,f)=0;
    elif x(1,f)>=-273.15 :
        D(1,f)=(2.1*((x(1,f)+273.15)^.779)*10^(-6))
    end
    end
    clf
    plot(x,D)
    xlabel('Temperature (in degree Celsius)'),ylabel('Viscosity (in Poise)'),title(['Variation in the viscosity of Gaseous UF6 with temperature'])
    elif z>2 :
    mprintf("Enter a value from 1 to 2 only")
    end
elif n>2 :
    printf("Please enter a value from 1 to 2 only")
end
elif i==2 :
    #LIQUID VISCOSITY
    mprintf(' Do you want to find out the viscosity for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n')
    n=input("")
    if n<1 :
    printf("Please enter a value from 1 to 2 only")
elif n==1 :
    #LIQUID VISCOSITY SINGLE TEMP CALCULATION
    dum=0;
    while dum==0;
    mprintf(" Enter the temperature in degree Celsius(greater than 64.02)")
    t=input("")
    if t<=64.02 :
    mprintf("\n")
    clc(1)
    elif t>64.02 :
    dum=1
end
end
s=t+273.15;
if t<=64.02 :
disp("Temperature  "+string(t)+"  degrees Celsius is less than the triple point temperature")
elif t>64.02 :
        u=(.1271*10^(-3)*%e^(1217/s))
    mprintf(' The viscosity of the UF6 liquid at %f degrees Celsius is %f Poise',t,u)
    disp("(From Cohens equation)")
    mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
    end
elif n==2 :
    #LIQUID VISCOSITY   RANGE OF TEMP CALCULATION
    dum=0;
    while dum==0;
    mprintf(" Enter the lower temperature in degree Celsius (greater than 64.02)")
    t1=input("")
    if t1<=64.02 :
    mprintf("\n")
    clc(1)
    elif t1>64.02 :
    dum=1
end
end
hum=0;
while hum==0;
    mprintf(" Enter the higher temperature in degree Celsius (greater than 64.02)")
    t2=input("")
    if t2<64.02 :
        mprintf("\n")
        clc(1)
    elif t2<t1 :
        mprintf("\n")
        clc(1)
    elif t2>t1 :
        hum=1;
    end
    end
    mprintf(" Enter step size in degree Celsius")
    t3=input("")
    for t=t1:t3:t2
        s=t+273.15;
        if t<=-140 :
disp("Temperature  "+string(t)+"  degrees Celsius is less than the absolute temperature")
elif t>-140 :
        u=(.1271*10^(-3)*%e^(1217/s))
    mprintf(' The viscosity of the UF6 liquid at %f degrees Celsius is %f Poise\n',t,u)
    end
end
    disp("(From Llewellyns equation)")
    mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
    #LIQUID VISCOSITY RANGE OF TEMP GRAPH
    mprintf('\n\n Do you want a graphical representation of the data ?\n 1.Yes\n 2.No\n Please enter a value corresponding to your choice')
    z=input("")
    if z<1 :
        mprintf("Please enter a value from 1 to 2 only")
    elif z==1 :
         k=0;
     m=t1
    while m<=t2
        m=m+t3;
        k=k+1;
    end
    x=zeros(1,k)
    for g=1:k
        x(1,g)=t1+(g-1)*t3
    end
    D=zeros(1,k)
    for f=1:k
        if x(1,f)<=-140 :
            D(1,f)=0
        elif x(1,f)>-140 :
            D(1,f)=(.1271*10^(-3)*%e^(1217/(x(1,f)+273.15)))
            end
    end
    clf
    plot(x,D)
    xlabel('Temperature (in degree Celsius)'),ylabel('Viscosity (in Poise)'),title(['Variation in the viscosity of Liquid UF6 with temperature'])
    elif z>2 :
    mprintf("Enter a value from 1 to 2 only")
    end
elif n>2 :
    printf("Please enter a value from 1 to 2 only")
end
elif i>2 :
    printf("Please enter a value from 1 to 2 only")
#VISCOSITY ENDS
end
#THERMAL CONDUCTIVITY STARTS
elif q==4 :
clc
disp("Welcome to the thermal conductivity portal")
#PHASE
mprintf(' Select the number corresponding to the state of UF6\n 1.Solid\n 2.Gas\n')
i=input("")
if i<1 :
    printf("Please enter a number from 1 to 2 only")
elif i==1 :
    mprintf(' Do you want to find out the thermal conductivity for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n')
    n=input("")
    if n<1 :
    printf("Please enter a value from 1 to 2 only")
elif n==1 :
    #SOLID THERM COND SINGLE TEMP
    dum=0;
    while dum==0;
    mprintf(" Enter the temperature in degree Celsius (between -253.8 to 64.02 degree Celsius)")
    t=input("")
    if t<=-253.8 :
    mprintf("\n")
    clc(1)
elif t>64.02 :
    mprintf("\n")
    clc(1)
elif t<=64.02 :
    dum=1
end
end
s=t+273.15;
if t<-253.8 :
    disp("Please enter a temperature within the given range")
    elif t<=64.02 :
    k=(-3.645*10^(-2)+1.895*10^(-3)*s)
    mprintf(' The thermal conductivity of the solid UF6 at %f degrees Celsius is \n%f  Watt/(m.K)',t,k)
mprintf('\n Source:\nCORRELATION OF THE THERMOPHYSICAL PROPERTIES OF URANIUM HEXAFLUORIDE OVER A WIDE RANGE OF TEMPERATURE AND PRESSURE \nby J. C. Anderson; C. P. Kerr and W. R. Williams')
elif t>64.02 :
    disp("Temperature "+string(t)+" degree Celsius is greater than the triple point temperature ")
    end
elif n==2 :
    #SOLID THERM COND RANGE OF TEMP
    dum=0;
    while dum==0;
    mprintf(" Enter the lower temperature in degree Celsius (between -253.8 to 64.02 degree Celsius)")
    t1=input("")
    if t1<=-253.8 :
    mprintf("\n")
    clc(1)
elif t1>64.02 :
    mprintf("\n")
    clc(1)
elif t1<=64.02 :
    dum=1
end
end
hum=0;
while hum==0;
    mprintf(" Enter the higher temperature in degree Celsius (between -253.8 to 64.02 degree Celsius)")
    t2=input("")
    if t2<-253.8 :
        mprintf("\n")
        clc(1)
        elif t2>64.02 :
    mprintf("\n")
    clc(1)
    elif t2<t1 :
        mprintf("\n")
        clc(1)
    elif t2>t1 :
        hum=1;
    end
    end
    mprintf(" Enter step size in degree Celsius")
    t3=input("")
    for t=t1:t3:t2
        s=t+273.15;
        if t<-253.8 :
disp("Temperature  "+string(t)+"  degrees Celsius is less than the given range")
    elif t<=64.02 :
    k=(-3.645*10^(-2)+1.895*10^(-3)*s)
    mprintf(' The thermal conductivity of the solid UF6 is %f  Watt/(m.K)\n',k)
elif t>64.02 :
    disp("Temperature "+string(t)+" degree Celsius is greater than the triple point temperature ")
    end
end
mprintf('\n Source:\nCORRELATION OF THE THERMOPHYSICAL PROPERTIES OF URANIUM HEXAFLUORIDE OVER A WIDE RANGE OF TEMPERATURE AND PRESSURE \nby J. C. Anderson; C. P. Kerr and W. R. Williams')
#SOLID THERM COND GRAPH
mprintf('\n\n Do you want a graphical representation of the data ?\n 1.Yes\n 2.No\n Please enter a value corresponding to your choice')
    z=input("")
    if z<1 :
        mprintf("Please enter a value from 1 to 2 only")
    elif z==1 :
         k=0;
     m=t1
    while m<=t2
        m=m+t3;
        k=k+1;
    end
    x=zeros(1,k)
    for g=1:k
        x(1,g)=t1+(g-1)*t3
    end
    D=zeros(1,k)
    for f=1:k
        if x(1,f)<-253.8 :
            D(1,f)=0;
        elif x(1,f)<=64.02 :
        D(1,f)=(-3.645*10^(-2)+1.895*10^(-3)*(x(1,f)+273.15))
    elif x(1,f)>64.02 :
        D(1,f)=0
        end
    end
    clf
    plot(x,D)
    xlabel('Temperature (in degree Celsius)'),ylabel('Thermal Conductivity (W/(m.K))'),title(['Variation in the thermal conductivity of solid UF6 with temperature'])
    elif z>2 :
    mprintf("Enter a value from 1 to 2 only")
    end
elif n>2 :
    printf("Please enter a value from 1 to 2 only")
end
elif i==2 :
    #GAS THERM COND 
    mprintf(' Do you want to find out the viscosity for\n 1.Single temperature\n 2.Range of temperaure?\n Please enter the number corresponding to your choice\n')
    n=input("")
    if n<1 :
    printf("Please enter a value from 1 to 2 only")
elif n==1 :
    #GAS THERMAL COND SINGLE TEMP
        dum=0;
    while dum==0;
    mprintf(" Enter the lower temperature in degree Celsius (greater than -238)")
    t=input("")
    if t<=-238 :
    mprintf("\n")
    clc(1)
elif t>-238 :
    dum=1
end
end
s=t+273.15;
if t<=-273.15 :
    disp("Temperature "+string(t)+" degree Celsius is less than the absolute temperature")
elif t<-238 :
    disp("Temperature"+string(t)+" degree Celsius is less than the lower temperature limit")
    elif t>=-238 :
    k=(1.46*(1+.0042*t)*10^(-5))*418
    mprintf(' The thermal conductivity of the gaseous UF6 at %f degrees Celsius is \n%f  W/(m.K)',t,k)
    disp(" (Using the Taylor and Agron;Llewellyn and Fleischmann equations)")
    mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
    end
elif n==2 :
    #GAS THERM COND RANGE OF TEMP
    dum=0;
    while dum==0;
    mprintf(" Enter the lower temperature in degree Celsius (greater than -238)")
    t1=input("")
    if t1<=-238 :
    mprintf("\n")
    clc(1)
elif t1>-238 :
    dum=1
end
end
hum=0;
while hum==0;
    mprintf(" Enter the higher temperature in degree Celsius (greater than -238)")
    t2=input("")
    if t2<-238 :
        mprintf("\n")
        clc(1)
    elif t2<t1 :
        mprintf("\n")
        clc(1)
    elif t2>t1 :
        hum=1;
    end
    end
    mprintf(" Enter step size in degree Celsius")
    t3=input("")
    for t=t1:t3:t2
        s=t+273.15;
        if t<=-273.15 :
    disp("Temperature "+string(t)+" degree Celsius is less than the absolute temperature")
elif t<-238 :
    disp("Temperature"+string(t)+" degree Celsius is less than the lower temperature limit")
    elif t>=-238 :
    k=(1.46*(1+.0042*t)*10^(-5))*418
    mprintf(' The thermal conductivity of the gaseous UF6 at %f degrees Celsius is %f  W/(m.K)\n',t,k)
    end
   end
disp(" (Using the Taylor and Agron;Llewellyn and Fleischmann equations)")
    mprintf('\n Source:\n Uranium Hexaflouride: A Survey of the Physico-Chemical Properties(GAT 280)\n by R. DeWitt')
    #GAS THERM COND GRAPH
mprintf('\n\n Do you want a graphical representation of the data ?\n 1.Yes\n 2.No\n Please enter a value corresponding to your choice')
    z=input("")
    if z<1 :
        mprintf("Please enter a value from 1 to 2 only")
    elif z==1 :
         k=0;
     m=t1
    while m<=t2
        m=m+t3;
        k=k+1;
    end
    x=zeros(1,k)
    for g=1:k
        x(1,g)=t1+(g-1)*t3
    end
    D=zeros(1,k)
    for f=1:k
        if x(1,f)<-238 :
            D(1,f)=0
            elif x(1,f)>=-238 :
            D(1,f)=(1.46*(1+.0042*x(1,f))*10^(-5))*418
            end
    end
    clf
    plot(x,D)
    xlabel('Temperature (in degree Celsius)'),ylabel('Thermal Conductivity  ( W / (m.K) )'),title(['Variation in the thermal conductivity of gaseous UF6 with temperature'])
    elif z>2 :
    mprintf("Enter a value from 1 to 2 only")
    end
elif n>2 :
    printf("Please enter a value from 1 to 2 only")
end
elif i>2
    printf("Please enter a number from 1 to 2 only")
#THERMAL CONDUCTIVITY ENDS
end
elif q>4 :
    printf("Please enter a value from 1 to 4 only")
    #ASKING FOR PROPERTY ENDS
end
#ASKING FOR RE-EVALUATING STARTS
mprintf("\n\n Do you want to find out any other property?\n 1.Yes\n 2.No\n Enter the number corresponding to your answer:")
z=input("")
if z==2 :
    printf("\n Thank you.")
    aaa=0
#ASKING FOR RE-EVALUATING ENDS
end
end

