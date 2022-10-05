#version 460

layout(binding = 0) buffer dcA1 { float A1 []; };
layout(rgba32f, binding = 1) uniform writeonly image2D img;
layout(local_size_x = 20, local_size_y = 20, local_size_z = 1) in;

const int W = 1280;
const int H = 720;

void main()
{
    int i = int(gl_GlobalInvocationID.x);
    int j = int(gl_GlobalInvocationID.y);

    int idx = i + j *W;
    A1[idx] = (sqrt(pow(640 - i, 2) + pow(360 - j, 2))) * 0.001;

    vec4 col = vec4(vec3(A1[idx]), 1);
    imageStore(img, ivec2(gl_GlobalInvocationID.xy), col);
}