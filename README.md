# Fake NEXT Checker & Renamer

* 간단하게 만든 스크립트입니다. 
* Python 으로 제작되었습니다.



## How-to

- python ./check_fake.py /Downloads/
- 하위 폴더의 -NEXT.mp4 파일 리스트를 각각 ffmpeg -i 를 이용하여 체크합니다.
- NEXT 릴에는 MH ENCODER 문구가 포함되는데 이를 확인하여 체크를 진행합니다.
- ![](https://i.imgur.com/Nqk34FT.png)
- NEXT 릴이 아닌데, 파일명에 -NEXT 문구가 포함이 되어 있다면 -NEXT 문구를 제거합니다.



## Video

[![Video Label](https://img.youtube.com/vi/zww4gcSC5oQ/maxresdefault.jpg)](https://youtu.be/zww4gcSC5oQ?t=0s)



![](https://i.imgur.com/CY61c4i.png)



Fake 로 체크가 되면, 파일 명에서 -NEXT는 제거됩니다.





마지막 업데이트 : 2019-05-10 (목) 