def filter_logs(logs, key, value):
    #За всеки взет ред от логс търся дали има аргумент в речника с ключ Key и съответната му стойност
    return list(filter(lambda log: log[key] == value, logs))


def top(logs, key, count):
    tmp = {}

    #Запълвам речника си с values на ключовата дума, ако се повтори някое value увеличавам стойността на tmp с едно
    for log in logs:
        if log[key] in tmp:
            tmp[log[key]] += 1
        else:
            tmp[log[key]] = 1

    #Сортирам елементите на tmp във възходящ ред по стойност(value) също искам резултата ми да е лист, за да мога да попвам елементите след това
    my_list = sorted(tmp.items(), key=lambda x: x[1])

    #След като имам елементи подредени във възходящ ред последния ще е най-срещания
    result = [my_list.pop() for i in range(count) if len(my_list) > 0]

    return dict(result)


def complex_filter(logs, filter_params):
    result = list()
    #За всеки лог от логс проверявам дали filter_params е подмножество на лог
    for log in logs:
        if filter_params.items() <= log.items():
            result.append(log)
    return result

