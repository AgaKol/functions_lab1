def return_10():
    return 10


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


def length_of_string(string):
    return len(string)


def join_string(string1, string2):
    return string1 + string2


def add_string_as_number(a, b):
    return int(a) + int(b)


months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


def number_to_full_month_name(n):
    return months[n-1]


months_short = ["Jan", "Feb", "Mar", "Apr", "May",
                "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def number_to_short_month_name(a):
    return months_short[a-1]


def volume_of_cube(a):
    return a**3


def reverse_string(a):
    return a[::-1]


def fahrenheit_to_celsius(a):
    return (a-32)*(5/9)


print(fahrenheit_to_celsius(70))
