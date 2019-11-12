from hw6 import MST_Kruskel, MST_Prim

G = ([(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
# MST_Kruskel(dense_tuples1)[0] == 4995
print(MST_Kruskel(G))
print(MST_Prim(G))



dense_tuples1 = generate_seq(1000, 500000, 1)
dense_tuples2 = generate_seq(1500, 150000, 1)
tuples_1 = generate_seq(1500, 5000, 1)
tuples_2 = generate_seq(1000, 20000, 4)