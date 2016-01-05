from gifts import loadGifts
from graph import createEdges, gisEdges, saveDownEdges, findClosestGifts,\
    loadEdges, mst, keepOnlyCaseStudyEdges, createGiftOrder, writeOutOrderGIS,\
    unifySubGraphs, writeOutOrder, addEdge
from submission import loadOrder, doSubmissionFromOrder,\
    createSubmissionFromTrips, calculateWRW
from path_opt import optimizeOrder

dataDirectory = "c:\\data\\kaggle-santa-2015\\"

#load gifts
gifts = loadGifts(dataDirectory + "gifts.csv")

# edges = createEdges(gifts)
# 
# #gisEdges(edges, gifts, dataDirectory + "graph_edges.csv")
# saveDownEdges(edges, gifts, dataDirectory + "graph1.csv")

# edges = loadEdges(gifts, dataDirectory + "graph1.csv")
# 
# edges2 = keepOnlyCaseStudyEdges(edges)
# gisEdges(edges2, gifts, dataDirectory + "graph_edges2.csv")
# saveDownEdges(edges2, gifts, dataDirectory + "graph2.csv")
# 
#mstEdges = mst(edges, gifts)
# 
# mstEdges2 = keepOnlyCaseStudyEdges(mstEdges)
# gisEdges(mstEdges2, gifts, dataDirectory + "mst_edges2.csv")
# 
#gisEdges(mstEdges, gifts, dataDirectory + "graph1_mst_edges.csv")
#saveDownEdges(mstEdges, gifts, dataDirectory + "graph1_mst.csv")

# edges = loadEdges(gifts, dataDirectory + "graph2.csv")
# gisEdges(edges, gifts, dataDirectory + "graph2_edges.csv")
# 
# mstEdges = mst(edges, gifts)
# 
# gisEdges(mstEdges, gifts, dataDirectory + "graph2_mst.csv")


# edges = loadEdges(gifts, dataDirectory + "graph1.csv")
# mstEdges = mst(edges, gifts)
# gisEdges(mstEdges, gifts, dataDirectory + "graph1_mst_edges.csv")
# saveDownEdges(mstEdges, gifts, dataDirectory + "graph1_mst.csv")


# mstEdges = loadEdges(gifts, dataDirectory + "graph1_mst.csv")
# addEdge(mstEdges, gifts, 39827, 21442)
# addEdge(mstEdges, gifts, 46399, 69322)
# print("#edges: " + str(len(mstEdges)))
# print("unify iter 1")
# mstEdges = unifySubGraphs(mstEdges, gifts)
# print("#edges: " + str(len(mstEdges)))
# print("unify iter 2")
# mstEdges = unifySubGraphs(mstEdges, gifts)
# print("#edges: " + str(len(mstEdges)))
# print("unify iter 3")
# mstEdges = unifySubGraphs(mstEdges, gifts)
# print("#edges: " + str(len(mstEdges)))
# print("unify iter 4")
# mstEdges = unifySubGraphs(mstEdges, gifts)
# print("#edges: " + str(len(mstEdges)))
# print("unify iter 5")
# mstEdges = unifySubGraphs(mstEdges, gifts)
# print("#edges: " + str(len(mstEdges)))
# print("unify iter 6")
# mstEdges = unifySubGraphs(mstEdges, gifts)
# gisEdges(mstEdges, gifts, dataDirectory + "graph1_mst_edges2.csv")
# order = createGiftOrder(mstEdges, gifts)
# writeOutOrderGIS(order, dataDirectory + "order1_path.csv", gifts)
#  
# writeOutOrder(order, dataDirectory + "order1.csv")

order = loadOrder(dataDirectory + "order1.csv")
trips = doSubmissionFromOrder(order, gifts)
print("of: " + str(calculateWRW(trips, gifts)))
optimizeOrder(gifts, order)
trips = doSubmissionFromOrder(order, gifts)
print("of: " + str(calculateWRW(trips, gifts)))

# createSubmissionFromTrips(trips, dataDirectory + "submission1.csv")

