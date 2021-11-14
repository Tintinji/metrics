#!/usr/bin/env python
# coding: utf-8

# # This is the game with Econometrics
# 
# I studied ECON5106(Advanced Applied Econometrics) in UiO, fall 2021.Here are some notes and ideas from the lectures and readings
# 
# The materials are heavily based on the course delivered by Zhiyang,Jia, from Statistics Norway.
# 
# ## Here is a list of the content in this book.
# 
# ### Maximum Likelihood
# 
# -   Underlying principle of ML(discrete case without a Likelihood function)
# -   Construct a likelihood function, derive the ML estimator
# -   Find out the distribution of the estimator
# -   Delta method(idea and applications)
# -   3 tests application(Wald,LM,LR)
# 
# ### Generalized Moment Methods(GMM)
# 
# -   Underlying principle of MM and GMM
# -   Analysis the notion of under-, exact, and over-identification
# -   Analysis the role of the weight matrix
# -   Analysis the notion of efcient GMM, and how this is obtained
# -   Analysis the Wald and Hansen J-test
# -   Be able to determine the functions g(), g_N(), and estimator“$\beta_{GMM}$”for specific models, such as the linear regression model.
# -   Explain the relationship between i) GMM and 2SLS, and ii) GMM and MLE.

# <img src="https://www.abbreviations.com/images/1731506_GMM.png" alt="">

# I found this [**Funny CAT**](https://datascienceparichay.com/article/insert-image-in-a-jupyter-notebook/) when reviewing the markdown syntax.
# 
# <img src="https://i0.wp.com/datascienceparichay.com/wp-content/uploads/2021/03/no_regrets_cat.jpg" width=300 height=300 />

# ### Non-parametric Methods
# 
# -   Tell the difference between a **parametric**,**semi-parametric** and **nonparametric** model.
# -   The curse of dimensionality
# -   Histogram & Kernel density estimators
# -   Local constant, local linear regression
# -   Partial linear regression model
# -   The principles of bandwidth selection & **Bias-Variance** trade-off

# ### Bootstrapping Methods
# 
# -   Give an account for the principle of bootstrapping method.
# -   Understand and can construct the bootstrap variance and confidence interval.
# -   Understand and can perform hypothesis testing using bootstrap method.
# -   Explain the notion of bias correction.
# -   Understand the diferent bootstrap procedures for regression models.
# -   Basic grasp of the limitations of the bootstrap method.

# ### Unconfoundedness
# 
# -   (Non-parametric) regression approaches to treatment effect estimation that rely on selection on observables
# -   **Matching** as a weighting estimator
# -   Role of **common support** and extrapolation
# -   Balancing property of the propensity score
# -   Relation between matching and OLS

# <figure>
# <img src="matching.jpeg" alt="" width=100 height=100 />
# <figcaption align = "center"><b>This is perfect illustration of matching...</b></figcaption>
# </figure>

# ### Partial Identification

# ### Local Average Treatment Effects(LATE)

# ### Selection Models

# ### Marginal Treatment Effects(MTE)

# ### DID and Event studies

# ### Machine Learning Topics
