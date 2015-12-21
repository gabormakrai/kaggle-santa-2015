from gifts import loadGifts
from graph import createEdges, gisEdges, saveDownEdges, findClosestGifts,\
    loadEdges, mst, keepOnlyCaseStudyEdges

dataDirectory = "c:\\data\\kaggle-santa-2015\\"

#load gifts
gifts = loadGifts(dataDirectory + "gifts.csv")

#edges = createEdges(gifts)

#gisEdges(edges, gifts, dataDirectory + "graph_edges.csv")

#saveDownEdges(edges, gifts, dataDirectory + "graph1.csv")

edges = loadEdges(gifts, dataDirectory + "graph1.csv")
# 
# edges2 = keepOnlyCaseStudyEdges(edges)
# gisEdges(edges2, gifts, dataDirectory + "graph_edges2.csv")
# saveDownEdges(edges2, gifts, dataDirectory + "graph2.csv")
# 
mstEdges = mst(edges, gifts)
# 
# mstEdges2 = keepOnlyCaseStudyEdges(mstEdges)
# gisEdges(mstEdges2, gifts, dataDirectory + "mst_edges2.csv")
# 
gisEdges(mstEdges, gifts, dataDirectory + "graph1_mst_edges.csv")
saveDownEdges(mstEdges, gifts, dataDirectory + "graph1_mst.csv")

# edges = loadEdges(gifts, dataDirectory + "graph2.csv")
# gisEdges(edges, gifts, dataDirectory + "graph2_edges.csv")
# 
# mstEdges = mst(edges, gifts)
# 
# gisEdges(mstEdges, gifts, dataDirectory + "graph2_mst.csv")

