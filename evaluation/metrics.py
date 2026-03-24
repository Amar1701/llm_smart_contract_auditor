# File: evaluation/metrics.py

class EvaluationMetrics:
    """
    Calculates system performance metrics with normalization
    """

    def normalize(self, name):
        name = name.lower()

        mapping = {
            "reentrancy": "reentrancy",
            "low level call": "low-level-calls",
            "solidity version": "solc-version"
        }

        for key in mapping:
            if key in name:
                return mapping[key]

        return name

    def evaluate(self, detected, slither_detected):
        detected_set = set([self.normalize(d["name"]) for d in detected])
        slither_set = set([self.normalize(s) for s in slither_detected])

        true_positive = len(detected_set & slither_set)
        false_positive = len(detected_set - slither_set)
        false_negative = len(slither_set - detected_set)

        precision = true_positive / (true_positive + false_positive + 1e-6)
        recall = true_positive / (true_positive + false_negative + 1e-6)
        accuracy = true_positive / (true_positive + false_positive + false_negative + 1e-6)
        f1_score = 2 * (precision * recall) / (precision + recall + 1e-6)

        return {
            "Precision": round(precision, 2),
            "Recall": round(recall, 2),
            "Accuracy": round(accuracy, 2),
            "F1 Score": round(f1_score, 2),
            "False Positives": false_positive,
            "False Negatives": false_negative
        }