

def dict_take(a):
    try:
        print(a["Italy"])
    except KeyError:
        print("This key is missing")
    finally:
     print("Operation completed")
value = {
            "Ukraine": "Kyiv",
            "France": "Paris",
            "Germany": "Berlin",
        }

dict_take(value)