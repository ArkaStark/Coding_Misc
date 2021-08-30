from PIL import Image
import os

keras.applications.inception_resnet_v2.InceptionResNetV2(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)

CONTENT_LOC = ''
STYLE_LOC = ''
WEIGHTS = []
BIAS = []

C = Image.open(CONTENT_LOC, 'r')
S = Image.open(STYLE_LOC, 'r')
w,h = C.size
G = Image.new("RGBA", (w,h))

# Calculating the Content Cost :
CONTENT_LAYER = 1
aC = C*WEIGHTS[1]
for i in range(1, CONTENT_LAYER):
    aC *= WEIGHTS[CONTENT_LAYER]

