

def range_extraction(args):
    flag = False
    first = None
    res = ''

    for i in range(len(args) - 1):
        if args[i] == args[i + 1] - 1 and not flag:  
            flag = True
            first = args[i]
        elif args[i] == args[i + 1] - 1:  
            continue
        else:  # Fin de una secuencia o número individual
            if flag and first is not None and args[i] - first >= 2:
                res += str(first) + '-' + str(args[i]) + ','
            elif flag and first is not None:  
                res += str(first) + ',' + str(args[i]) + ','
            else:
                res += str(args[i]) + ','

            flag = False
            first = None

    
    if flag and first is not None and args[-1] - first >= 2:
        res += str(first) + '-' + str(args[-1]) + ','
    elif flag and first is not None:  
        res += str(first) + ',' + str(args[-1]) + ','
    else:
        res += str(args[-1]) + ','

    return res.rstrip(',')  