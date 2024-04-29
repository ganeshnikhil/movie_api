import csv 
from fuzzywuzzy import fuzz
import time 
# index the sorted data in correct way 

def sno_sorted_data(data:list[int , str , str]) -> list:
   new_no = []
   for index , names in enumerate(data):
      new_no.append([index+1] + names[1:])
   return new_no 


# read the csv data then sort it;.
def sort_csv_data(path:str)-> tuple:
   data = csv.reader(open(path))
   data = list(data)
   first = data[0]
   sorted_data = sorted(data[1:], key=lambda x: x[1].strip().lower())
   arrange_sno = sno_sorted_data(sorted_data)
   return (first,  arrange_sno)

# write the csv data in file 
def write_csv_data(path:str , header:list[str , str , str] , data:list[int , str , str]) -> None:
   # writing to csv file
   with open(path, 'w') as csvfile:
      # creating a csv writer object
      csvwriter = csv.writer(csvfile)
      # writing the fields
      csvwriter.writerow(header)
      # writing the data rows
      csvwriter.writerows(data)


# find probable movie it could be avoid mispell
def prob_movie_name(target:str, path:str)-> str:
   data = list(csv.reader(open(path)))
   movie_names = [val[1].strip().lower() for val in data[1:]]
   target = target.strip().lower()

   # Fuzzy search with threshold (adjust as needed)
   best_match = None
   best_score = float('-inf')  # Negative infinity
   for name in movie_names:
      score = fuzz.ratio(target, name)
      # Use ratio for overall similarity
      if score > best_score:
         best_match = data[movie_names.index(name) + 1]
         best_score = score

   # Return exact match or closest fuzzy match if threshold met
   threshold = 80  # Adjust threshold for desired accuracy vs. strictness
   return best_match if best_score >= threshold else ''


def find_movie_prob(target:str, data:list[int , str , str], movie_names:list[str]) -> str:
   best_match = None
   best_score = float('-inf')  # Negative infinity
   for name in movie_names:
      score = fuzz.ratio(target, name)
      # Use ratio for overall similarity
      if score > best_score:
         best_match = data[movie_names.index(name) + 1]
         best_score = score
   #print(best_score)
   # Return exact match or closest fuzzy match if threshold met
   threshold = 80  # Adjust threshold for desired accuracy vs. strictness
   return best_match if best_score >= threshold else ''

# find the movie name from csv data using binary search and return the summary 
def find_movie_name(target:str , path:str) -> str:
   data = list(csv.reader(open(path)))
   movie_names = [val[1].strip().lower() for val in data[1:]]
   target = target.strip().lower()
   left = 0 
   right = len(movie_names) - 1 
   while left < right:
      mid = (left+right)//2 
      if movie_names[mid] == target:
         return data[mid+1]
      elif movie_names[mid] < target:
         left = mid + 1
      else:
         right = mid 
   return find_movie_prob(target , data , movie_names)


         
# find the movie by gien id no 
def find_movie_id(id:int, path:str) -> str:
   data = list(csv.reader(open(path)))
   if id > 0 and id <= len(data):
      value = data[id]
      return value 
   return ''


def measure_time() -> int:
   """
   Decorator to measure the execution time of a function.
   """
   start_time = time.time()
   find_movie_name("the matrx", "database/film.csv")
   # prob_movie_name("fuck", "database/film.csv")
   end_time = time.time()
   return end_time - start_time

if __name__ == "__main__":
   print(measure_time())
   
   
   
#print(measure_time())
#print(prob_movie_name("the matrix","database/film.csv"))
#header, data = sort_csv_data('film_1.csv')
#write_csv_data("film_2.csv" , header , data)
# for i , val in enumerate(sort_csv_data("film_1.csv")):
#    print( i , val[0])
# #sort_csv_data("film.csv")
# value = find_movie_name("the matrix", "database/film.csv")
# if value:
#    if len(value) == 3:
#       id , name , summary = value 
      
#       result = {
#          'ID':int(id),
#          'Name':name,
#          'Summary':summary
#       }
#       print(result)
#    else:
#       print(value)
# else:
#    print("Data not found ....")

# # header , data = sort_csv_data('film.csv')
# # write_csv_data('film_1.csv',header , data)

