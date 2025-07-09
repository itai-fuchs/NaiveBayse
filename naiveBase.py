from model import Model
from clean_table import Clean_csv


class ProbabilityCalculation:
    def __init__(self,user_input,model,target_variable):
        self.user_input=user_input
        self.model=model
        self.target_variable=target_variable


    def calculation(self):
        result={}
        for key,val in self.user_input.items():
            for uniq_target in self.model:
                if uniq_target not in result :
                    result[uniq_target] =(0.00001  +self.model[uniq_target][key][val]) *self.target_variable[uniq_target]
                else:
                    result[uniq_target]*=self.model[uniq_target][key][val] +0.00001
        for key,val in result.items():

            result[key]=round(val,3)
        return result

    def result(self):
        result=self.calculation()
        return max(result,key=result.get)








a={'age': "senior", 'income': 'high', 'student': 'no', 'credit_rating': 'excellent'}
b={'age': 'senior', 'income': 'low', 'student': 'yes', 'credit_rating': 'excellent'}
c={'age': 'senior', 'income': 'medium', 'student': 'no', 'credit_rating': 'excellent'}
d={'age': 'youth', 'income': 'high', 'student': 'no', 'credit_rating': 'fair'}
e= {'age': 'youth', 'income': 'medium', 'student': 'no', 'credit_rating': 'fair'}

ct = Clean_csv("C:/Users/itai/Downloads/buy_computer_data.csv")
ct.execute()

m = Model(ct.table)
m.execute()

p=ProbabilityCalculation(b,m.model,m.target_variable())
print(p.calculation())




