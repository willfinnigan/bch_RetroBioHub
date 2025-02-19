'''
This route handles the requests send by retrobiocat and distributes it
'''


from flask_restx import Resource, Namespace, Model, fields
from flask import request


import json

from Models.retrobiocat_query_payload import PayloadRetrobiocat
from retrobiohub.retrobiocat_biocathub_mapper.retrobiocat_biocathub_mapper import RetrobiocatBiocathubMapper
#from Models.parser_for_planning import Retrobiocat_model as rbc_model
import retrobiohub.mini_mongo_adapter as MiniMongo 


ns = Namespace("Mini Mongo query", description="Queries MiniMongo")




class RequestHandler(Resource):
    '''
    Test Instance this class will be removed in the near future
    '''
    @ns.doc()
    def post(self):

        db = MiniMongo.MiniMongo()
        entry = db.get_collection_by_id("61ed3b2c1c97376beba509f0")
        print(entry)
        response = entry["experiment"]


        res = "Minimongo"
        return response

ns.add_resource(RequestHandler, "/")

