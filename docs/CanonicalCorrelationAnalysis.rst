Canonical Correlation Analysis
===========================

Introduction
------------
The CanonicalCorrelationAnalysis (CCA) class implements a fundamental multivariate statistical method that explores the relationships between two sets of variables. CCA finds linear combinations of variables in one set that are maximally correlated with linear combinations of variables in another set. This technique is particularly valuable when analyzing complex, multi-dimensional relationships between two sets of measurements.

Description
-----------
CCA identifies and quantifies the associations between two sets of variables by finding canonical variates - linear combinations of the original variables that maximize the correlation between the two sets. The method successively finds these pairs of canonical variates, with each pair being uncorrelated with all previous pairs.

Mathematical Formulation
-----------------------
For two sets of variables X ∈ ℝ^(n×p) and Y ∈ ℝ^(n×q), CCA finds vectors a and b that solve:

.. math::

   \max_{a,b} \rho = \frac{a^T \Sigma_{xy} b}{\sqrt{(a^T \Sigma_{xx} a)(b^T \Sigma_{yy} b)}}

subject to:
   a^T \Sigma_{xx} a = 1
   b^T \Sigma_{yy} b = 1

where:
- Σ_{xx} is the covariance matrix of X
- Σ_{yy} is the covariance matrix of Y
- Σ_{xy} is the cross-covariance matrix between X and Y
- a and b are the canonical coefficients
- ρ is the canonical correlation

The solution involves solving the eigenvalue problems:

.. math::

   \Sigma_{xx}^{-1}\Sigma_{xy}\Sigma_{yy}^{-1}\Sigma_{yx}a = \lambda^2a
   \Sigma_{yy}^{-1}\Sigma_{yx}\Sigma_{xx}^{-1}\Sigma_{xy}b = \lambda^2b

Properties
---------
1. Invariance to linear transformations
2. Ordered canonical correlations: ρ₁ ≥ ρ₂ ≥ ... ≥ ρᵣ ≥ 0
3. Orthogonality of canonical variates
4. Maximum number of correlations: r = min(p,q)

Implementation Features
---------------------
The class provides:
1. Automatic handling of standardization
2. Regularization options for ill-conditioned matrices
3. Statistical significance testing
4. Cross-validation procedures
5. Visualization tools for canonical variates

Academic References
-----------------
1. Hotelling, H. (1936). Relations Between Two Sets of Variates. Biometrika, 28(3/4), 321-377.

2. Anderson, T. W. (2003). An Introduction to Multivariate Statistical Analysis (3rd ed.). Wiley Series in Probability and Statistics.

3. González, I., Déjean, S., Martin, P. G., & Baccini, A. (2008). CCA: An R package to extend canonical correlation analysis. Journal of Statistical Software, 23(12), 1-14.

4. Hardoon, D. R., Szedmak, S., & Shawe-Taylor, J. (2004). Canonical correlation analysis: An overview with application to learning methods. Neural computation, 16(12), 2639-2664.

Applications
-----------
CCA is particularly useful in:
- Bioinformatics (gene expression analysis)
- Neuroimaging (brain-behavior relationships)
- Psychometrics (ability-achievement relationships)
- Environmental science (species-environment relationships)
- Financial analysis (market relationships)
- Signal processing (feature fusion)

Conclusion
----------
The CanonicalCorrelationAnalysis class provides a comprehensive implementation of CCA within the distancia package. Its robust implementation, coupled with various analytical and visualization tools, makes it an invaluable tool for exploring and quantifying relationships between multiple sets of variables. The implementation balances computational efficiency with numerical stability, making it suitable for both small-scale analyses and large-dimensional problems.

Usage Notes
----------
- Input data should be preprocessed to handle missing values
- Variables should be scaled appropriately
- The number of observations should exceed the number of variables in both sets
- Regularization parameters may need tuning for high-dimensional data
