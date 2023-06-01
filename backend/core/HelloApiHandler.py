from flask_restful import Api, Resource, reqparse

class HiApiHandler(Resource):
    def get(self):
        return {
                'resultStatus': 'SUCCESS',
                'message': "Hello API Handler"
                }


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)

        args = parser.parse_args()

        #note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        request_type = args['type']
        request_json = args['message']
        # process request_type and request_json here
        # currently just returning directly for demo purposes
        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
          message = "Your Message Requested: {}".format(ret_msg)
        else:
          message = "No Msg"
        
        final_ret = {"resultStatus": "Success", "message": message}

        return final_ret


