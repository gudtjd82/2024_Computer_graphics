#!/usr/bin/env python3
# -*- coding: utf-8 -*
# sample_python aims to allow seamless integration with lua.
# see examples below

import os
import sys
import pdb  # use pdb.set_trace() for debugging
import code # or use code.interact(local=dict(globals(), **locals()))  for debugging.
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image 
from ray import *

class Color:
    def __init__(self, R, G, B):
        self.color=np.array([R,G,B]).astype(np.float64)

    # Gamma corrects this color.
    # @param gamma the gamma value to use (2.2 is generally used).
    def gammaCorrect(self, gamma):
        inverseGamma = 1.0 / gamma;
        self.color=np.power(self.color, inverseGamma)

    def toUINT8(self):
        return (np.clip(self.color, 0,1)*255).astype(np.uint8)

class Shader:
    def __init__(self, name, s_type, diffuseColor):
        self.name = name
        self.s_type = s_type
        self.diffuseColor = diffuseColor

    def print_shader(self):
        print("name:", self.name)
        print("type:", self.s_type)
        print("diffuseColor:", self.diffuseColor)
    
    def get_name(self):
        return self.name

class Lambertian(Shader):
    def __init__(self, name, s_type, diffuseColor):
        super().__init__(name, s_type, diffuseColor)

class Phong(Shader):
    def __init__(self, name, s_type, diffuseColor, specularColor, exp):
        super().__init__(name, s_type, diffuseColor)
        self.specularColor = specularColor
        self.exp = exp
    
    def print_shader(self):
        super().print_shader()
        print("sepcularColor:", self.specularColor)
        print("exponent:", self.exp)

class Sphere:
    def __init__(self, center, radius, shader):
        self.center = center
        self.radius = radius
        self.shader = shader
    
    def get_normal(self, point):
        dir = point - self.center  
        return (dir / np.linalg.norm(dir))

    def print_Sphere(self):
        print("Shape: Sphere")
        print("center pos:", self.center)
        print("radius:", self.radius)
        print("=====shader=====")
        if self.shader is not None:
            self.shader.print_shader()

class Light:
    def __init__(self, pos, intensity):
        self.pos = pos
        self.intensity = intensity

    def print_light(self):
        print("=======light=======")
        print("position:", self.pos)
        print("intesity:", self.intensity)
        print("===================")

