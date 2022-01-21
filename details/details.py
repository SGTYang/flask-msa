import urllib.request
import json
from flask import Flask

app = Flask(__name__)

@app.route('/details/<string:movie_code>', methods=['GET'])
# 영화진흥원 api를 통해 영화 상세정보를 가져온다.
def get_movie_details(movie_code):
    key_num = '7a5569340435ebbf7c32fbfa54d229a9'
    url_get_details = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
    url = f'{url_get_details}?key={key_num}&movieCd={movie_code}'
    #데이터를 보낼 때 인코딩하여 바이너리 형태로 보낸다. 없는 페이지 요청하면 에러를 띄운다
    req = urllib.request.Request(url)
    data_get = urllib.request.urlopen(req).read()
    data_json = json.loads(data_get)
    return json.dumps(data_json)

if __name__=="__main__":
   app.run(host="0.0.0.0", port="80", debug=True)
