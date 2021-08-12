Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import Budget
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import Budget
ModuleNotFoundError: No module named 'Budget'
>>> import Budget; print(calcBills())
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import Budget; print(calcBills())
ModuleNotFoundError: No module named 'Budget'
>>> import Budget; print(Budget.calcBills())
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import Budget; print(Budget.calcBills())
ModuleNotFoundError: No module named 'Budget'
>>> print(Budget.calcBills())
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(Budget.calcBills())
NameError: name 'Budget' is not defined
>>> 