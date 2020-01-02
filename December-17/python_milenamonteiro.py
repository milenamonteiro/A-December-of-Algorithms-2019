def fastest_path(line1, line2, start, end):
    path = []
    start_index = 0
    end_index = 0
    intersection = list(set(line1).intersection(set(line2)))
    intersection = "".join(a for a in intersection) # converts to string
    intersection_index_line1 = line1.index(intersection)
    intersection_index_line2 = line2.index(intersection)
    
    if start in line1 and end in line1:
        start_index = line1.index(start)
        end_index = line1.index(end)
        path = line1[start_index:end_index+1]
        
    elif start in line2 and end in line2:
        start_index = line2.index(start)
        end_index = line2.index(end)
        path = line2[start_index:end_index+1]
        
    elif start in line1 and end in line2:
        start_index = line1.index(start)
        end_index = line2.index(end)
        
        if intersection_index_line1 > start_index:
            path += line1[start_index:intersection_index_line1]
        else:
            path += line1[intersection_index_line1 - 1:start_index - 1][::-1]
            
        if intersection_index_line2 > end_index:
            path += line2[end_index:intersection_index_line2 + 1][::-1]
        else:
            path += line2[intersection_index_line2 - end_index + 1:end_index + 1]
        
    else:
        start_index = line2.index(start)
        end_index = line1.index(end)
        if intersection_index_line2 > start_index:
            path += line2[start_index:intersection_index_line2 + 1]
        else:
            path += line2[intersection_index_line2 - start_index + 1:start_index + 1][::-1]
        
        if intersection_index_line1 > end_index:
            path += line1[end_index:intersection_index_line1][::-1]
        else:
            path += line1[intersection_index_line1 + 1:end_index + 1]
            
    print(" -> ".join(a for a in path))

fastest_path(
    ['Park', 'Central', 'Beach', 'Mylapore', 'Kilpauk'],
    ['Central', 'T.Nagar', 'Washerampet', 'MKB Nagar'],
    'Park',
    'T.Nagar')
