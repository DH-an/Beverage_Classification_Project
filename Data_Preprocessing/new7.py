from wand.image import Image
import os

img_list = os.listdir('image\img\one')
print(img_list)


#워터마크로 사용할 이미지
w_mark = Image(filename ='image\image2\반원\emovebg-preview2.png')
w_mark.sample(200,200)

for filename in img_list:
    #사용할 이미지 파일을 img에 저장
    img = Image(filename = 'image\img\one\ea8.jpg')

    #워터마크 적용 함수 watermark
    img.watermark(image=w_mark, transparency=0.0, left=100, top=100)
    img.save(filename='image\image2\watermark_image\ew_test38.jpg')
