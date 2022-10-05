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
    int idx = i + j * W;

    int dx1 = (i - 1) + (j - 1) * W;
    int dx2 = i + (j - 1) * W;
    int dx3 = (i + 1) + (j - 1) * W;
    int dx4 = (i + 1) + j * W;
    int dx5 = (i + 1) + (j + 1) * W;
    int dx6 = i + (j + 1) * W;
    int dx7 = (i - 1) + (j + 1) * W;
    int dx8 = (i - 1) + j * W;

    int sum = int(A1[dx1]) + int(A1[dx2]) + int(A1[dx3]) + int(A1[dx4]) + int(A1[dx5]) + int(A1[dx6]) + int(A1[dx7]) + int(A1[dx8]);
    
    if(A1[idx] == 0 && sum == 3) A1[idx] = 1;
    if((A1[idx] == 1 && sum > 3) || (A1[idx] == 1 && sum < 2)) A1[idx] = 0;

    vec4 col = vec4(vec3(A1[idx]), 1);
    imageStore(img, ivec2(gl_GlobalInvocationID.xy), col);
}