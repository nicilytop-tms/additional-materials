start = 'Start'
end = 'End'
planed_count_of_holes = 2


def drill(count_of_holes):
    made_one_hole = 'We made one hole!'
    result = 0
    
    for i in range(count_of_holes):
        print(made_one_hole)
        result += 1
    return result


print(start)
drill_result = drill(planed_count_of_holes)
print(f'As a result {drill_result} holes!')
print(end)

