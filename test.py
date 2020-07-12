from idates import IDates

if __name__ == '__main__':
    import time
    obj = IDates(date="2020-09-01", fmt="%Y-%m-%d")
    print(obj.to_timestamp())
    print(obj.to_string())
    print(obj.to_tz_string("utc"))

    obj = IDates(timestamp=1598889600)
    print(obj.to_timestamp())
    print(obj.to_string())
    print(obj.to_tz_string("utc"))
    obj1 = IDates(datetime=obj.days_jump(10))

    print(obj1.to_string())
