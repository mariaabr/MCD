# CLUSTER ANALYSIS
iris
str(iris) # str means structure

# Distance matrix
?dist
dist(iris[1:5,1:4]) # only lines 1 to 5 and 4 columns
d = dist(iris[,1:4]) # all lines
?hclust # cluster hierarquico
hc = hclust(d) # complete
plot(hc, labels=iris$Species, hang=-1) # plot the cluster dendrogram + label identifica por tipo de especie + hang os forks alinham-se
hc$merge # the first line represents the most similar flowers/individs
hc$height # distances betwen th different individs
plot(hc, labels=iris$Specie)
rect.hclust(hc, k=2) # divide the cluster dendrogram in two partsxi

d = dist(iris[,1:4])
hc = hclust(d, method="centroid")
plot(hc, hang = -1)

?cophenetic # computes the cophenetic distance for a hierarchical clustering
cophenetic(hc)

# k-means
k = kmeans(iris[,1:4], centers = 3) # number 3 is the number of centers

# Results:
# K-means clustering with 3 clusters of sizes 50, 62, 38

# Cluster means:
#   Sepal.Length Sepal.Width Petal.Length Petal.Width ->> means of each variable in every center
# 1     5.006000    3.428000     1.462000    0.246000
# 2     5.901613    2.748387     4.393548    1.433871
# 3     6.850000    3.073684     5.742105    2.071053
# 
# Clustering vector: ->> where are the values centered, near each center
#   [1] 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# [46] 1 1 1 1 1 2 2 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 2 2 2 2 2 2 2 2 2 2 2 2
# [91] 2 2 2 2 2 2 2 2 2 2 3 2 3 3 3 3 2 3 3 3 3 3 3 2 2 3 3 3 3 2 3 2 3 2 3 3 2 2 3 3 3 3 3 2 3
# [136] 3 3 3 2 3 3 3 2 3 3 3 2 3 3 2
# 
# Within cluster sum of squares by cluster:
#   [1] 15.15100 39.82097 23.87947
# (between_SS / total_SS =  88.4 %)
# 
# Available components:
#   
#   [1] "cluster"      "centers"      "totss"        "withinss"     "tot.withinss" "betweenss"   
# [7] "size"         "iter"         "ifault"

str(k)
cutree(hc, k=2) # divide into two groups >> nao deu o resultado correto
