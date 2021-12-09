from flask_restx import Resource, Namespace, Model, fields
from Models.retrobiocat_query_payload import Experiment

ns = Namespace("Request Handler", description="Routes handling Requests from Retrobiocat")


modelExperiment = Experiment().define_reaction()

model = ns.model("Experiment", modelExperiment)


class RequestHandler(Resource):
    @ns.doc(body=model, model=model)
    def post(self):
    
        return "success"

class ResponseHeader(Resource):
    @ns.doc(body=model)
    def get(self):
        return "444"


ns.add_resource(RequestHandler, "")
ns.add_resource(ResponseHeader, "/res")






'''
experiment = {
    "name": fields.String,
    "enzyme": fields.String
}

experimentModel = Model(experiment)

user_fields = ns.model("User", {
    "name": fields.String,
    "id":fields.String
})

user = ns.model("UserData", {
    "identity": fields.Nested(user_fields)
})

ns.add_model("Reaction", Reaction)
experimentSwagger = ns.add_model("experimentModel",{"name":fields.String})


reaction = ns.model("Experiment", {"name":fields.String})


'''