#include "ofMain.h"
#include "ofApp.h"

//========================================================================
int main()
{
	ofGLWindowSettings settings;
	settings.setGLVersion(4, 6);
	settings.setSize(1280, 720);
	settings.windowMode = OF_WINDOW;
	ofCreateWindow(settings);
	ofSetWindowTitle("Gray Scott Diffusion");

	ofRunApp(new ofApp());
}
