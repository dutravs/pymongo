import pymongo
from pymongo import MongoClient
import datetime


client = MongoClient('localhost', 27017)
db = client['anatel']

collection = db['minas']

#Questão 03 - Quantos documentos possui a coleção minas? (Arquivos duplicados)
#result = list(collection.find())
#print(len(result))

#Questão 04 - Mostre os 5 primeiros documentos da coleção. 
#result = list(collection.find().limit(5))
#print(result)

#Questão 05 - Selecione o documento que possui o maior número de solicitações QtdeSolic na Anatel.
# result = list(collection.aggregate([
#     {
#         '$sort': {
#             'QtdeSolic': -1
#         }
#     }, {
#         '$limit': 1
#     }
# ]))
# print(result)

#Questão 06 - Qual é o menor número de solicitações QtdeSolic na Anatel?
# result = list(collection.aggregate([
#     {
#         '$sort': {
#             'QtdeSolic': 1
#         }
#     }, {
#         '$limit': 1
#     }
# ]))
# print(result)

#Questão 07 - Mostre todos os documentos com o menor número de solicitações QtdeSolic na Anatel.
# result_menor = list(collection.aggregate([
#     {
#         '$sort': {
#             'QtdeSolic': 1
#         }
#     }, {
#         '$limit': 1
#     }
# ]))

# result = list(collection.aggregate([
#     {
#         '$match': {
#             'QtdeSolic': result_menor[0]['QtdeSolic']
#         }
#     }
# ]))

# print(result)

#Questão 08 - Mostre as contagens de solicitações QtdeSolic por tipo de serviço Servico, em ordem decrescente pelas contagens

#Questão 09 - Mostre todos os documentos com atributo Tipo igual a "Reclamação".
# result = list(collection.aggregate([
#     {
#         '$match': {
#             'Tipo': 'Reclamação'
#         }
#     }
# ]))
# print(result)

#Questão 10 - Quais diferentes valores encontramos em Tipo?

#result = list(collection.distinct('Tipo'))
#print(result)   
