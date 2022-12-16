
def app():
    data="hello word"
    data=data.encode("utf-8")
    f"200 okk",[
        ("Content-Type","text/plain"),
        ("Content-Length",str(len(data))),
        print(data)
    ]
    
    return iter([data])
app()