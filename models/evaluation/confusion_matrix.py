# confusion_matrix.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

class ConfusionMatrixEvaluator:
    def __init__(self, model):
        self.model = model

    def evaluate(self, df, text_col="text", label_col="label", normalize=None):
        """
        Runs predictions and computes confusion matrix
        """

        X = df[text_col]
        y_true = df[label_col]

        y_pred = self.model.predict(X)

        labels = np.unique(y_true)

        cm = confusion_matrix(y_true, y_pred, labels=labels, normalize=normalize)

        return cm, labels, y_true, y_pred

    def plot(self, cm, labels, title="Confusion Matrix"):
        fig, ax = plt.subplots(figsize=(10, 8))

        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm,
            display_labels=labels
        )

        disp.plot(
            cmap="Blues",
            xticks_rotation=45,
            ax=ax,
            values_format=".2f" if cm.dtype != int else "d"
        )

        plt.title(title)
        plt.tight_layout()
        plt.show()

    def save_plot(self, cm, labels, path):
        fig, ax = plt.subplots(figsize=(10, 8))

        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm,
            display_labels=labels
        )

        disp.plot(
            cmap="Blues",
            xticks_rotation=45,
            ax=ax
        )

        plt.title("Confusion Matrix")
        plt.tight_layout()

        fig.savefig(path)
        plt.close()