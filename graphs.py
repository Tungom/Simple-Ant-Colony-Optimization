#-------------------------------------------------------------
# Chia E Tungom (chemago99@yahoo.com)
#
# graphs for double bridge experiment 
# graph1 from Marco Dorigo's book Ant colony optimization
# graph2 from the book computational intelligene by Engelbreth
#--------------------------------------------------------------

# Exteded double bridge experiment from Marco Dorigo ACO Book 
# Shortest path is [ 0,  9, 10, 12, 13,  8] or [ 0,  9, 14, 17, 13,  8]

graph1 = [[0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
          [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0],
          [0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0],
          [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1],
          [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0]]

# Shortest path is [ 0,  3,  4]

graph2 = [[0,0,0,1,0,1,0],
          [0,0,1,1,0,0,0],
          [0,1,0,1,1,0,0],
          [1,1,1,0,1,1,0],
          [0,0,1,1,0,0,1],
          [1,0,0,1,0,0,1],
          [0,0,0,0,1,1,0]]