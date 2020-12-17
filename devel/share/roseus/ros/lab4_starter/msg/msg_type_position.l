;; Auto-generated. Do not edit!


(when (boundp 'lab4_starter::msg_type_position)
  (if (not (find-package "LAB4_STARTER"))
    (make-package "LAB4_STARTER"))
  (shadow 'msg_type_position (find-package "LAB4_STARTER")))
(unless (find-package "LAB4_STARTER::MSG_TYPE_POSITION")
  (make-package "LAB4_STARTER::MSG_TYPE_POSITION"))

(in-package "ROS")
;;//! \htmlinclude msg_type_position.msg.html


(defclass lab4_starter::msg_type_position
  :super ros::object
  :slots (_position ))

(defmethod lab4_starter::msg_type_position
  (:init
   (&key
    ((:position __position) (make-array 2 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _position __position)
   self)
  (:position
   (&optional __position)
   (if __position (setq _position __position)) _position)
  (:serialization-length
   ()
   (+
    ;; float64[2] _position
    (* 8    2)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[2] _position
     (dotimes (i 2)
       (sys::poke (elt _position i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[2] _position
   (dotimes (i (length _position))
     (setf (elt _position i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(setf (get lab4_starter::msg_type_position :md5sum-) "f44864fd31f13dff3a84000f39a69268")
(setf (get lab4_starter::msg_type_position :datatype-) "lab4_starter/msg_type_position")
(setf (get lab4_starter::msg_type_position :definition-)
      "float64[2] position

")



(provide :lab4_starter/msg_type_position "f44864fd31f13dff3a84000f39a69268")


