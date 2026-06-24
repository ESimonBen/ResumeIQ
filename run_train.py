# run_train.py
from models.pipeline import TrainingPipeline
from models.evaluation.confusion_matrix import ConfusionMatrixEvaluator
from config.paths import ARTIFACTS_DIR

def main():
    pipeline = TrainingPipeline()

    train_df, val_df = pipeline.load_data()

    pipeline.train(train_df)

    print("\nValidation Results:")
    pipeline.evaluate(val_df)

    evaluator = ConfusionMatrixEvaluator(pipeline.model)

    cm, labels, _, _ = evaluator.evaluate(val_df)

    evaluator.plot(cm, labels)

    evaluator.save_plot(cm, labels, ARTIFACTS_DIR / "confusion_matrix.png")

    pipeline.save()

    print("\nModel saved successfully")

if __name__ == "__main__":
    main()