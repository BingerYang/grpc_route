# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import route_pb2 as proto_dot_route__pb2


class RouteStub(object):
  """Define route
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.handle = channel.unary_unary(
        '/Route/handle',
        request_serializer=proto_dot_route__pb2.Request.SerializeToString,
        response_deserializer=proto_dot_route__pb2.Response.FromString,
        )


class RouteServicer(object):
  """Define route
  """

  def handle(self, request, context):
    """common rpc function
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RouteServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'handle': grpc.unary_unary_rpc_method_handler(
          servicer.handle,
          request_deserializer=proto_dot_route__pb2.Request.FromString,
          response_serializer=proto_dot_route__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Route', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))