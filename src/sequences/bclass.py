from shapely.geometry import Polygon

class MatchingBlocks:
  # These are the attributes needed to do the matching
  a_blocks_sizes = []
  b_blocks_sizes = []
  a_blocks_coordinates = []
  b_blocks_coordinates = []

  # Function to generate the list of polygons that we are gonna use
  def proportional_matching(self, matching_list, iterations): 
    polygon_list = []
    visited_group = [0] * len(self.a_blocks_sizes)
    cummulated_flag = False

    #This allows me to check something crucial, which blocks divide into which, both ways, much faster than checking the list of pairs.
    matching_assignations = [[] for x in range(len(self.a_blocks_sizes))] 
    inverse_matching_assignations = [[] for x in range(len(self.b_blocks_sizes))] 

    print(matching_assignations)
    print(inverse_matching_assignations)

    # Here I assign the values
    for a, b in matching_list: 
      matching_assignations[a].append(b)
      inverse_matching_assignations[b].append(a)
    
    # Now I go through the list again
    for i in range(len(matching_assignations)):
      if len(matching_assignations[i]) == 1: # If it is an agroupation
        print("This block is grouped")
        #Similar process, it's like dividing the B blocks into A blocks
        sum_of_blocks = 0
        for a_blocks in inverse_matching_assignations[matching_assignations[i][0]]:
          sum_of_blocks += self.a_blocks_sizes[a_blocks]
        ratio = (self.b_blocks_sizes[matching_assignations[i][0]]/sum_of_blocks)
        print("Ratio will be: ",ratio," pixels")

        accumulated = 0
        for j in inverse_matching_assignations[matching_assignations[i][0]]:
          # Take the part off.
          if visited_group[j] == 0:
            
            block_start = self.a_blocks_coordinates[j]

            counter = self.b_blocks_coordinates[matching_assignations[i][0]]

            last_pixel_end = block_start + accumulated
            last_pixel_right = 0
            while (last_pixel_right != self.a_blocks_coordinates[j] + self.a_blocks_sizes[j]): 
              last_pixel_right = last_pixel_end + ratio

              if last_pixel_right > self.a_blocks_coordinates[j] + self.a_blocks_sizes[j]:
                accumulated = last_pixel_right - (self.a_blocks_coordinates[j] + self.a_blocks_sizes[j])
                last_pixel_right = self.a_blocks_coordinates[j] + self.a_blocks_sizes[j]
                cummulated_flag = True

              polygon_list.append(Polygon([(last_pixel_end, 0),(last_pixel_right, 0),(counter, iterations),(counter + 1, iterations)])) # Tada
              if not cummulated_flag:
                counter += 1
              last_pixel_end = last_pixel_right
              cummulated_flag = False  
            visited_group[j] = 1
          
      else: # Otherwise it is a division. Easier case imo
        print("This block is divided")
        sum_of_blocks = 0
        for b_blocks in matching_assignations[i]:
          sum_of_blocks += self.b_blocks_sizes[b_blocks]
        ratio = (self.a_blocks_sizes[i]/sum_of_blocks)
        # Now let's form the parallelograms n-n
        inverse_ratio = (1/ratio) # Since doing the parallelograms through agroupation is way easier, we will do them with the inverse ratio, from B to A
        print("Ratio will be: ",inverse_ratio," pixels")
        accumulated = 0
        for j in matching_assignations[i]:
           # Since it is proportional, this is needed because don't want to affect the wrong pixels
          block_start = self.b_blocks_coordinates[j]

          counter = self.a_blocks_coordinates[i]

          last_pixel_end = block_start + accumulated
          last_pixel_right = 0
          while (last_pixel_right != self.b_blocks_coordinates[j] + self.b_blocks_sizes[j]): # x doesn't matter as a variable, we just want the operation to be executed for the number of pixels that exist.
            last_pixel_right = last_pixel_end + inverse_ratio

            if last_pixel_right > self.b_blocks_coordinates[j] + self.b_blocks_sizes[j]:
              accumulated = last_pixel_right - (self.b_blocks_coordinates[j] + self.b_blocks_sizes[j])
              last_pixel_right = self.b_blocks_coordinates[j] + self.b_blocks_sizes[j]
              cummulated_flag = True

            polygon_list.append(Polygon([(last_pixel_end, 0),(last_pixel_right, 0),(counter, iterations),(counter + 1, iterations)])) # Tada
            if not cummulated_flag:
              counter += 1
            last_pixel_end = last_pixel_right
            cummulated_flag = False
    
    return polygon_list