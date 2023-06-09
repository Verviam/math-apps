import cmath

def arithmeticSequence():
    print('Arithmetic Sequence Chosen')
    a1 = float(input('What is the first term? '))
    diff = float(input('What is the common difference? '))
    position = int(input('What is the position of the term being found? '))
    
    aN = a1 + diff * (int(position) - 1)
    print('The ' + str(position) + ' term is ' + str(int(aN)))
    return aN
 
def geometricSequence():
    print('Geometric Sequence Chosen')
    a1 = float(input('What is the first term? '))
    ratio = float(input('What is the common ratio? '))
    position = int(input('What is the position of the term being found? '))

    aN = a1 * pow(ratio, position-1)
    print('The ' + str(position) + 'term is ' + str(int(aN)))
    return aN

def arithmeticSeries():
    print('Arithmetic Series Chosen')
    a1 = float(input('What is the first term? '))
    n = float(input('How many numbers are in the series? '))
    aN = input('What is the ' + str(int(n)) + ' number in the sequence? [Type A to use Arithmetic Explicit Sequence to find out] ')

    if str(aN) == 'A':
        arithmeticSequence()
        again = input('Do you want to go back to the Arithmetic Series Calculator? Y/N ')
        if again == ('Y'):
            arithmeticSeries()
    Sn = n * (a1 + float(aN))/2
    print('The sum of all the numbers is ' + 'Sn')
    return Sn

# fix value error convert string to float: A

def geometricSeries():
    ...
    
def geometricArithmetic():
    print('''
    Arithmetic Sequence: '1'
    Arithmetic Series: '2'
    Geometric Sequence: '3'
    Geometric Series: '4'
    ''')
    choose = float(input('Which formula do you want to use? '))

    if choose == 1:
        arithmeticSequence()
    elif choose == 2:
        arithmeticSeries()
    elif choose == 3:
        geometricSequence()
    elif choose == 4: 
        geometricSeries()
    else:
        geometricArithmetic()
    again = input('Do you want to run this program again? Y/N ')
    if again == ('Y'):
        geometricArithmetic()

geometricArithmetic()
