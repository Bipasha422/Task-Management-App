def play(status):
    match status:
        case 200:
            return"ok"
        case 400:
            return "better"
        case 600:
            return "best"
print(play(600))