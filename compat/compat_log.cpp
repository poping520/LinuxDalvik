#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <stdio.h>

#include <sys/types.h>
#include <sys/stat.h>

#include <android/log.h>

#ifdef __cplusplus
extern "C" {
#endif

#define LOG_BUF_SIZE	1024

    int __android_log_write(int prio, const char *tag, const char *msg) {
        printf("%d %s: %s\n", prio, tag, msg);
        return 0;
    }

    int __android_log_buf_write(int bufID, int prio, const char *tag, const char *msg) {
        printf("%d %s: %s\n", prio, tag, msg);
        return 0;
    }

    int __android_log_print(int prio, const char* tag, const char* fmt, ...) {
        va_list ap;
        char buf[LOG_BUF_SIZE];

        va_start(ap, fmt);
        vsnprintf(buf, LOG_BUF_SIZE, fmt, ap);
        va_end(ap);

        return __android_log_write(prio, tag, buf);
    }

    int __android_log_btwrite(int32_t tag, char type, const void* payload, size_t len) {
        return 0;
    }

    int __android_log_vprint(int prio, const char* tag, const char* fmt, va_list ap) {
        char buf[LOG_BUF_SIZE];

        vsnprintf(buf, LOG_BUF_SIZE, fmt, ap);

        return __android_log_write(prio, tag, buf);
    }

    void __android_log_assert(const char* cond, const char* tag, const char* fmt, ...) {
        char buf[LOG_BUF_SIZE];

        if (fmt) {
            va_list ap;
            va_start(ap, fmt);
            vsnprintf(buf, LOG_BUF_SIZE, fmt, ap);
            va_end(ap);
        } else {
            /* Msg not provided, log condition.  N.B. Do not use cond directly as
             * format string as it could contain spurious '%' syntax (e.g.
             * "%d" in "blocks%devs == 0").
             */
            if (cond)
                snprintf(buf, LOG_BUF_SIZE, "Assertion failed: %s", cond);
            else
                strcpy(buf, "Unspecified assertion failed");
        }

        __android_log_write(ANDROID_LOG_FATAL, tag, buf);

        __builtin_trap(); /* trap so we have a chance to debug the situation */
    }

    int __android_log_buf_print(int bufID, int prio, const char *tag, const char *fmt, ...) {
        va_list ap;
        char buf[LOG_BUF_SIZE];

        va_start(ap, fmt);
        vsnprintf(buf, LOG_BUF_SIZE, fmt, ap);
        va_end(ap);

        return __android_log_buf_write(bufID, prio, tag, buf);
    }

#ifdef __cplusplus
}
#endif



