from flask import Flask, render_template
import os
import requests

app = Flask(__name__)

#환경 변수 불러오기
detailsHost = os.environ.get("DETAILS_SVC_SERVICE_HOST")

@app.route('/')
@app.route('/home')
@app.route('/index')
def front():
  return render_template('index.html')

#영화 정보 조회 요청보내기
@app.route('/movie/<string:movie_code>', methods=['GET'])
def movieInfoRoute(movie_code):
  try:
    # 데이터를 보낼 때 딕셔너리 형태로 보낸다. 없는 페이지 요청해도 에러를 띄우지 않는다.
    details = requests.get(f'http://{detailsHost}:80/details/{movie_code}').json()
  except BaseException:
    details = None

  if details:
    return render_template(
    'details.html',
    movie_code=details['movieInfoResult']['movieInfo']['movieCd'],
    movie_name=details['movieInfoResult']['movieInfo']['movieNm'],
    movie_year=details['movieInfoResult']['movieInfo']['prdtYear'],
    movie_director=details['movieInfoResult']['movieInfo']['directors'][0]['peopleNm'],
    movie_genre=details['movieInfoResult']['movieInfo']['genres'][0]['genreNm'],
    image_file = movie_code+'.jpg',
    )
  else:
    return render_template('error.html')

if __name__=="__main__":
   app.run(host="0.0.0.0", port="80", debug=True)
