def find_start_time(s,t):
    sh,sm = map(int,s.split(":"))
    th,tm = map(int,t.split(":"))
    sm -= tm
    if sm < 0:
        sm += 60
        sh -= 1
    sh -= th
    if sh < 0:
        sh += 24
    print(f"{sh:02d}:{sm:02d}")
find_start_time("06:30","06:20")