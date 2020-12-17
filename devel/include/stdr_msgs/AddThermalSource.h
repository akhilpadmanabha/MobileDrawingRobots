// Generated by gencpp from file stdr_msgs/AddThermalSource.msg
// DO NOT EDIT!


#ifndef STDR_MSGS_MESSAGE_ADDTHERMALSOURCE_H
#define STDR_MSGS_MESSAGE_ADDTHERMALSOURCE_H

#include <ros/service_traits.h>


#include <stdr_msgs/AddThermalSourceRequest.h>
#include <stdr_msgs/AddThermalSourceResponse.h>


namespace stdr_msgs
{

struct AddThermalSource
{

typedef AddThermalSourceRequest Request;
typedef AddThermalSourceResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AddThermalSource
} // namespace stdr_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::stdr_msgs::AddThermalSource > {
  static const char* value()
  {
    return "9fd17d9c0c1371182c625b3bfbbcf75f";
  }

  static const char* value(const ::stdr_msgs::AddThermalSource&) { return value(); }
};

template<>
struct DataType< ::stdr_msgs::AddThermalSource > {
  static const char* value()
  {
    return "stdr_msgs/AddThermalSource";
  }

  static const char* value(const ::stdr_msgs::AddThermalSource&) { return value(); }
};


// service_traits::MD5Sum< ::stdr_msgs::AddThermalSourceRequest> should match 
// service_traits::MD5Sum< ::stdr_msgs::AddThermalSource > 
template<>
struct MD5Sum< ::stdr_msgs::AddThermalSourceRequest>
{
  static const char* value()
  {
    return MD5Sum< ::stdr_msgs::AddThermalSource >::value();
  }
  static const char* value(const ::stdr_msgs::AddThermalSourceRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::stdr_msgs::AddThermalSourceRequest> should match 
// service_traits::DataType< ::stdr_msgs::AddThermalSource > 
template<>
struct DataType< ::stdr_msgs::AddThermalSourceRequest>
{
  static const char* value()
  {
    return DataType< ::stdr_msgs::AddThermalSource >::value();
  }
  static const char* value(const ::stdr_msgs::AddThermalSourceRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::stdr_msgs::AddThermalSourceResponse> should match 
// service_traits::MD5Sum< ::stdr_msgs::AddThermalSource > 
template<>
struct MD5Sum< ::stdr_msgs::AddThermalSourceResponse>
{
  static const char* value()
  {
    return MD5Sum< ::stdr_msgs::AddThermalSource >::value();
  }
  static const char* value(const ::stdr_msgs::AddThermalSourceResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::stdr_msgs::AddThermalSourceResponse> should match 
// service_traits::DataType< ::stdr_msgs::AddThermalSource > 
template<>
struct DataType< ::stdr_msgs::AddThermalSourceResponse>
{
  static const char* value()
  {
    return DataType< ::stdr_msgs::AddThermalSource >::value();
  }
  static const char* value(const ::stdr_msgs::AddThermalSourceResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // STDR_MSGS_MESSAGE_ADDTHERMALSOURCE_H
