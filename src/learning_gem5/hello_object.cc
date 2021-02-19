#include "learning_gem5/hello_object.hh"

#include "base/trace.hh"
#include "debug/Hello.hh"

HelloObject:: HelloObject(HelloObjectParams * params) :
    SimObject(params)
{
    DPRINTF(Hello, "Create the hello object\n");
}

HelloObject*
HelloObjectParams::create()
{
    return new HelloObject(this);
}
