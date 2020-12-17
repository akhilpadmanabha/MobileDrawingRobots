; Auto-generated. Do not edit!


(cl:in-package lab4_starter-msg)


;//! \htmlinclude msg_type_position.msg.html

(cl:defclass <msg_type_position> (roslisp-msg-protocol:ros-message)
  ((position
    :reader position
    :initarg :position
    :type (cl:vector cl:float)
   :initform (cl:make-array 2 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass msg_type_position (<msg_type_position>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <msg_type_position>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'msg_type_position)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lab4_starter-msg:<msg_type_position> is deprecated: use lab4_starter-msg:msg_type_position instead.")))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <msg_type_position>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lab4_starter-msg:position-val is deprecated.  Use lab4_starter-msg:position instead.")
  (position m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <msg_type_position>) ostream)
  "Serializes a message object of type '<msg_type_position>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'position))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <msg_type_position>) istream)
  "Deserializes a message object of type '<msg_type_position>"
  (cl:setf (cl:slot-value msg 'position) (cl:make-array 2))
  (cl:let ((vals (cl:slot-value msg 'position)))
    (cl:dotimes (i 2)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<msg_type_position>)))
  "Returns string type for a message object of type '<msg_type_position>"
  "lab4_starter/msg_type_position")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'msg_type_position)))
  "Returns string type for a message object of type 'msg_type_position"
  "lab4_starter/msg_type_position")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<msg_type_position>)))
  "Returns md5sum for a message object of type '<msg_type_position>"
  "f44864fd31f13dff3a84000f39a69268")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'msg_type_position)))
  "Returns md5sum for a message object of type 'msg_type_position"
  "f44864fd31f13dff3a84000f39a69268")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<msg_type_position>)))
  "Returns full string definition for message of type '<msg_type_position>"
  (cl:format cl:nil "float64[2] position~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'msg_type_position)))
  "Returns full string definition for message of type 'msg_type_position"
  (cl:format cl:nil "float64[2] position~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <msg_type_position>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'position) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <msg_type_position>))
  "Converts a ROS message object to a list"
  (cl:list 'msg_type_position
    (cl:cons ':position (position msg))
))
