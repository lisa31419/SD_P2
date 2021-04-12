from flask_restful import reqparse, Resource

from data import places


class Places(Resource):
    def get(self, id):
        place = next(iter([x for x in places if x["id"] == id]), None)
        return {'place': place}, 200 if place else 404

    def post(self, id):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type

        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('country', type=str)
        parser.add_argument('disciplines', type=str,
                            action="append")  # action = "append" is needed to determine that is a list of strings

        data = parser.parse_args()
        return {'message': "Not developed yet"}, 404

    def delete(self, id):
        return {'message': "Not developed yet"}, 404

    def put(self, id):
        return {'message': "Not developed yet"}, 404
