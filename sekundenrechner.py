
second=int(0)
minute=int(0)
hour=int(0)

def show_time():
    sec = int(input("Bitte Sekunden eingeben: "))
    hour=int(sec/3600)
    sec=int(sec-(hour*3600))
    minute=int(sec/60)
    sec=int(sec-(minute*60))
    second=sec
    print("Stunden: " + str(hour))
    print("Minuten: " + str(minute))
    print("Sekunden: " + str(second))
    
show_time()