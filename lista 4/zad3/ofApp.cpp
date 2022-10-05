#include "ofApp.h"
#include "ofConstants.h"

void ofApp::setup()
{
    srand(time(NULL));
    
    shader.setupShaderFromFile(GL_COMPUTE_SHADER, "computeShader.cs");
    shader.linkProgram();

    tekstura.allocate(W, H, GL_RGBA32F);
    tekstura.bindAsImage(1, GL_WRITE_ONLY);

    // initialize
    for (int x = 0; x < W; x++)
        for (int y = 0; y < H; y++)
        {
            int idx = x + y * W;
            if (rand() / float(RAND_MAX) < 0.3) A1cpu[idx] = 1.0;
        }

    A1.allocate(W * H * sizeof(float), A1cpu, GL_DYNAMIC_DRAW);
    A1.bindBase(GL_SHADER_STORAGE_BUFFER, 0);
}

void ofApp::update()
{
    shader.begin();
    shader.dispatchCompute(W / 20, H / 20, 1);
    shader.end();
}

void ofApp::draw()
{
    tekstura.draw(0, 0);
}