Cats vs Dogs Classification: HOG + PCA + SVM

A traditional machine learning pipeline that classifies images of cats and dogs using:
- HOG features for edge/shape extraction
- PCA to reduce dimensionality
- Linear SVM for classification
- Optimizations: sampling subset (10%), smaller images (64×64), joblib parallelism

🎯 Performance

| Metric | Value |
|--------|-------|
| Dataset size | 2500 images |
| HOG dims → post-PCA | 1176 → 200 components |
| Accuracy | **68.8%** |
| Precision / Recall | Cats: 0.69 / 0.71 • Dogs: 0.68 / 0.67 |

🔍 How This Compares
- HOG + SVM pipelines typically achieve **60–75%** accuracy :contentReference[oaicite:14]{index=14}.
- On Asirra, classical SVM approaches reached **~83–87% with richer feature sets** :contentReference[oaicite:15]{index=15}.

🚀 Next Steps
- Train on the full dataset (~25k images) to boost accuracy.
- Experiment with enhanced features (e.g., HOG + LBP fusion) to reach ~85% :contentReference[oaicite:16]{index=16}.
- Optionally explore non-linear SVM kernels or simple CNN models to surpass 90%.


