from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)

DATA = {
    'places':
        ['rome',
         'london',
         'new york city',
         'los angeles',
         'brisbane',
         'new delhi',
         'beijing',
         'paris',
         'berlin',
         'barcelona']
}

class Places(Resource):
    def get(self):
        return {'data': DATA}, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('location', required=True, location='form')
        args = parser.parse_args()

        if args['location'] in DATA['places']:
            return {
                'message': f"'{args['location']}' already exists."
            }, 401
        else:
            DATA['places'].append(args['location'])
            return {'data': DATA}, 200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('location', required=True, location='form')
        args = parser.parse_args()

        if args['location'] in DATA['places']:
            DATA['places'].remove(args['location'])
            return {'data': DATA}, 200
        else:
            return {
                'message': f"'{args['location']}' does not exist."
                }, 404


api.add_resource(Places, '/places')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)