nums = [3,4,9,6,2]

def divisiblebytwo():
  for i in nums:
    if i % 2 == 0:
      print(f'{i}: osztható')
    else:
      print(f'{i}: nem osztható')
      
#TEST
divisiblebytwo()