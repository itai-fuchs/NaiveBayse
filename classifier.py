class BayesianClassifier:
    """
    Prediction based on a Bayesian model
    """

    @staticmethod
    def calc_prediction(data, model, ratio_target_variable):
        result = {}

        for target_class in model:
            # התחל עם ההסתברות המקדימה של המחלקה
            prob = ratio_target_variable.get(target_class, 0)

            for col, val in data.items():
                # קבל את ההסתברות המותנית, ואם הערך לא קיים במודל, נשתמש בסכום קטן (smoothing)
                val_prob = model[target_class][col].get(val, 0.01)
                prob *= val_prob

            result[target_class] = prob

        return result

    @staticmethod
    def prediction(data, model, ratio_target_variable):
        predict = BayesianClassifier.calc_prediction(data, model, ratio_target_variable)
        # בחר את המחלקה עם ההסתברות המקסימלית
        return max(predict, key=predict.get)
