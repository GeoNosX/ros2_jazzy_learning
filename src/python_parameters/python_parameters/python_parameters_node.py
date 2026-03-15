import rclpy
from rclpy.node import Node

class MinimalParam(Node):

    def __init__(self):
        super().__init__('minimal_param_node')
        self.declare_parameter('my_parameter','world')
        self.timer =self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        my_param=self.get_parameter('my_parameter').get_parameter_value().string_value
        self.get_logger().info('Hello %s' % my_param)

def main(args=None):
    rclpy.init(args=args)
    minimal_param = MinimalParam()
    rclpy.spin(minimal_param)
    minimal_param.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()