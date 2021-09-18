def simple_interest(p,t,r):
     si=(p*t*r)/(30*100)
     return round(si), round((si+p))


def compound_interest(priciple,rate,time):
     Amount=priciple * (pow((1+(rate/100)),time))
     CI=Amount-priciple
     return round(CI),round((CI+priciple))
