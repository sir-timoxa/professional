def sourcetemplate(url):
    def f(**kwargs):
        if kwargs:
            result = "&".join(f"{k}={v}" for k, v in sorted(kwargs.items()))
            return f"{url}?{result}"
        else:
            return f"{url}"

    return f

url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))