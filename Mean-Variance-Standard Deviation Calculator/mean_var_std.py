import numpy as np

def calculate(list):
  if len(list) !=9 :
    raise ValueError("List must contain nine numbers.")
  list = np.reshape(list,(3,3))
  calculations ={
    'mean': [
      np.mean(list, axis =0).tolist(), 
      np.mean(list, axis =1).tolist(), 
      np.mean(list.tolist())
      ],
    'variance': [
      np.var(list, axis =0).tolist(),
       np.var(list, axis =1).tolist(), 
       np.var(list.tolist())
       ],
    'standard deviation': [
      np.std(list, axis =0).tolist(), 
      np.std(list, axis =1).tolist(), 
      np.std(list.tolist())
      ],
    'max': [
      np.max(list, axis =0).tolist(), 
      np.max(list, axis =1).tolist(), 
      np.max(list.tolist())
      ],
    'min': [
      np.min(list, axis =0).tolist(), 
      np.min(list, axis =1).tolist(), 
      np.min(list.tolist())
      ],
    'sum': [
      np.sum(list, axis =0).tolist(), 
      np.sum(list, axis =1).tolist(), 
      np.sum(list.tolist())]
  }

  return calculations
  



  