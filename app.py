from flask import Flask , jsonify 
from sort_search import find_movie_name , find_movie_id
app = Flask(__name__)

# csv data path 
FILE_NAME = "database/film.csv"
app.config['STRICT_SLASHED'] = False

# get the id , name , summary in the dict
def summary(value:list|str)->dict:
   if value:
      id, name, summary = value
      result = {
         'ID': int(id),
         'Name': name,
         'Summary': summary
      }
   else:
      result = {
         'ID': None,
         'Name':"not found.",
         'summary':None
      }
   return result 

#search movie  by name  in csv file
@app.route('/<string:movie>/', methods=['GET'])
def search_movie(movie:str)-> dict:
   movie = movie.replace('_',' ')
   value = find_movie_name(movie.strip(), FILE_NAME)
   result = summary(value)
   return jsonify(result)

# serach by id  in csv file 
@app.route('/<int:id>/', methods=['GET'])
def search_id(id:int) -> dict:
   print(id)
   value = find_movie_id(int(id) , FILE_NAME)
   
   result = summary(value)
   return jsonify(result)


if __name__ == '__main__':
   app.run(debug = True)
