class BayesianClassifier:
    """
    Prediction based on a Bayesian model
    """

    @staticmethod
    def calc_prediction(data, model, ratio_target_variable):
        result = {}

        for target_col in model:

            prob = ratio_target_variable.get(target_col, 0)

            for col, val in data.items():
                val_prob = model[target_col][col].get(val, 0.01)
                prob *= val_prob

            result[target_col] = prob

        return result

    @staticmethod
    def prediction(data, model, ratio_target_variable):
        predict = BayesianClassifier.calc_prediction(data, model, ratio_target_variable)

        return max(predict, key=predict.get)
