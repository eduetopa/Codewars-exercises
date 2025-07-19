def rule30(list_, n):
    
    #Rule 30 combinations
    rule = {
        "000": 0,
        "001": 1,
        "010": 1,
        "011": 1,
        "100": 1,
        "101": 0,
        "110": 0,
        "111": 0,
    }
    
    
    result = list_
    cell = ""
    
    # Only 0s array, just multiply the size
    if 1 not in result:
        result += [0] * n * 2
        return result
    
    
    for _ in range(n):
        # Need extra 0s to process
        # 
        aux = [0] + result + [0]
        result = [1] 
        
        for i in range(0, len(aux) - 2):
            # Gather by 3 the elements of the array to have the combination key in cell
            for j in range(3):
                cell += str(aux[i + j])
            
            result.append(rule[cell])
            cell = ""
            
        result.append(1)
                    
    return result