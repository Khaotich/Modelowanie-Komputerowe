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

    ofShader shader;
    ofBufferObject A1;
    ofTexture texture;

    float A1cpu[W * H] = { 0 };
};