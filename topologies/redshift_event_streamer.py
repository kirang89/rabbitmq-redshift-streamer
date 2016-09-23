from streamparse import Topology

from bolts.redshift_bolt import RedshiftBolt
from spouts.rabbitmq_spout import RabbitMQSpout


class RedshiftEventStreamer(Topology):
    rabbitmq_spout = RabbitMQSpout.spec()
    redshift_bolt = RedshiftBolt.spec(inputs=[rabbitmq_spout], par=2)
