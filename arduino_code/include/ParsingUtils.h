#ifndef MY_FUNCTIONS_H
#define MY_FUNCTIONS_H

#include <Arduino.h>

extern boolean newData;
extern char receivedChars[];
extern char tempChars[];


void recvWithStartEndMarkers();
void parseData();
void showParsedData();

#endif // MY_FUNCTIONS_H
