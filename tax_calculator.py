def calc_tax(income):
    tax=income-88000-90000-128000
    if(tax<=540000):
        return int(tax*0.05)
    elif(tax>540000 and tax<=1210000):
        return int((540000*0.05)+(tax-540000)*0.12)
    elif(tax>1210000 and tax<=2420000):
        return int((540000*0.05)+((1210000-540000)*0.12)+(tax-1210000)*0.2)
    elif(tax>2420000 and tax<=4530000):
        return int((540000*0.05)+((1210000-540000)*0.12)+((2420000-1210000)*0.2)+(tax-2420000)*0.3)
    elif(tax>4530000 and tax<=10310000):
        return int((540000*0.05)+((1210000-540000)*0.12)+((2420000-1210000)*0.2)+((4530000-2420000)*0.3)+(tax-4530000)*0.4)
    elif(tax>10310000):
        return int((540000*0.05)+((1210000-540000)*0.12)+((2420000-1210000)*0.2)+((4530000-2420000)*0.3)+((10310000-4530000)*0.4)+(tax-10310000)*0.45)
    else:
        return 0
