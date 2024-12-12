import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
  # Working Funciton have the conditions
  def working(val):
       
   length = len(val.split(" "))
   for i in range(length):
      if val.split(" ")[i][0:5] == "DIAB1": 
         return True
   
   return False

  
  return patients[patients["conditions"].apply(lambda x: len(x)>= 5 and working(x))]