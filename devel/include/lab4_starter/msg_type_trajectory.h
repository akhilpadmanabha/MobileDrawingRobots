// Generated by gencpp from file lab4_starter/msg_type_trajectory.msg
// DO NOT EDIT!


#ifndef LAB4_STARTER_MESSAGE_MSG_TYPE_TRAJECTORY_H
#define LAB4_STARTER_MESSAGE_MSG_TYPE_TRAJECTORY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <lab4_starter/msg_type_position.h>

namespace lab4_starter
{
template <class ContainerAllocator>
struct msg_type_trajectory_
{
  typedef msg_type_trajectory_<ContainerAllocator> Type;

  msg_type_trajectory_()
    : trajectory()  {
    }
  msg_type_trajectory_(const ContainerAllocator& _alloc)
    : trajectory(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector< ::lab4_starter::msg_type_position_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::lab4_starter::msg_type_position_<ContainerAllocator> >::other >  _trajectory_type;
  _trajectory_type trajectory;





  typedef boost::shared_ptr< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> const> ConstPtr;

}; // struct msg_type_trajectory_

typedef ::lab4_starter::msg_type_trajectory_<std::allocator<void> > msg_type_trajectory;

typedef boost::shared_ptr< ::lab4_starter::msg_type_trajectory > msg_type_trajectoryPtr;
typedef boost::shared_ptr< ::lab4_starter::msg_type_trajectory const> msg_type_trajectoryConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::lab4_starter::msg_type_trajectory_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace lab4_starter

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'lab4_starter': ['/home/akhil/ros_workspaces/project/src/lab4_starter/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7fe035463acb6da30cda877f198c818b";
  }

  static const char* value(const ::lab4_starter::msg_type_trajectory_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7fe035463acb6da3ULL;
  static const uint64_t static_value2 = 0x0cda877f198c818bULL;
};

template<class ContainerAllocator>
struct DataType< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> >
{
  static const char* value()
  {
    return "lab4_starter/msg_type_trajectory";
  }

  static const char* value(const ::lab4_starter::msg_type_trajectory_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> >
{
  static const char* value()
  {
    return "msg_type_position[] trajectory\n\
================================================================================\n\
MSG: lab4_starter/msg_type_position\n\
float64[2] position\n\
";
  }

  static const char* value(const ::lab4_starter::msg_type_trajectory_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.trajectory);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct msg_type_trajectory_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::lab4_starter::msg_type_trajectory_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::lab4_starter::msg_type_trajectory_<ContainerAllocator>& v)
  {
    s << indent << "trajectory[]" << std::endl;
    for (size_t i = 0; i < v.trajectory.size(); ++i)
    {
      s << indent << "  trajectory[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::lab4_starter::msg_type_position_<ContainerAllocator> >::stream(s, indent + "    ", v.trajectory[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // LAB4_STARTER_MESSAGE_MSG_TYPE_TRAJECTORY_H
