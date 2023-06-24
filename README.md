<p align="center">
  <img src="https://www.solvetic.com/uploads/monthly_01_2016/tutorials-1415-0-60642300-1452279191.jpg" alt="This is an alt text.">
</p>


<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://static.eldinamo.cl/media/2021/08/falabella.jpg" width="400" alt="Laravel Logo"></a></p>

<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/7/7a/Logo_Ripley.svg" width="400" alt="Laravel Logo"></a></p>

<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/b/b2/Logo_Paris_Cencosud.png" width="400" alt="Laravel Logo"></a></p>


<p align="center">
<a href="https://travis-ci.org/laravel/framework"><img src="https://travis-ci.org/laravel/framework.svg" alt="Build Status"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/v/laravel/framework" alt="Latest Stable Version"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/l/laravel/framework" alt="License"></a>
</p>

##  Bot that converts WEBP images to JPG and resizes them
## Installation

clone  repo

```bash
git clone git@github.com:Taoista/webp_to_jpg.git
```
enter the project
```bash
cd webp_to_jpg
```

Recommendation (install virtualenv optional)
```bash
pip install virtualenv
```
Install package
```bash
pip install -r requirements.txt
```
copy .env.example to .env
```bash
pip install -r requirements.txt
```

## Program Usage
```bash
python main.py
```
## Execution Blocks

> The first time it is executed, two folders will be created: one named 'inicio' where the images in JPG format are located, and the folder 'termino' where the transformed images in JPG format will be saved
>
>> On the second run of the program, you need to ensure that you have the images in WebP format in the 'inicio' folder. Execute the 'python main.py' command again.

## Notes
save image jpg
```docker
FOLDER /inicio
```
save image jpg
```docker
FOLDER /finish
```
size image inf file .env
```.env
IMG_WIDTH = 1500
IMG_HEIGHT = 1500
```
## Versions

| Left columns  | Right columns |
| ------------- |:-------------:|
| Python        | 3.10.7        |
| Pillow        | 9.5.0         |
| virtualenv    | 1.0.0         |
