#include <iostream>

#include "jni.h"
#include <JniInvocation.h>

int main()
{
    JavaVM* jvm;
    JNIEnv* env;

    JniInvocation* invocation = new JniInvocation();
    bool succ = invocation->Init(nullptr);

    jint ret = JNI_CreateJavaVM(&jvm, (JNIEnv**)&jvm, NULL);

    delete invocation;

    return 0;
}
