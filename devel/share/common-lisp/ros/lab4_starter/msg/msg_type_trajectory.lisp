; Auto-generated. Do not edit!


(cl:in-package lab4_starter-msg)


;//! \htmlinclude msg_type_trajectory.msg.html

(cl:defclass <msg_type_trajectory> (roslisp-msg-protocol:ros-message)
  ((trajectory
    :reader trajectory
    :initarg :trajectory
    :type (cl:vector lab4_starter-msg:msg_type_position)
   :initform (cl:make-array 0 :element-type 'lab4_starter-msg:msg_type_position :initial-element (cl:make-instance 'lab4_starter-msg:msg_type_position))))
)

(cl:defclass msg_type_trajectory (<msg_type_trajectory>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <msg_type_trajectory>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'msg_type_trajectory)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lab4_starter-msg:<msg_type_trajectory> is deprecated: use lab4_starter-msg:msg_type_trajectory instead.")))

(cl:ensure-generic-function 'trajectory-val :lambda-list '(m))
(cl:defmethod trajectory-val ((m <msg_type_trajectory>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lab4_starter-msg:trajectory-val is deprecated.  Use lab4_starter-msg:trajectory instead.")
  (trajectory m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <msg_type_trajectory>) ostream)
  "Serializes a message object of type '<msg_type_trajectory>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'trajectory))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'trajectory))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <msg_type_trajectory>) istream)
  "Deserializes a message object of type '<msg_type_trajectory>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'trajectory) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'trajectory)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'lab4_starter-msg:msg_type_position))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<msg_type_trajectory>)))
  "Returns string type for a message object of type '<msg_type_trajectory>"
  "lab4_starter/msg_type_trajectory")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'msg_type_trajectory)))
  "Returns string type for a message object of type 'msg_type_trajectory"
  "lab4_starter/msg_type_trajectory")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<msg_type_trajectory>)))
  "Returns md5sum for a message object of type '<msg_type_trajectory>"
  "7fe035463acb6da30cda877f198c818b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'msg_type_trajectory)))
  "Returns md5sum for a message object of type 'msg_type_trajectory"
  "7fe035463acb6da30cda877f198c818b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<msg_type_trajectory>)))
  "Returns full string definition for message of type '<msg_type_trajectory>"
  (cl:format cl:nil "msg_type_position[] trajectory~%================================================================================~%MSG: lab4_starter/msg_type_position~%float64[2] position~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'msg_type_trajectory)))
  "Returns full string definition for message of type 'msg_type_trajectory"
  (cl:format cl:nil "msg_type_position[] trajectory~%================================================================================~%MSG: lab4_starter/msg_type_position~%float64[2] position~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <msg_type_trajectory>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'trajectory) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <msg_type_trajectory>))
  "Converts a ROS message object to a list"
  (cl:list 'msg_type_trajectory
    (cl:cons ':trajectory (trajectory msg))
))
