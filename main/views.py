# -*- coding: utf-8 -*-
from .forms import LoginForm
import sys
import os
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as dlogin
from django.http import JsonResponse, HttpResponse
from django.conf import settings


@csrf_exempt
def login(request):
    form = LoginForm(request.POST or None)
    aaaaa = form.is_valid()
    if request.method == 'POST' and form.is_valid():
        user = form.authenticate_user()
        dlogin(request, user)
        sign = request.session

        return render(request, 'signin.html')


@csrf_exempt
def signin(request):
    return render(request, 'signin.html')


@csrf_exempt
def req_test(request):
    json_dict = dict()
    xml_data = '''<?xml version="1.0"?><coSpaces total="12"><coSpace id="11111111-477c-1234-8314-123456789123"><name>1111</name><autoGenerated>false</autoGenerated><uri>1111</uri><callId>1111</callId></coSpace><coSpace id="aaa395c5-1591-3211-abcd-027dce062734"><name>abcd</name><autoGenerated>false</autoGenerated><uri>2222</uri><callId>2222</callId></coSpace><coSpace id="672e85d4-12ss-reqw-aaa5-0db0e16cea85"><name>9002</name><autoGenerated>false</autoGenerated><uri>9002</uri><callId>9002</callId></coSpace><coSpace id="f524c55b-cbb8-sddf-9b1a-3dde8dcf8b7f"><name>9800</name><autoGenerated>false</autoGenerated><uri>9800</uri><callId>9800</callId></coSpace><coSpace id="12312312-e96f-435d-84d3-2bfe6e532bc4"><name>9856</name><autoGenerated>false</autoGenerated><uri>9856</uri><callId>9856</callId></coSpace><coSpace id="09876543-eb2f-44f5-bc14-84f825c8c65c"><name>9865</name><autoGenerated>false</autoGenerated><uri>9865</uri><callId>9865</callId></coSpace><coSpace id="123qwerty-632c-41cf-bccc-2265c62bfbaa"><name>TMS_Scheduled_Meeting_6000</name><autoGenerated>false</autoGenerated><uri>6000</uri><callId>6000</callId></coSpace><coSpace id="b9287016-8ad1-4863-a11f-3b07bd9bcde4"><name>TM_기본미팅룸</name><autoGenerated>false</autoGenerated><uri>8991</uri><callId>8991</callId></coSpace><coSpace id="f58c9dcb-7894-5612-3012-f329610db5da"><name>테스트룸</name><autoGenerated>false</autoGenerated><uri>8000</uri><callId>8000</callId></coSpace><coSpace id="55555555-0937-46f9-b39a-506a9f2843af"><name>conferencee</name><autoGenerated>false</autoGenerated><uri>4561</uri><callId>4561</callId></coSpace><coSpace id="08512345-2f90-4f0e-b563-999999999999"><name>testtesttes</name><autoGenerated>false</autoGenerated><uri>4321</uri><callId>4321</callId></coSpace><coSpace id="2e2bdc30-36d6-4a1e-ac3f-90b8fa5b13c0"><name>iiiiiiiii</name><autoGenerated>false</autoGenerated><uri>1235</uri><callId>8888</callId></coSpace></coSpaces>'''
    
    #json_dict['text'] = xml_data
    #json_dict['status_code'] = 200
    print(xml_data)
    response = HttpResponse(xml_data, content_type='text/xml')
    return response


@csrf_exempt
def req_detail(request, id=None):
    read_xml = open(os.path.join(settings.BASE_DIR, 'cospace.xml'), 'r')
    for r in read_xml:
        if r.find(id) != -1:
            res = HttpResponse(r, content_type='text/xml')
            return res
        else:
            res = HttpResponse('<?xml version="1.0"?><failureDetails><coSpaceDoesNotExist /></failureDetails>', content_type='text/xml')
    return res
