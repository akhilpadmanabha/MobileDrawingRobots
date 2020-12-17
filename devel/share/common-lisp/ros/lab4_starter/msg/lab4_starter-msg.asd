
(cl:in-package :asdf)

(defsystem "lab4_starter-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "msg_type_position" :depends-on ("_package_msg_type_position"))
    (:file "_package_msg_type_position" :depends-on ("_package"))
    (:file "msg_type_trajectory" :depends-on ("_package_msg_type_trajectory"))
    (:file "_package_msg_type_trajectory" :depends-on ("_package"))
  ))