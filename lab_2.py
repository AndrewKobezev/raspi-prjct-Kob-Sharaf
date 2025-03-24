def get_op():
    while True:
        operat = input('введите операцию\n')
        if operat in ['-','/','*','+']:
            return operat
            break
        
        else:
            pass  
    
def get_num():
    
    while True:
        num_1 = input('введите 1\n')
        num_2 = input('введите 2\n')
       
        try:
            
            num_1 = float(num_1)
            num_2 = float(num_2)
                        
            return num_1, num_2
            break
        
        except:
            print ('ВВОДИ ЧИСЛА!!!')
       
            
def calc(op, num1, num2):
    if op == '/':
        while num2 == 0:
            num2 = input('ДЕЛЕНИЕ НА НОЛЬ. ВВЕДИТЕ ЕЩЁ РАЗ!\n')
            num2 = float(num2)
    else:
        pass
        
    arg = 'x'+op+'y'
    f = lambda x,y: eval(arg)
    print(f'{num1} {op} {num2} = ', f(num1, num2))
        
            
       
op = get_op()
num1, num2 = get_num()



calc(op, num1, num2)
