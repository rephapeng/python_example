import zmq
import time
import sys
import msgpack
from elasticsearch import Elasticsearch

es = Elasticsearch("http://192.168.65.4:9002")
port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    #  Wait for next request from client
    message = socket.recv()
    recieve = msgpack.unpackb(message)
    res = es.index(index="test-merapilabs", doc_type='server-log', id=recieve['timestamp'], body=recieve)
    print(res['created'])

    res = es.get(index="test-merapilabs", doc_type='server-log', id=1)
    print(res['_source'])

    es.indices.refresh(index="test-index")
    print "Received request: ", recieve
    time.sleep (1)  
    socket.send("World from %s" % port)
