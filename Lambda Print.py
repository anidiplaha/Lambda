#A REGULAR FUNCTION
def rkm( funct, *args ):
def printer_one( arg ):
        return print (arg)
        def printer_two( arg ):
                print(arg)
#CALL A REGULAR FUNCTION 
rkm( printer_one, 'printer 1 REGULAR CALL' )
rkm( printer_two, 'printer 2 REGULAR CALL \n' )
#CALL A REGULAR FUNCTION THRUGH A LAMBDArkm(lambda: printer_one('printer 1 LAMBDA CALL'))
rkm(lambda: printer_two('printer 2 LAMBDA CALL'))
