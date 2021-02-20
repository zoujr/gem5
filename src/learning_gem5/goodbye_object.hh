#ifndef __LEARNING_GEM5_GOODBYE_OBJECT_HH__
#define __LEARNING_GEM5_GOODBYE_OBJECT_HH__

#include "params/GoodbyeObject.hh"
#include "sim/sim_object.hh"

class GoodbyeObject : public SimObject
{
    private:
        void processEvent();

        void fillBuffer();

        EventWrapper<GoodbyeObject, &GoodbyeObject::processEvent> event;

        float bandwidth;

        int bufferSize;

        char *buffer;

        std::string message;

        int bufferUsed;

    public:
        GoodbyeObject(GoodbyeObjectParams *p);
        ~GoodbyeObject();

        void sayGoodbye(std::string other_name);
};

#endif // __LEARNING_GEM5_GOODBYE_OBJECT_HH__
