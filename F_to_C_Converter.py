## Convert Celcius to Farenheight Function

def c_to_f(deg_c):
    if deg_c < -273.15:
        print('No no that\'s way too low')
    else:
        deg_f = (deg_c * 9 / 5) + 32
        return deg_f

print(c_to_f(input('How hot is it though? ')))

# printing 10 from this dictionary

# money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
# 
# ten = money['under_bed'][1]
# print ten 

## Conditionals



v = 5

if v < 4:
    print 'It was less than 4'
elif v == 5:
    print 'Hell yeah pimps'
else:
    print 'It was greater than 4'
exit

name = 'Jacob'

if name == "Jacob":
    print "Looks like your name is Jacob"
else:
    print "You name isn't Jacob"
exit


