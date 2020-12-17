;; Auto-generated. Do not edit!


(when (boundp 'lab4_starter::msg_type_trajectory)
  (if (not (find-package "LAB4_STARTER"))
    (make-package "LAB4_STARTER"))
  (shadow 'msg_type_trajectory (find-package "LAB4_STARTER")))
(unless (find-package "LAB4_STARTER::MSG_TYPE_TRAJECTORY")
  (make-package "LAB4_STARTER::MSG_TYPE_TRAJECTORY"))

(in-package "ROS")
;;//! \htmlinclude msg_type_trajectory.msg.html


(defclass lab4_starter::msg_type_trajectory
  :super ros::object
  :slots (_trajectory ))

(defmethod lab4_starter::msg_type_trajectory
  (:init
   (&key
    ((:trajectory __trajectory) (let (r) (dotimes (i 0) (push (instance lab4_starter::msg_type_position :init) r)) r))
    )
   (send-super :init)
   (setq _trajectory __trajectory)
   self)
  (:trajectory
   (&rest __trajectory)
   (if (keywordp (car __trajectory))
       (send* _trajectory __trajectory)
     (progn
       (if __trajectory (setq _trajectory (car __trajectory)))
       _trajectory)))
  (:serialization-length
   ()
   (+
    ;; lab4_starter/msg_type_position[] _trajectory
    (apply #'+ (send-all _trajectory :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; lab4_starter/msg_type_position[] _trajectory
     (write-long (length _trajectory) s)
     (dolist (elem _trajectory)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; lab4_starter/msg_type_position[] _trajectory
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _trajectory (let (r) (dotimes (i n) (push (instance lab4_starter::msg_type_position :init) r)) r))
     (dolist (elem- _trajectory)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get lab4_starter::msg_type_trajectory :md5sum-) "7fe035463acb6da30cda877f198c818b")
(setf (get lab4_starter::msg_type_trajectory :datatype-) "lab4_starter/msg_type_trajectory")
(setf (get lab4_starter::msg_type_trajectory :definition-)
      "msg_type_position[] trajectory
================================================================================
MSG: lab4_starter/msg_type_position
float64[2] position

")



(provide :lab4_starter/msg_type_trajectory "7fe035463acb6da30cda877f198c818b")


