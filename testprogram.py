def test ():
    from uncertainties import ufloat
    from uncertainties import unumpy
    from uncertainties.umath import *
    numbers = unumpy.uarray(([1,2,3,4,5],[0.1,0.2,0.3,0.4,0.5]))
    print numbers
    print "Mean: {}".format(numbers.mean())
    print unumpy.sin(numbers)
    for i in numbers:
       print "Number: {}, Uncertainty: {}, Square of number: {}".format(i.nominal_value, i.std_dev(), i**2)

test()
    
