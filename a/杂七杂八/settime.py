import datetime

def Main():
	today = datetime.datetime.today()
	year = str(today.year)
	month = str(today.month)
	day = str(today.day)
	hour = str(today.hour)
	minute = str(today.minute)
	second = str(today.second)
	microsecond = str(today.microsecond)

	set_time = "date -s \""+ year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second + "." + microsecond + "\""
	print(set_time)
	# xsh.Screen.Send(set_time)
	# xsh.Screen.Send("\r")



Main()