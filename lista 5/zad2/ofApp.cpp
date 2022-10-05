#include "ofApp.h"
#include "ofConstants.h"

void ofApp::setup()
{
    srand(time(NULL));
    shader.setupShaderFromFile(GL_COMPUTE_SHADER, "computeShader.cs");
    shader.linkProgram();

    tekstura.allocate(W, H, GL_RGBA32F);
    tekstura.bindAsImage(2, GL_WRITE_ONLY);

    // initialize
    for (int x = 0; x < W; x++)
        for (int y = 0; y < H; y++)
        {
            int idx = x + y * W;
            if (rand() / float(RAND_MAX) < 0.5)
            {
                A1cpu[idx] = 1.0;
                A2cpu[idx] = 1.0;
            }
            else
            {
                A1cpu[idx] = 0.0;
                A2cpu[idx] = 0.0;
            }
        }

    A1.allocate(W * H * sizeof(float), A1cpu, GL_STATIC_DRAW);
    A2.allocate(W * H * sizeof(float), A2cpu, GL_STATIC_DRAW);
    A1.bindBase(GL_SHADER_STORAGE_BUFFER, 0);
    A2.bindBase(GL_SHADER_STORAGE_BUFFER, 1);
}

void ofApp::update()
{
    static int c = 1;
    c = 1 - c;
    A1.bindBase(GL_SHADER_STORAGE_BUFFER, 0 + c);
    A2.bindBase(GL_SHADER_STORAGE_BUFFER, 0 + 1 - c);
    
    shader.begin();
    shader.dispatchCompute(W / 20, H / 20, 1);
    shader.end();
}

void ofApp::draw()
{
    tekstura.draw(0, 0);
}