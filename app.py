import pandas as pd
import pymysql.cursors
import time
import configparser

config = configparser.ConfigParser()
config.read('.config.ini')

host = config['DB']['host']
user = config['DB']['user']
password = config['DB']['password']
db = config['DB']['db']

def getDataFromMeteoSuisse():
	data = pd.read_csv('http://data.geo.admin.ch/ch.meteoschweiz.swissmetnet/VQHA69.csv',
                   sep = '|',
                   header = 1)

	data.head()
	data = data.loc[data.stn == 'WAE',:]

	connection = pymysql.connect(host = host, user=user, passwd=password, db=db)
	query = ("CALL `writeWeatherLog`("+ "'" + "79cf6c22-dcc6-11e5-8e77-00113217113f" + "'"  + ","+ "'" 
	         + str(data.tre200s0.values[0]) + "'" + ","+ "'" 
	         + str(data.fu3010z0.values[0]) + "'" + ","+ "'"  
	         + str(data.rre150z0.values[0]) + "'"+ ","+ "'" 
	         + str(data.prestas0.values[0]) + "'" + ","+ "'" 
	         + str(data.ure200s0.values[0]) + "'" + ","+ "'" 
	         + str(data.stn.values[0]) + "'" +",'" 
	         + str(data.stn.values[0]) + "'" +",'" 
	         + str(data.sre000z0.values[0]) +  "'" + ")")

	with connection.cursor() as cursor:
	    cursor.execute(query)
	connection.commit()
	e_Log = cursor.fetchall()
	connection.close()

while True:
	print("Start downloading...")
	getDataFromMeteoSuisse()
	print("OK")
	time.sleep(3600)