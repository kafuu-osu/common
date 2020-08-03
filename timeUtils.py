import time, datetime

# get now timeString or timeStamp
def getTime(needFormat=0, formatMS=True):
    if needFormat != 0:
        return datetime.datetime.now().strftime(f'%Y-%m-%d %H:%M:%S{r".%f" if formatMS else ""}')
    else:
        return time.time()


# timeString to timeStamp
def toTimeStamp(timeString):
    if '.' not in timeString: getMS=False
    else: getMS=True
    timeTuple = datetime.datetime.strptime(timeString, f'%Y-%m-%d %H:%M:%S{r".%f" if getMS else ""}')
    return float(f'{str(int(time.mktime(timeTuple.timetuple())))}'+(f'.{timeTuple.microsecond}' if getMS else ''))


# timeStamp to timeString
def toTimeString(timeStamp):
    if type(timeStamp) == int: getMS=False
    else: getMS=True
    timeTuple = datetime.datetime.utcfromtimestamp(timeStamp+8*3600)
    return timeTuple.strftime(f'%Y-%m-%d %H:%M:%S{r".%f" if getMS else ""}')