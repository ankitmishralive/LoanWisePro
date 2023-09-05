

def dependent_Transformer(DEPENDENTS):

    if(DEPENDENTS=='1'):
                    DEPENDENTS_1 = 1
                    DEPENDENTS_2 = 0
                    DEPENDENTS_3 = 0

    elif(DEPENDENTS == '2'):
                    DEPENDENTS_1 = 0
                    DEPENDENTS_2 = 1
                    DEPENDENTS_3 = 0
    
    elif(DEPENDENTS=="3+"):
                    DEPENDENTS_1 = 0
                    DEPENDENTS_2 = 0
                    DEPENDENTS_3 = 1
    else:
                    DEPENDENTS_1 = 0
                    DEPENDENTS_2 = 0
                    DEPENDENTS_3 = 0  

    return DEPENDENTS_1,DEPENDENTS_2,DEPENDENTS_3

    


def propertyArea_Transformer(PROPERTY_AREA):

        if(PROPERTY_AREA=="Semiurban"):
                        semiurban=1
                        urban=0
        elif(PROPERTY_AREA=="Urban"):
                        semiurban=0
                        urban=1
        else:
                        semiurban=0
                        urban=0
        return semiurban,urban

