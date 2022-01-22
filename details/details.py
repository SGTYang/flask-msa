import json
from flask import Flask, request, Response, abort
from flask_restx import Resource, Api, fields

app = Flask(__name__)

api = Api(app)

movie_code_dict={
    '20133165':{
        "movie_name": '이블데드',
        "movie_year": '2013',
        "movie_director": '페드 알바레즈',
        "movie_genre": '공포(호러)'
        },
    '20161081':{
        "movie_name": '애나벨: 인형의 주인',
        "movie_year": '2017',
        "movie_director": '데이비드 F. 샌드버그',
        "movie_genre": '공포(호러)',
        },
    '20178126':{
        "movie_name": '인시디어스4: 라스트키',
        "movie_year": '2017',
        "movie_director": '애덤 로비텔',
        "movie_genre": '공포(호러)',
        },
    '20162941':{ 
        "movie_name": "컨저링 2",
        "movie_year": "2016",
        "movie_director": "제임스 완",
        "movie_genre": "공포(호러)",
        },
    '20152781':{
        "movie_name": "배트맨 대 슈퍼맨: 저스티스의 시작",
        "movie_year": "2016",
        "movie_director": "잭 스나이더",
        "movie_genre": "액션",
        },
    '20217845':{
        "movie_name": "더 수어사이드 스쿼드",
        "movie_year": "2021",
        "movie_director": "제임스 건",
        "movie_genre": "액션",
        },
    '20143253':{
        "movie_name": "존 윅",
        "movie_year": "2014",
        "movie_director": "채드 스타헬스키",
        "movie_genre": "액션",
        },
    '20166101':{
        "movie_name": "존 윅 - 리로드",
        "movie_year": "2017",
        "movie_director": "채드 스타헬스키",
        "movie_genre": "액션",
        },
    '20196655':{
        "movie_name": "존 윅 3: 파라벨룸",
        "movie_year": "2019",
        "movie_director": "채드 스타헬스키",
        "movie_genre": "액션",
        },
    '20136961':{
        "movie_name": "퍼시릭 림",
        "movie_year": "2013",
        "movie_director": "길예르모 델 토로",
        "movie_genre": "액션",
        },
    '20174603':{
        "movie_name": "퍼시픽 림: 업라이징",
        "movie_year": "2018",
        "movie_director": "스티븐 S. 드나이트",
        "movie_genre": "액션",
        }
}

ns_movies = api.namespace('ns_movies', description='Movies APIs')

movie_data = api.model(
    'movie_code',
    {
      "movie_name": fields.String(description="movie name", required=True),
      "movie_year": fields.String(description="movie year", required=True),
      "movie_director": fields.String(description="movie director", required=True),
      "movie_genre": fields.String(description="movie genre", required=True),
    }
)

@app.route('/movie/<string:movie_code>')
def get(movie_code):
    if movie_code not in movie_code_dict.keys():
       abort(404, description=f"Movie {movie_code} doesn't exist")
    data = movie_code_dict[movie_code]
    return json.dumps(data)

@ns_movies.route('/swagger/<string:movie_code>')
class movies(Resource):
    def get(self, movie_code):
        if movie_code not in movie_code_dict.keys():
            abort(404, description=f"Movie Code {movie_code} doesn't exist")
        data = movie_code_dict[movie_code]
        return {
            'movie code': movie_code,
            'data': data
        }
    @ns_movies.expect(movie_data)
    def post(self, movie_code):
        if movie_code in movie_code_dict.keys():
            abort(409, description=f"Movie {movie_code} already exists")

        movie_code_dict[movie_code] = request.get_json()
        return Response(status=201)

    def delete(self, movie_code):
        if not movie_code in movie_code_dict.keys():
            abort(404, description=f"Movie {movie_code} doesn't exists")
        
        del movie_code_dict[movie_code]
        return Response(status=200)

    @ns_movies.expect(movie_data)
    def put(self, movie_code):
        if not movie_code in movie_code_dict.keys():
            abort(404, description=f"Movie code {movie_code} doesn't exists")

        movie_code_dict[movie_code] = request.get_json()
        return Response(status=200)


if __name__=="__main__":
   app.run(host="0.0.0.0", port="80", debug=True)