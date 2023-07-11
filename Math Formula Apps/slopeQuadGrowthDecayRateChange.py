import cmath

def slopeApp():
    
    yTwo = float(input('What is your Y two? '))
    yOne = float(input('What is your Y one? '))
    xTwo = float(input('What is your X Two? '))
    xOne = float(input('What is your X One? '))

    try: 
        total = (yTwo-yOne)/(xTwo-xOne)
        print(total)
    except ZeroDivisionError:
        print('Undefined')

def growthOrDecay():

    a = input('What is the starting amount? ')
    r = 1.0 #rate calculation (growth): change addition symbol to subtraction if decay

    r2 = input('What is the rate of growth or decay? ')
    t = input('How long in years? ') #time
    growth_decay = input('Do you want growth or decay? (G/D) ')
    

    rateG = float(r) + float(r2)
    amountG = float(a) * rateG

    rateD = float(r) - float(r2)
    amountD = float(a) * rateD

    try:
        if growth_decay == 'G':
            total = pow(amountG, float(t))
        elif growth_decay == 'D':
            total = pow(amountD, float(t))
        print(total)
    except UnboundLocalError:
        print('Please write G or D in uppercase')

def quadraticFormula():

    a = float(input('What is your A value? '))
    b = float(input('What is your B value? '))
    c = float(input('What is your C value? '))
    print('A: ' + str(a),' B: ' + str(b),' C: ' + str(c))

    root1 = 0.0
    root2 = 0.0

    root1 = (-b + cmath.sqrt(b*b - 4*a*c)) / (2 * a)
    root2 = (-b - cmath.sqrt(b*b - 4*a*c)) / (2 * a)

    print(root1)
    print(root2)

def rateChange():
    
    new = float(input('What is your new value? '))
    old = float(input('What is your old value? '))

    try:
        total = (old-new)/old * 100
        print('Your rate of change is ' + str(total) + '%')
    except ZeroDivisionError: 
        print('Cannot divide by 0')

def formulaApp():
    print('''
    Slope App : '1'
    Quadratic Formula App: '2'
    Growth and Decay App: '3'
    Rate of Change: '4'
    ''')
    calc_again = input('What formula app do you want to use? ')
    if calc_again == '1':
        slopeApp()
    elif calc_again == '2':
        quadraticFormula()
    elif calc_again == '3':
        growthOrDecay()
    elif calc_again == '4':
        rateChange()
    else:
        formulaApp()
    again = input('Do you want to run this program again? Y/N ')
    if again == ('Y'):
        formulaApp()

formulaApp()
