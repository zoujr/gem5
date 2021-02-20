#include "learning_gem5/hello_object.hh"

#include "base/trace.hh"
#include "debug/Hello.hh"

HelloObject::HelloObject(HelloObjectParams * params) :
    SimObject(params),
    event([this]{processEvent();}, name()),
    goodbye(params->goodbye_object),
    latency(params->time_to_wait),
    timesLeft(params->number_of_fires),
    myName(params->name)
{
    DPRINTF(Hello, "Created the hello object\n");
    panic_if(!goodbye, "HelloObject must have a non-null GoodbyeObject");
}

HelloObject*
HelloObjectParams::create()
{
    return new HelloObject(this);
}

void
HelloObject::processEvent()
{
    timesLeft--;
    DPRINTF(Hello, "Hello world! Processing the event! %d left\n", timesLeft);

    if (timesLeft <= 0) {
        DPRINTF(Hello, "Done firing!\n");

        goodbye->sayGoodbye(myName);
    } else {
        schedule(event, curTick() + latency);
    }
}

void
HelloObject::startup()
{
    schedule(event, latency);
}
