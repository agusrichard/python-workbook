from concurrent import futures
import grpc
import time
import unary_pb2 as pb2
import unary_pb2_grpc as pb2_grpc


class UnaryService(pb2_grpc.UnaryServicer):
    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        message = request.message
        result = f'Hello I am up and running received "{message}" message from you'
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)


def serve():
    port = 50051
    print(f"Running on port {port}")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()