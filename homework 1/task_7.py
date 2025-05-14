time_seconds = int(input("Please enter time in seconds: "))
minutes = time_seconds // 60
time_seconds %= 60
seconds = time_seconds
print("Your time in minutes: ", minutes, "minutes", seconds, "seconds")
