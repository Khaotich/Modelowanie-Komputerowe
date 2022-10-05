#include "ofApp.h"
#include "ofConstants.h"

#define W 1280
#define H 720

void ofApp::setup()
{
	shader.setupShaderFromFile(GL_COMPUTE_SHADER, "computeShader.cs");
	shader.linkProgram();

	texture.allocate(W, H, GL_RGBA32F);
	texture.bindAsImage(1, GL_WRITE_ONLY);

	A1.allocate(W * H * sizeof(float), A1cpu, GL_STATIC_DRAW);
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
	texture.draw(0, 0);
}