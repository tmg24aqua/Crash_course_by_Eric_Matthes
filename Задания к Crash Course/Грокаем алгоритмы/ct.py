def countdown(i) :
    print(i)
    countdown(i-1)
    if i <= 1:
        return
    else :
        countdown(i-1)