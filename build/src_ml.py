# -*- coding: utf-8 -*-
"""Machine Learning (KSE) — 6 modules; the syllabus lists topics as bullets,
so each bullet is a concept and the bullet text is the verbatim quote."""
REL = "source/Syllabus_Machine_Learning.pdf"; D = "machine-learning"
H = {1:"Supervised Learning",2:"Unsupervised Learning",3:"Deep Learning",
     4:"Regularization methods",5:"Ensemble learning",6:"Performance metrics"}
Q = {
 "clsreg":"Classification/Regression","knn":"KNN","linreg":"Linear Regression",
 "dtree":"Decision Tree","over":"Overfitting and train/validation splits","cv":"CV algorithm",
 "comp":"Data compression","curse":"The curse of dimensionality","pca":"PCA, t-SNE/UMAP (briefly)",
 "clust":"H-clustering, K-Means, DBSCAN;",
 "neuron":"Artificial neuron","ff":"Feed-forward, backprop, convolutional operation,","loop":"Training loop",
 "l12":"L2 and L1 regularisation","wd":"Weight decay, dropout","aug":"Data augmentation",
 "avg":"Basic averaging and majority vote","bag":"Bagging ensemble","rf":"Random forest",
 "boost":"Adaptive boosting, stacking, and blending;",
 "acc":"Accuracy, baselines","cm":"Confusion matrix, recall and precision","f1":"F1/Dice, ROC/AUC.",
 "hol":"Holistic view",
}
def c(slug, name, kind, diff, definition, aliases, quotes):
    return dict(slug=slug, name=name, kind=kind, difficulty=diff, domain=D,
                definition=definition, aliases=aliases,
                occurrences=[{"rel_path": REL, "role": r, "quote": q, "confidence": 0.9}
                             for r, q in quotes])

