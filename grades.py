grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85]

def grades_sum(scores):
  total = 0
  for score in scores:
    total += score
  return total

print (grades_sum(grades))

def grades_average(grades_input):
    input = float(len(grades_input))
    sum = grades_sum(grades_input)
    average = float(sum/input)
    print(average)

grades_average([10,20,30,40,50,50])