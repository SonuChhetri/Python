# Q10.  In a town, the percentage of men is 52. The percentage of total literacy is 48. If total percentage of  literate  men  is  35  of  the  total  population,  write  a  program  to  find  the  total  number  of illiterate men and women if the population of the town is 80,000.

def illiterate_count(total_population, literate_men_percent):

  # Calculating the number of literate men
  literate_men = (literate_men_percent / 100) * total_population

  # Calculating the number of men
  men = (52 / 100) * total_population

  # Calculating the number of illiterate men
  illiterate_men = men - literate_men

  # Calculating the number of women
  women = total_population - men

  # Calculating the number of literate women
  literate_women = (48 / 100) * total_population - literate_men

  # Calculating the number of illiterate women
  illiterate_women = women - literate_women

  return illiterate_men, illiterate_women

total_population = 80000

literate_men_percent = 35

# Calculating the number of illiterate men and women
illiterate_men, illiterate_women = illiterate_count(total_population, literate_men_percent)

print("Number of illiterate men:", illiterate_men)
print("Number of illiterate women:", illiterate_women)