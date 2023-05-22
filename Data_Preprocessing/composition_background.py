from wand.image import Image
import os

img_list = os.listdir('image\img\one')
print(img_list)

#워터마크로 사용할 이미지
w_mark = Image(filename ='image\image2\반원\emovebg-previeww6.png')
w_mark.sample(250,250)

#실질적으로 워터마크를 넣는 코드
#사용할 이미지 파일을 img에 저장

for filename in img_list:
    print("현재 처리하는 이미지",filename)
    img = Image(filename = 'image\img\one/' + filename)

    #워터마크 적용 함수 watermark
    img.watermark(image=w_mark, transparency=0.0, left=100, top=100)
    img.save(filename='image\image2\watermark_image\ew6' + filename)

#img_list = os.listdir('image\image2\원본\est1.jpg')
