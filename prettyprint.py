def prettyprint(list, args):
    for i in range(len(list)):
        for j in args:
            print(f"{j}: {list[i][j]}")
        print("###################")