# Ensemble Methods, Part 1: Bagging and Random Forests

Code and data for the article [Ensemble Methods, Part 1: Bagging and Random Forests](https://medium.com/@319257836/ensemble-methods-part-1-bagging-and-random-forests-d44cb6bd019c).

## Contents

- `bagging.ipynb` reproduces every number and chart in the article, in the same order.
- `plot_style.py` defines the colors, fonts and sizes shared by all the charts.
- `data/classification_1500.csv` is a synthetic dataset with 1,500 rows and 25 features, used for the model comparison and the OOB curves.
- `data/moons_train.csv` has 260 points of a two-class problem, used to train the models in the decision boundary comparison.
- `data/moons_test.csv` has 4,000 new points from the same distribution, used to evaluate them.
- `figures/` contains all the figures in the article.

## How to run it

```bash
pip install -r ../../requirements.txt
jupyter notebook bagging.ipynb
```

The notebook runs offline in a few minutes on a laptop and overwrites the charts in `figures/` with the same images.

## Figures

The notebook generates the five charts: `fig02_crowd_error`, `fig07_base_models`, `fig08_variance_band`, `fig10_boundaries` and `fig11_oob_curve`.

The other figures are diagrams and formulas drawn for the article. The data behind them, such as the bootstrap sample and the out-of-bag matrix, is printed in the notebook. The cover illustration (`fig01_hero.png`) was generated with AI.
