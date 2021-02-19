#ifndef __LEARNING_GEM5_HELLO_OBEJCT_HH__
#define __LEARNING_GEM5_HELLO_OBEJCT_HH__

#include "params/HelloObject.hh"
#include "sim/sim_object.hh"

class HelloObject : public SimObject
{
    private:
        void processEvent();

        EventFunctionWrapper event;

        Tick latency;

        int timesLeft;

    public:
        HelloObject(HelloObjectParams *p);

        void startup();
};

#endif // __LEARNING_GEM5_HELLO_OBEJCT_HH__
