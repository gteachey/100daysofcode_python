def leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def bureas_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def teacher_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


for year in range(0, 100000000):
    if leap(year) != bureas_leap(year):
        print(f"Code returning different answers in year {year}")
    elif teacher_leap(year) != bureas_leap(year):
        print(f"Code returning different answers from teacher's code in year {year}")
    else:
        print("Nothing is happening!")
print("Finished checking code!")
