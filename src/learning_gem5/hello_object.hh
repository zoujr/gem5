#ifndef __LEARNING_GEM5_HELLO_OBEJCT_HH__
#define __LEARNING_GEM5_HELLO_OBEJCT_HH__

#include "learning_gem5/goodbye_object.hh"
#include "params/HelloObject.hh"
#include "sim/sim_object.hh"

class HelloObject : public SimObject
{
    private:
        void processEvent();

        EventFunctionWrapper event;

        GoodbyeObject* goodbye;

        const std::string myName;

        const Tick latency;

        int timesLeft;

    public:
        HelloObject(HelloObjectParams *p);

        void startup();
};

#endif // __LEARNING_GEM5_HELLO_OBEJCT_HH__
