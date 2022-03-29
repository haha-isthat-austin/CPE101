# Name:       Austin Ma                                                         
# Course:     CPE 101                                                           
# Instructor: Daniel Kauffman                                                   
# Assignment: Calcudoku                                                         
# Term:       Fall 2018                                                         
                                                                                 
                                                                                 
def main():                                                                     
   finish = 0                  
   o_well = []
   row = 0                                                                  
   col = 0                                                                            
   cages = []   
   puzzle = input()                                                              
   max_val = 5
   for i in puzzle:
      cages.append([i])
   grid = [[0] * max_val] * max_val         
   while finish != 1:
      grid[row][col] += 1   #this is currently out of range in index
      print(grid[row][col])    
      if grid[row][col] >= max_val:
         grid[row][col] = 0
         col -= 1
         if col not in grid[row] and row > 0:
            row -= 1
            col = max_val
      if col >= max_val: 
         col = 0                
         row += 1
      if validate_all(grid, cages) is True: 
         col += 1               
      if grid[-1][-1] > 0 and validate_all(grid, cages) is True:
         finish = 1
   for i in grid:
      print(", ".join(grid[i]))
                        
                        
def validate_all(grid, cages): 
   yee = True                                                 
   x = validate_rows(grid)
   y = validate_cols(grid)
   z = validate_cages(grid, cages) 
   return  x & y & z == yee


def grid_trans(grid):
   newlist = []
   for i in grid:
      for j in i:
         newlist.append(j)
   return newlist 
    
      
def validate_rows(grid):                                                        
   dups = []                                                                                                                                    
   for row in grid:
      for j in row:
         if row.count(j) > 1:
            return False
   return True

   
def validate_cols(grid):
   yee = True
   j = 0
   newlist = []
   superlist = []
   for i in grid:
      newlist.append(i[j])
   superlist.append(newlist)
   newlist = []
   j += 1
   return validate_rows(superlist) == yee
   
 
def validate_cages(grid, cages):  
   grid_1d = grid_trans(grid)
   check_sum = 0
   for i in cages[1:]:
      for j in i[2:]:
         check_sum += grid_1d[j]
      if check_sum <= i[0]:
         check_sum = 0
      else:
         return False
   return True

         
if __name__ == "__main__":                                                      
   main()    
