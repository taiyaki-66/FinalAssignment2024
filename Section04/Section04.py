import datetime

timeNow = datetime.datetime.now()

fileName = timeNow.strftime('%Y%m%d_%H%M%f')[:-3] + '.log'

# path = '/Section04/log/'

logFile = open('Section04\log\%s' %(fileName), 'w')
logFile.write('[%s]\t%s' %(timeNow.strftime('%Y%m%d_%H:%M:%S.%f')[:-3], 'execute!'))