UNITS = {
 "ML-M1": (1, 1, "Module 1. Supervised Learning", [
   c("supervised-learning","Supervised Learning","definition",2,"Learning a mapping from inputs to known target values using labelled examples.",[],[("introduced",H[1])]),
   c("classification","Classification","method",2,"Supervised prediction of a discrete class label.",[],[("introduced",Q["clsreg"])]),
   c("regression","Regression","method",2,"Supervised prediction of a continuous numeric value.",[],[("introduced",Q["clsreg"])]),
   c("knn","K-Nearest Neighbours","method",2,"Predicting from the labels of the closest training examples, with no explicit training step.",["KNN"],[("introduced",Q["knn"])]),
   c("linear-regression","Linear Regression","method",2,"Fitting a linear function of the features by minimising squared error.",[],[("introduced",Q["linreg"])]),
   c("decision-tree","Decision Tree","method",2,"A predictor that splits the feature space by recursive threshold questions.",[],[("introduced",Q["dtree"])]),
   c("overfitting","Overfitting","principle",3,"Fitting noise in the training data so that performance on unseen data degrades.",[],[("introduced",Q["over"])]),
   c("train-validation-split","Train/Validation Split","method",2,"Holding out part of the data to estimate performance on examples not used for fitting.",["train/validation splits"],[("introduced",Q["over"])]),
   c("cross-validation","Cross-Validation","method",3,"Rotating the held-out fold over the data to get a more stable performance estimate.",["CV algorithm"],[("introduced",Q["cv"])]),
 ]),
 "ML-M2": (2, 1, "Module 2. Unsupervised Learning", [
   c("unsupervised-learning","Unsupervised Learning","definition",3,"Finding structure in data without target labels.",[],[("introduced",H[2])]),
   c("data-compression","Data Compression","method",3,"Representing data with fewer numbers while preserving what matters.",[],[("introduced",Q["comp"])]),
   c("curse-of-dimensionality","The Curse of Dimensionality","principle",4,"In high dimensions data becomes sparse and distances lose contrast, undermining methods that rely on proximity.",[],[("introduced",Q["curse"])]),
   c("pca","Principal Component Analysis","method",4,"Projecting data onto the directions of greatest variance, found from the eigenstructure of its covariance matrix.",["PCA"],[("introduced",Q["pca"])]),
   c("nonlinear-embedding","t-SNE / UMAP","method",4,"Non-linear dimensionality reduction aimed at preserving local neighbourhoods for visualisation.",["t-SNE","UMAP"],[("introduced",Q["pca"])]),
   c("hierarchical-clustering","Hierarchical Clustering","method",3,"Building a nested tree of clusters by repeatedly merging or splitting groups.",["H-clustering"],[("introduced",Q["clust"])]),
   c("k-means","K-Means","method",3,"Partitioning data into k clusters by alternately assigning points to nearest centroids and recomputing them.",[],[("introduced",Q["clust"])]),
   c("dbscan","DBSCAN","method",4,"Density-based clustering that finds arbitrarily shaped clusters and labels sparse points as noise.",[],[("introduced",Q["clust"])]),
 ]),
 "ML-M3": (3, 1, "Module 3. Deep Learning", [
   c("deep-learning","Deep Learning","definition",4,"Learning with many-layered networks that build their own representations of the input.",[],[("introduced",H[3])]),
   c("artificial-neuron","Artificial Neuron","definition",3,"A unit computing a weighted sum of inputs followed by a non-linear activation.",[],[("introduced",Q["neuron"])]),
   c("feedforward-network","Feed-Forward Network","framework",4,"A network of neuron layers passing signals in one direction from input to output.",["feed-forward"],[("introduced",Q["ff"])]),
   c("backpropagation","Backpropagation","method",4,"Computing the gradient of the loss with respect to every weight by applying the chain rule backwards through the layers.",["backprop"],[("introduced",Q["ff"])]),
   c("convolution-operation","Convolutional Operation","method",4,"Sliding a shared small filter across the input so that the same local pattern is detected anywhere.",["convolutional operation"],[("introduced",Q["ff"])]),
   c("training-loop","Training Loop","method",3,"The repeated cycle of forward pass, loss evaluation, gradient computation and weight update.",[],[("introduced",Q["loop"])]),
 ]),
 "ML-M4": (4, 1, "Module 4. Regularization", [
   c("regularization","Regularization","principle",4,"Deliberately constraining a model to reduce overfitting at the cost of some training fit.",["regularisation"],[("introduced",H[4])]),
   c("l2-regularization","L2 Regularization","method",4,"Penalising the sum of squared weights, shrinking them smoothly toward zero.",[],[("introduced",Q["l12"])]),
   c("l1-regularization","L1 Regularization","method",4,"Penalising the sum of absolute weights, which drives some exactly to zero and selects features.",[],[("introduced",Q["l12"])]),
   c("weight-decay","Weight Decay","method",4,"Shrinking weights at every update step, the optimisation-side view of L2 penalty.",[],[("introduced",Q["wd"])]),
   c("dropout","Dropout","method",3,"Randomly disabling units during training so the network cannot rely on any single path.",[],[("introduced",Q["wd"])]),
   c("data-augmentation","Data Augmentation","method",3,"Enlarging the training set with label-preserving transformations of existing examples.",[],[("introduced",Q["aug"])]),
 ]),
 "ML-M5": (5, 1, "Module 5. Ensemble learning", [
   c("ensemble-learning","Ensemble Learning","framework",4,"Combining several models so their errors partly cancel and the whole beats any part.",[],[("introduced",H[5])]),
   c("averaging-and-voting","Averaging and Majority Vote","method",3,"The simplest combination rules: average the predicted numbers, or take the most frequent predicted class.",["basic averaging and majority vote"],[("introduced",Q["avg"])]),
   c("bagging","Bagging","method",4,"Training each member on a bootstrap resample to decorrelate their errors and cut variance.",["bagging ensemble"],[("introduced",Q["bag"])]),
   c("random-forest","Random Forest","method",4,"Bagged decision trees with additional random feature subsampling at each split.",[],[("introduced",Q["rf"])]),
   c("boosting","Adaptive Boosting","method",5,"Fitting members in sequence, each concentrating on the examples its predecessors got wrong.",["AdaBoost","adaptive boosting"],[("introduced",Q["boost"])]),
   c("stacking","Stacking and Blending","method",5,"Training a further model to combine the predictions of the base models.",["blending"],[("introduced",Q["boost"])]),
 ]),
 "ML-M6": (6, 1, "Module 6. Performance metrics", [
   c("accuracy","Accuracy","metric",2,"The share of predictions that are correct; misleading when classes are imbalanced.",[],[("introduced",Q["acc"])]),
   c("baseline","Baseline","principle",2,"The trivial predictor any real model must beat before its score means anything.",["baselines"],[("introduced",Q["acc"])]),
   c("confusion-matrix","Confusion Matrix","tool",2,"The table of predicted against actual classes, from which most classification metrics are derived.",[],[("introduced",Q["cm"])]),
   c("recall","Recall","metric",3,"The share of truly positive cases the model retrieves.",["sensitivity"],[("introduced",Q["cm"])]),
   c("precision","Precision","metric",3,"The share of predicted positives that are actually positive.",[],[("introduced",Q["cm"])]),
   c("f1-score","F1 / Dice Score","metric",3,"The harmonic mean of precision and recall, a single number balancing the two.",["F1","Dice"],[("introduced",Q["f1"])]),
   c("roc-auc","ROC / AUC","metric",4,"The curve of true against false positive rates over all thresholds, and the area beneath it.",["ROC","AUC"],[("introduced",Q["f1"])]),
   c("holistic-evaluation","Holistic View of Evaluation","principle",4,"Judging a model by the whole picture of metrics, baselines and error structure rather than one score.",["holistic view"],[("introduced",Q["hol"])]),
 ]),
}
