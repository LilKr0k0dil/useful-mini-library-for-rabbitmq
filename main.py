import multiprocessing
import ss
import sys
import json
from flask import Flask, request

app = Flask(__name__)
processes = []


        
        


@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()
    processes = []

    for queue_data in request_data[0]['queue']:
        host = request_data[0]['server-mq']['address']
        queue = queue_data['name']
        p = multiprocessing.Process(target=ss.read_and_write, args=(queue,host))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()



    

if __name__ == '__main__':
    app.run(debug=True, port=5000)