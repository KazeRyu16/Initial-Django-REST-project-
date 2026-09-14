import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):

    print(request.GET) #url query params
    print(request.POST)
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass

    #print(data)
    data['params'] = dict(request.GET) 
    data['headers'] = dict(request.headers) # dict --> means store the data in the data dictionary
    print(data['headers'])
    # print(data['headers'])    #prints evrything content_type,length,etc included
    # print(request.content_type) #prints the content type
    return JsonResponse(data) # returns json data


