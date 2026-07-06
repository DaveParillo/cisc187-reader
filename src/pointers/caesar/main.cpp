
#include "caesar.h"
#include "help.h"

#include <cstring>    // strcmp
#include <iostream>
#include <string>

int main(int argc, char** argv) {
    // Define a default a 'character handler'
    // the variable 'handler' provides an option to 
    // change the encryption function at runtime
    transform handler = rot13;

    // loop on command line argumenats
    // call help and exit or
    // use of the 2 transforms
    // or reject the input and exit
    for (int i=1; i < argc; ++i) {
        if (!std::strcmp(argv[i], "-h")) {
            help(*argv);
        } else if (!std::strcmp(argv[i], "-l")) {
            handler = rot13;
        } else if (!std::strcmp(argv[i], "-f")) {
            handler = rot47;
        } else {
            usage(*argv);
            exit(-1);
        }
    }

    std::string message;
    while (getline(std::cin, message)) {
        render_text(message, handler);
    }
    return 0;
}


