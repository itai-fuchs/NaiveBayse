

class BayesianClassifier:
    """
    Prediction based on a Bayesian model
    """
    @staticmethod
    def calc_prediction(user_input,model,ratio_target_variable):
        """
        Calculating the prediction
        :param user_input:
        :param model:
        :param ratio_target_variable:
        :return:
        """
        result={}
        for key,val in user_input.items():
            for uniq_target in model:
                if uniq_target not in result :
                    result[uniq_target] =(0.00001  + model[uniq_target][key][val]) *ratio_target_variable[uniq_target]
                else:
                    result[uniq_target]*=model[uniq_target][key][val] +0.00001
        for key,val in result.items():

            result[key]=round(val,3)
        return result

    @staticmethod
    def prediction(user_input, model, target_variable):
        """
        Prediction result
        :param user_input:
        :param model:
        :param target_variable:
        :return:
        """
        predict = BayesianClassifier.calc_prediction(user_input, model, target_variable)
        return max(predict, key=predict.get)



