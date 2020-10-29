def filter_logs(logs, key, value):

    return list(filter(lambda log: log[key] == value, logs))


def top(logs, key, count):
    result = for i in (map(lambda log: {log[i]: 0 for i in log if i == key}, logs))
    return result


def complex_filter(logs, filter_params):
    # Имплементация
    ...


logs = [
    {"timestamp": "2020-05-11T13:42:50", "status": "error", "countryISO2": "BG"},
    {"timestamp": "2020-05-11T13:43:20", "status": "success", "countryISO2": "UK"},
    {"timestamp": "2020-05-11T13:44:30", "status": "success", "countryISO2": "NZ"},
]
print(filter_logs(logs, "status", "success"))
print(top(logs, "status", 1))

