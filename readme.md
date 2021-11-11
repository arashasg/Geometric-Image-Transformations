# Geometric-Image-Transformations
## Rotate Picture(Affine Transform.py
We can rotate an image around an arbitrary point c = (cx, cy) by adding a proper translation vector.
This can be done by translating any point with the translation − c (so that c moves to
the origin), rotating around the origin, and translating back with the translation vector
+ c. The transformation then becomes x′ = R(x − c) + c = R x + (c − Rc).
### output:
<p float="left" align="center">
  <img src="https://github.com/arashasg/Geometric-Image-Transformations/blob/master/Images/output.gif"  width="350 height="350px"/>
</p>

## Homography Transform(Perspective Correction.py)
Look at the following traffic sign. In this part, We wanted to correct
the perspective and extract the sign plate as if we
are looking at it from the front. We had already
found the coordinates of the four corners of the sign
plate and stored them.
### Input:
<p float="left" align="center">
  <img src="https://github.com/arashasg/Geometric-Image-Transformations/blob/master/Images/Input.PNG"  width="350px" height="350px"/>
</p>

### Output:
<p float="left" align="center">
  <img src="https://github.com/arashasg/Geometric-Image-Transformations/blob/master/Images/Output.PNG"  width="550px" height="350px"/>
</p>