def main():

    tree = ET.parse(sys.argv[1])
    root = tree.getroot()

    # set default values
    viewDir=np.array([0,0,-1]).astype(np.float64)
    viewUp=np.array([0,1,0]).astype(np.float64)
    viewProjNormal=-1*viewDir  # you can safely assume this. (no examples will use shifted perspective camera)
    viewWidth=1.0
    viewHeight=1.0
    projDistance=1.0
    intensity=np.array([1,1,1]).astype(np.float64)  # how bright the light is.
    Shaders = []    # class Shader array
    Spheres = []    # class Shpere array
    lights = []     # class light array
    print(np.cross(viewDir, viewUp))

    # image size
    imgSize=np.array(root.findtext('image').split()).astype(np.int32)

    # camera
    for c in root.findall('camera'):
        viewPoint=np.array(c.findtext('viewPoint').split()).astype(np.float64)
        viewDir=np.array(c.findtext('viewDir').split()).astype(np.float64)
        viewProjNormal=np.array(c.findtext('projNormal').split()).astype(np.float64)
        viewUp=np.array(c.findtext('viewUp').split()).astype(np.float64)

        if c.findtext('projDistance') is not None:
            projDistance=float(c.findtext('projDistance'))

        viewWidth=float(c.findtext('viewWidth'))
        viewHeight=float(c.findtext('viewHeight'))
        print('viewpoint', viewPoint)
        print('viewDir', viewDir)
        print('viewProjNormal', viewProjNormal)
        print('viewUp', viewUp)
        print('projDistance', projDistance)
        print('viewWidth', viewWidth)
        print('viewHeight', viewHeight)

    # shader
    for c in root.findall('shader'):
        s_name = c.get('name')
        s_type = c.get('type')
        diffuseColor_c=np.array(c.findtext('diffuseColor').split()).astype(np.float64)

        if s_type == 'Lambertian':
            Shaders.append(Lambertian(s_name, s_type, diffuseColor_c))
        elif s_type == 'Phong':
            specularColor_c=np.array(c.findtext('specularColor').split()).astype(np.float64)
            exponent_c = np.array(c.findtext('exponent').split())[0].astype(np.float64)
            Shaders.append(Phong(s_name, s_type, diffuseColor_c, specularColor_c, exponent_c))

    # surface
    for c in root.findall('surface'):
        surface_type = c.get('type')
        surface_shader = None
        for s in c.findall('shader'):
            s_ref = s.get('ref')
            if s_ref == None:
                s_type = s.get('type')
                diffuseColor_c=np.array(s.findtext('diffuseColor').split()).astype(np.float64)

                if s_type == 'Lambertian':
                    surface_shader = Lambertian(s_name, s_type, diffuseColor_c)
                elif s_type == 'Phong':
                    specularColor_c=np.array(s.findtext('specularColor').split()).astype(np.float64)
                    exponent_c = np.array(s.findtext('exponent').split())[0].astype(np.float64)
                    surface_shader = Phong(s_name, s_type, diffuseColor_c, specularColor_c, exponent_c)
            else:
                for shader in Shaders:
                    if shader.get_name() == s_ref:
                        surface_shader = shader
                        # pdb.set_trace()
                        break
        if surface_type == 'Sphere':
            center_pos = np.array(c.findtext('center').split()).astype(np.float64)
            radius=float(c.findtext('radius'))

            Spheres.append(Sphere(center_pos, radius, surface_shader))

    # light
    for c in root.findall('light'):
        pos = np.array(c.findtext('position').split()).astype(np.float64)
        intensity = np.array(c.findtext('intensity').split()).astype(np.float64)

        lights.append(Light(pos, intensity))

    i = 0
    for sphere in Spheres:
        print("===============", i+1, "번째===============")
        sphere.print_Sphere()
        print("===================================")
        i += 1
    
    for light in lights:
        light.print_light()

    #code.interact(local=dict(globals(), **locals()))  

    # Create an empty image
    channels=3
    img = np.zeros((imgSize[1], imgSize[0], channels), dtype=np.uint8)
    img[:,:]=0
    
    # 각 픽셀에 대해 레이를 쏘고 구체와의 교차를 검사
    for y in range(imgSize[1]):
        for x in range(imgSize[0]):
            # 픽셀 위치를 이미지 공간의 위치로 변환 (NDC로 변환)
            # pixel-to-image mapping
            pixel_ndc = np.array([x / imgSize[0], y / imgSize[1]])  # 범위: [0, 1]
            pixel_ndc = pixel_ndc * 2.0 - 1.0                       # 범위: [-1, 1]

            pixel_camera = np.array([pixel_ndc[0] * viewWidth, pixel_ndc[1] * viewHeight, -projDistance])

            # camera axis
            forward_vec = viewDir / np.linalg.norm(viewDir)
            right_vec = np.cross(forward_vec, viewUp)
            up_vec = np.cross(right_vec, forward_vec)

            forward_vec = np.array([[forward_vec[0]], [forward_vec[1]], [forward_vec[2]]])
            right_vec = np.array([[right_vec[0]], [right_vec[1]], [right_vec[2]]])
            up_vec = np.array([[up_vec[0]], [up_vec[1]], [up_vec[2]]])

            # rotation matrix
            R = np.identity(4)
            R[:3, :3] = np.hstack((right_vec, -up_vec, -forward_vec))

            # translate matrix
            T = np.identity(4)
            T[:3, 3] = np.array(viewPoint)

            transformation = T@R

            pixel_camera = transformation @ np.array([pixel_camera[0],pixel_camera[1],pixel_camera[2], 1])
            pixel_camera = pixel_camera[:3]

            # ray_dircection 정규화
            ray_direction = pixel_camera - viewPoint
            ray_direction /= np.linalg.norm(ray_direction)

            hit = False                
            hit_color = np.array([0., 0., 0.], dtype=np.float64)  # 교차가 없을 경우 사용할 기본 색상
            best_t = float('inf')
            best_sphere = None
            best_surface_point = None

            for sphere in Spheres:
                hit, t, surface_point = intersect_ray_sphere(viewPoint, ray_direction, sphere)
                if hit and t < best_t:
                    best_t = t
                    best_sphere = sphere
                    best_surface_point = surface_point
            
            if best_sphere is not None:
                surface_normal = best_sphere.get_normal(best_surface_point)
                L = np.array([0., 0., 0.], dtype=np.float64)
                for light in lights:
                    # shadow
                    blocked = False
                    light_dir = best_surface_point - light.pos
                    _, best_t, _ = intersect_ray_sphere(light.pos, light_dir, best_sphere)
                    for sphere in Spheres:
                        if sphere != best_sphere:
                            hit, t, surface_point = intersect_ray_sphere(light.pos, light_dir, sphere)
                        if hit and t < best_t:  # blocked
                            L = np.array([0., 0., 0.])
                            blocked = True
                            break
                    
                    if not blocked:
                        l = light.pos - best_surface_point
                        l = l / np.linalg.norm(l)

                        # shading
                        if best_sphere.shader is not None:
                            # Lambertian
                            if best_sphere.shader.s_type == 'Lambertian':
                                L += best_sphere.shader.diffuseColor * light.intensity * max(0, np.dot(surface_normal, l))
                                # if best_sphere.shader.name == "blue":
                                #     print(L)
                                #     pdb.set_trace()
                            elif best_sphere.shader.s_type == 'Phong':
                                L += best_sphere.shader.diffuseColor * light.intensity * max(0, np.dot(surface_normal, l))

                                v = -ray_direction
                                h = (v+l) / np.linalg.norm(v+l)
                                cos = max(0, np.dot(surface_normal, h))
                                p = best_sphere.shader.exp
                                L += best_sphere.shader.specularColor * light.intensity * (cos**p)

                                L = np.clip(L, 0, 1)

                hit_color = L  # 교차 발생시 구체의 색상을 사용

            img[y][x] = (hit_color * 255).astype(np.uint8)  # 색상을 이미지에 적용


    rawimg = Image.fromarray(img, 'RGB')
    #rawimg.save('out.png')
    rawimg.save(sys.argv[1]+'_test.png')
    
if __name__=="__main__":
    main()
