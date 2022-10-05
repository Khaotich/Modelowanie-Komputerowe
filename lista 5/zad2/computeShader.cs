#version 460

layout(binding = 0) buffer dcA1 { float A1 []; };
layout(binding = 1) buffer dcA2 { float A2 []; };
layout(rgba32f, binding = 2) uniform writeonly image2D img;
layout(local_size_x = 20, local_size_y = 20, local_size_z = 1) in;

const int W = 1280;
const int H = 720;

void main()
{
    int i = int(gl_GlobalInvocationID.x);
    int j = int(gl_GlobalInvocationID.y);
    int idx = i + j * W;

    int sum = 0;

    for (int x = -5; x <= 5; ++x)
        for (int y = -5; y <= 5; ++y)
        {
            if (x == 0 && y == 0) continue;
            int xy = (i + x) + (j + y) * W;
            if (A1[xy] == 1) sum += 1;
        }

    if (sum >= 34 && sum <= 58 && A1[idx] == 1) A2[idx] = 1;
    else if (sum >= 34 && sum <= 45) A2[idx] = 1;
    else A2[idx] = 0;

    vec4 col = vec4(vec3(A2[idx]), 1);
    imageStore(img, ivec2(gl_GlobalInvocationID.xy), col);
}