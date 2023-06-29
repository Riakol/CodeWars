def dirReduc(arr):
    sides = {"NORTH": "SOUTH",
             "SOUTH": "NORTH",
             "EAST": "WEST",
             "WEST": "EAST"}

    for x in range(1, len(arr)):
        if sides[arr[x]] == arr[x-1]:
            del arr[x-1:x+1]
            return dirReduc(arr)
    return arr