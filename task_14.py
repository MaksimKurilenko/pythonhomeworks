units_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
def roman_to_arabic (roman_number):
    roman_number = str.upper(roman_number)
    arabic_result = 0
    prev_value = 0  
    for i in roman_number[::-1]:
        arabic_value = units_dict[i]
        if arabic_value < prev_value:
            arabic_result -= arabic_value
        else:
            arabic_result += arabic_value
    prev_value = arabic_value 
    return arabic_result
roman_value_1 = input("Please enter a first Roman number: ")
arabic_result_1 = roman_to_arabic(roman_value_1)
roman_value_2 = input("Please enter a second Roman number: ")
arabic_result_2 = roman_to_arabic(roman_value_2)

arabic_sum =int(arabic_result_1 + arabic_result_2)
arabic_minus = int(arabic_result_1 - arabic_result_2)
if 1 <= arabic_sum < 4000 and 1 <= arabic_minus < 4000:
    units_roman = {0:"", 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII",9:"IX"}
    tens_roman = {0:"", 1:"X", 2:"XX", 3:"XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX", 8:"LXXX",9:"XC"}
    hundreds_roman = {0:"", 1:"C", 2:"CC", 3:"CCC", 4:"CD", 5:"D", 6:"DC", 7:"DCC", 8:"DCCC",9:"CM"}
    thousands_roman = {0:"", 1:"M", 2:"MM", 3:"MMM",}
    def arabic_to_roman(arabic_number):
        roman_thousands = arabic_number//1000
        roman_hundreds = (arabic_number%1000)//100
        roman_tens = (arabic_number%100)//10
        roman_units = arabic_number%10
        roman_number = thousands_roman[roman_thousands]+hundreds_roman[roman_hundreds]+tens_roman[roman_tens]+units_roman[roman_units]
        return roman_number
    roman_sum = arabic_to_roman(arabic_sum)
    roman_minus = arabic_to_roman(arabic_minus)
    print("Sum of your values is:", roman_sum)
    print("Difference of your values is: ", roman_minus)

else:
    print("Error. Your values can`t be converted")



