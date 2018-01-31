import pandas #import pandas packages for data reader to fetch data from websites such as Yahoo finance
import pandas_datareader.data as web
from pandas_datareader import data, wb
import datetime

start= datetime.datetime(2015,7,28) #date and time function to import data for range of time (in this case, 52 weeks)
end = datetime.datetime(2016,7,28)

GIS = data.DataReader("GIS", "yahoo", start, end) #enter arguments and define variables for stock tickers, source of data, start and end date
BP = data.DataReader("BP", "yahoo", start, end) #encountered error here with the package being unable to access Yahoo site. Checked Stack Overflow extensively- likely an issue with moving to Python 3.6
JNJ= data.DataReader("JNJ", "yahoo", start, end)
VZ= data.DataReader("VZ", "yahoo", start, end)
HSY= data.DataReader("HSY", "yahoo", start, end)

stockpicks= data.DataFrame({"GIS": GIS["Close"], #enter types to create data frame
                      "BP": BP["Close"],
                      "JNJ": JNJ["Close"],
                      "VZ": VZ["Close"],
                      "HSY": HSY["Close"]})

corComp.rename(columns={'Close': 'GIS'}, inplace=True)