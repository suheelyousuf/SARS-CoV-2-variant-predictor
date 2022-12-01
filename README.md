# SARS-CoV-2-variant-predictor
## A machine learning model for the prediction of SARS-CoV-2 variants

Adaptive mutations in the severe acute respiratory syndrome coronavirus 2
(SARS-CoV-2) genome can change the virus&#39;s pathogenicity. Even a single amino
acid substitution can have a significant impact on a SARS-CoV-2&#39;s capacity to
escape the immune system and hinder the progress of vaccine development against
this virus. Identification of specific variant of SAR-Cov-2 is complicated and
computationally expensive task. In this study we developed a machine learning
model to efficiently differentiate among various SARS-Cov-2 variant genomes. To
scale up the performance of the model and to make the model computationally less
expensive we used k-mer pattern as the only feature for classification. In this study
we used next-generation sequencing data and six ML algorithms namely Naive
Bayes (NB), K-Nearest Neighbor (KNN), Support Vector Machine (SVM), Random
Forest (RF) and AdaBoost Classifiers to predict SARS-CoV-2 variants, the accuracy
of all the models is compared and finally we recommended AdaBoost classifier the
best model for the prediction of the SARS-CoV-2 variants. We expect our model will
help researchers efficiently predict SARS-CoV-2 variants from huge genome
datasets. Table 1 shows the relative comparison of different machine learning
algorithms.

| ML Algorithm       | Accuracy           | Precision  |  Recall  |  f1  |
| ------------- |:-------------:| -----:|:--------:|:----:|
| Naive Bayes      | 82% | 81% |  82%  | 80%  |
| K-NN      | 81% | 84% |  81%  | 80%  |
| SVM      | 81% | 84% |  81%  | 80%  |
| Random Forest      | 93% | 94% |  93%  | 93%  |
| AdaBoost      | 95% | 97% |  94%  | 95%  |

## Table 1
