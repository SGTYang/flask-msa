from flask import Flask, render_template
import os
import requests

app = Flask(__name__)

#환경 변수 불러오기
detailsHost = os.environ.get("DETAILS_SVC_SERVICE_HOST")
detailsPort = os.environ.get("DETAILS_SVC_SERVICE_PORT")

@app.route('/home')
@app.route('/')
def front():
  return render_template('index.html')

#영화 정보 조회 요청보내기
@app.route('/movie/<string:movie_code>')
def movieInfoRoute(movie_code):
  try:
    # 데이터를 보낼 때 딕셔너리 형태로 보낸다.
    details = requests.get(f'http://{detailsHost}:{detailsPort}/movie/{movie_code}').json()
  except BaseException:
    details = None

  if details:
    return render_template(
    'details.html',
    movie_code=movie_code,
    movie_name=details['movie_name'],
    movie_year=details['movie_year'],
    movie_director=details['movie_director'],
    movie_genre=details['movie_genre'],
    image_file = movie_code+'.jpg',
    )
  else:
    return render_template('error.html')

if __name__=="__main__":
   app.run(host="0.0.0.0", port="80", debug=True)