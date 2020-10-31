from itertools import chain
logs = [
    {"timestamp": "2020-05-11T13:42:50", "status": "error", "countryISO2": "BG"},
    {"timestamp": "2020-05-11T13:43:20", "status": "success", "countryISO2": "UK"},
    {"timestamp": "2020-05-11T13:44:30", "status": "success", "countryISO2": "NZ"},
]


search = {"status": "success", "countryISO2": "NZ"}
for log in logs:
    if search.items() <= log.items():
        print(log)



