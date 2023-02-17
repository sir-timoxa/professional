from datetime import datetime, timedelta

pattern = '%H:%M'
start = datetime.strptime(input(), pattern)
end = datetime.strptime(input(), pattern)

start_lesson = start
while start_lesson <= end and (start_lesson+timedelta(minutes=45))<= end:
    end_lesson = start_lesson+timedelta(minutes=45)
    print(f'{start_lesson.strftime(pattern)} - {end_lesson.strftime(pattern)}')
    start_lesson=end_lesson+timedelta(minutes=10)
