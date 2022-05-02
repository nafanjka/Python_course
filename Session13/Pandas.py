#Installing pandas
#Please make sure you have pandas installed. You can install it with pip from your computer or Atom/VS Code terminal/cmd just like you have installed other third-party packages. Please execute one of the commands below to do the installation depending on what version of Python you are using:

#pip3.10 install pandas

#or

#pip3.9 install pandas

#or

#pip3.8 install pandas

#etc.

#Also, in the next lecture, we will use an enhanced Python interactive shell called IPython.

#IPython is just like the standard shell you get when you run Python, but IPython provides better printing for large text. This ability makes IPython suitable for data analysis because the program prints data in a well-structured format. You can install IPython with pip:

#pip3.10 install ipython

#or

#pip3.9 install ipython

#or

#pip3.8 install ipython

#in terminal:
#ipython
#In [1]: import pandas

#In [2]: df1=pandas.DataFrame([[2,4,6],[10,20,30]])

#In [3]: df1
#Out[3]: 
#    0   1   2
#0   2   4   6
#1  10  20  30

#In [5]: df1=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"])

#In [6]: df1
#Out[6]: 
#   Price  Age  Value
#0      2    4      6
#1     10   20     30

#In [7]: df1=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"],index=["First","Second"])

#In [8]: df1
#Out[8]: 
#        Price  Age  Value
#First       2    4      6
#Second     10   20     30

#In [9]: df2=pandas.DataFrame([{"Name":"John", "Surname":"Simpson"},{"Name":"Jack"}])

#In [10]: df2
#Out[10]: 
#   Name  Surname
#0  John  Simpson
#1  Jack      NaN - because we didn't specify surname value for Jack, but we can update it

#In [11]: type(df1)
#Out[11]: pandas.core.frame.DataFrame

#dir(df1) shows available methods to work with this frame, lets use 'mean'

#In [13]: df1.mean()
#Out[13]: 
#Price     6.0
#Age      12.0
#Value    18.0
#dtype: float64

#In [14]: df1.mean().mean()
#Out[14]: 12.0

#In [15]: type(df1.mean())
#Out[15]: pandas.core.series.Series

#In [16]: df1.Price
#Out[16]: 
#First      2
#Second    10
#Name: Price, dtype: int64

#In [17]: df1.Price.mean()
#Out[17]: 6.0

#In [18]: df1.Price.max()
#Out[18]: 10