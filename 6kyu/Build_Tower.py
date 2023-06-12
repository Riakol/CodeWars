def tower_builder(n_floors):
   tower, x = [], 0
   for i in range(1, n_floors * 2, 2):
      tower.append(f"{' ' * ((n_floors - 1) - x)}{'*' * i}{' ' * ((n_floors - 1) - x)}")
      x += 1
   return tower


'''
https://www.codewars.com/kata/576757b1df89ecf5bd00073b
'''
