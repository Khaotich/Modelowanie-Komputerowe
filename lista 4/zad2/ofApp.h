#pragma once
#include "ofMain.h"

#define W 1280
#define H 720

class ofApp : public ofBaseApp
{
public:
    void setup();
    void update();
    void draw();

    ofBufferObject A1, B1, A2, B2;
    ofTexture tekstura;
    ofShader shader;

    float A1cpu[W * H];
    float A2cpu[W * H];
    float B1cpu[W * H];
    float B2cpu[W * H];
};