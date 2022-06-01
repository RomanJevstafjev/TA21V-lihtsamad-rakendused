from yaweather import Estonia, YaWeather

y = YaWeather(api_key="8fd3caf0-692e-4c4d-af8a-3d366770e356")
res = y.forecast(Estonia.Tallinn)

with open("5_task_logs.txt", "a") as file:
    file.write(str(res.fact.temp) + "\n")