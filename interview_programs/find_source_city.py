def find_source_city(paths):
    dest = []
    for i in range(len(paths)):
        dest.append(paths[i][1])
    for i in range(len(paths)):
        source = paths[i][0]
        found = False
        for j in range(len(dest)):
            if source == dest[j]:
                found = True
                break
        if not found:
            return source
print(find_source_city([["A","Z"]]))