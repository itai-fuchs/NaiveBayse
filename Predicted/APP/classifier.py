import logging

class BayesianClassifier:
    """
    Prediction based on a Bayesian model
    """

    @staticmethod
    def calc_prediction(sample, model, ratio_target_variable):
        logging.debug(f"Calculating prediction for sample: {sample}")
        result = {}

        for target_val in model:
            prob = ratio_target_variable.get(target_val, 0)
            logging.debug(f"Initial probability for target '{target_val}': {prob}")

            for col, val in sample.items():
                val_prob = model[target_val][col].get(val, 0.01)
                prob *= val_prob
                logging.debug(f"Multiplying by P({col}={val}|{target_val})={val_prob}, cumulative prob={prob}")

            result[target_val] = prob
            logging.debug(f"Result probability for target '{target_val}': {prob}")

        return result

    @staticmethod
    def prediction(sample, model, ratio_target_variable):
        prediction_probs = BayesianClassifier.calc_prediction(sample, model, ratio_target_variable)
        logging.info(f"Prediction probabilities: {prediction_probs}")
        predicted_class = max(prediction_probs, key=prediction_probs.get)
        logging.info(f"Predicted class: {predicted_class}")
        return predicted_class
