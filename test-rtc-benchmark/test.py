# import time
# import requests
# import os
#
# # API_KEY = os.environ['API_KEY']
# API_KEY = 'a008b118-023f-42d0-a65f-156499ba2ae5'
# test_id = '6252917e72e72e00129e3652'
# CPU_LIMIT = 0.5
# BASE_URL = 'https://api.testrtc.com/v1'
# HEADERS = {'apikey': API_KEY}
#
# args = {
#     "executionParameters": {
#         "concurrentUsers": 1,
#         "sessionSize": 50
#     }
# }
#
#
# def getRunStatus(test_run_id):
#     return
#
#
# print("starting Empty single slide benchmark test")
# res = requests.post(BASE_URL + '/tests/{}/run'.format(test_id), headers=HEADERS, json=args)
# if res.status_code != 200:
#     print('Error on test {} code {}'.format(test_id, res.status_code))
#     exit(1)
# run_id=res.json()['testRunId']
# run = requests.get(BASE_URL + '/testruns/{}?detailed=true'.format(run_id),
#                          headers=HEADERS,
#                          json=args)
# runStatus=run.json().get('status')
#
# if runStatus != 'started':
#     print("Error running the test")
#     exit(1)
# else:
#     while runStatus == 'started':
#         print ("test is running")
#         time.sleep(30)
#         run = requests.get(BASE_URL + '/testruns/{}?detailed=true'.format(run_id),
#                            headers=HEADERS,
#                            json=args)
#         runStatus = run.json().get('status')
#
# results = requests.get(BASE_URL + '/testruns/{}?detailed=true'.format(run_id), headers=HEADERS,json=args)
# print(results.json())
# avg_CPU = (results.json().get('stats').get('performance').get('browserCpu').get('avg'))
#
# if avg_CPU > CPU_LIMIT:
#     print('Test failed - CPU was above limit')
#     print('url to the test is: ' + results.json().get('url'))
#     exit(1)
# else:
#     print('Test Passed - CPU was below limit')
#     print("URL to the test : " + results.json().get('url'))
#     exit(0)
