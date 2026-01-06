import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

class AnomalyDetectionEvaluator:
    """Evaluates ML model performance for Anomaly Detection tasks."""
    
    def __init__(self, n_samples=1000):
        self.X, self.y = make_classification(
            n_samples=n_samples, n_features=20, n_informative=15, 
            n_classes=2, random_state=42
        )
        self.model = RandomForestClassifier(random_state=42)

    def run_evaluation(self):
        """Trains model and computes ROC/AUC metrics."""
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.3, random_state=42
        )
        
        self.model.fit(X_train, y_train)
        y_prob = self.model.predict_proba(X_test)[:, 1]
        
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        roc_auc = auc(fpr, tpr)
        return fpr, tpr, roc_auc

    def plot_roc_curve(self, fpr, tpr, roc_auc):
        """Visualizes the ROC Curve for research documentation."""
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, color='#1A73E8', lw=2, label=f"ROC Curve (AUC = {roc_auc:.3f})")
        plt.plot([0, 1], [0, 1], color='#BDC1C6', linestyle='--', lw=1, label="Baseline")
        
        plt.xlabel("False Positive Rate (FPR)")
        plt.ylabel("True Positive Rate (TPR)")
        plt.title("Model Discrimination Power: Anomaly Detection Performance", fontsize=12)
        plt.legend(loc="lower right")
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    evaluator = AnomalyDetectionEvaluator()
    f, t, a = evaluator.run_evaluation()
    evaluator.plot_roc_curve(f, t, a)
