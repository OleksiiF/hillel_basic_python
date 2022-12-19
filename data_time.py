import time
import datetime


# print(time.time())
# print(time.time_ns())
# print(time.timezone)
#
#
# print("Start")
# time.sleep(3)
# print("End")
#
# print(
#     f"{time.ctime(0)=},\n"
#     f"{time.ctime(100)=},\n"
#     f"{time.ctime()=},\n"
# )
# #########################################################
# current_datetime = datetime.datetime.now()
# print(
#     f"{current_datetime=}, {type(current_datetime)=}\n"
#     f"{current_datetime.ctime()=},\n"
#     f"{current_datetime.timestamp()=},\n"  # equal to time.time()
#     f"{current_datetime.date()=},\n"
#     f"{current_datetime.year=},\n"
#     f"{current_datetime.month=},\n"
#     f"{current_datetime.weekday()=},\n"  # week starts from 0 (zero)
#     f"{current_datetime.isoweekday()=},\n"  # week starts from 1
#     f"{current_datetime.day=},\n"
#     f"{current_datetime.time()=},\n"
#     f"{current_datetime.hour=},\n"
#     f"{current_datetime.minute=},\n"
#     f"{current_datetime.second=},\n"
#     f"{current_datetime.microsecond=}"
# )
# #########################################################
# datetime_param = "31-12-2030 23:59"
# parsed_dt = datetime.datetime.strptime(datetime_param, "%d-%m-%Y %H:%M")
# print(f"{parsed_dt=}, {type(parsed_dt)=}")
# #########################################################
# current_datetime = datetime.datetime.now()
# time.sleep(3)
# time_difference = datetime.datetime.now() - current_datetime
#
# print(
#     f"{time_difference=}, {type(time_difference)=},\n"
#     f"{time_difference.microseconds=}, {type(time_difference.microseconds)=},\n"
#     f"{time_difference.days=}, {type(time_difference.days)=},\n"
#     f"{time_difference.seconds=}, {type(time_difference.seconds)=},\n"
#     f"{time_difference.total_seconds()=}, {type(time_difference.total_seconds())=}"
# )