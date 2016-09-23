import os
import pika
from streamparse import Spout


class RabbitMQSpout(Spout):
    outputs = ['user_data']

    def initialize(self, stormconf, context):
        scheme = os.environ.get('RABBITMQ_SCHEME', "amqp://guest:guest@127.0.0.1/%2f")  # noqa
        params = pika.URLParameters(scheme)
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="users", durable=True)

    def next_tuple(self):
        method_frame, _, data = self.channel.basic_get(queue="users", no_ack=False)  # noqa
        if method_frame and data:
            self.channel.basic_ack(method_frame.delivery_tag)
            self.emit([data])
