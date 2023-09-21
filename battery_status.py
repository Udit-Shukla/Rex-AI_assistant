import psutil
import datetime

battery_data=psutil.sensors_battery()
print('Battery power left : {}%'.format(battery_data.percent))
if battery_data.power_plugged:
    print('Power is connected')
else:
    print('Power is not connected')
    print('Time left on battery: {}'.format(datetime.timedelta(seconds=battery_data.secsleft)))    