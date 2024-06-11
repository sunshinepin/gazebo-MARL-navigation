#!/usr/bin/env python

import rospy
import tf
import tf2_ros
from geometry_msgs.msg import TransformStamped

def handle_world_to_odom(ns):
    br = tf2_ros.TransformBroadcaster()
    t = TransformStamped()
    
    t.header.frame_id = 'world'
    t.child_frame_id = ns + '/odom'
    
    t.transform.translation.x = 0.0
    t.transform.translation.y = 0.0
    t.transform.translation.z = 0.0
    t.transform.rotation.x = 0.0
    t.transform.rotation.y = 0.0
    t.transform.rotation.z = 0.0
    t.transform.rotation.w = 1.0
    
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        t.header.stamp = rospy.Time.now()
        br.sendTransform(t)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('world_to_odom_broadcaster')
    namespace = rospy.get_param('~namespace', '')
    handle_world_to_odom(namespace)
    rospy.spin()