def test_function():
 
    def inner_function():
        print("Я в области видимости функции test_function")
 
    inner_function()
 
test_function()

inner_function()


'''

Я в области видимости функции test_function
Traceback (most recent call last):
  File "C:/Users/user/Desktop/Python/Test.py", line 10, in <module>
    inner_function()
NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

Функция inner_function вне функции test_function невидна

'''
