# drewImage()로 이미지 그리기 사례

- (20, 20) 위치에 원본 크기로 그리기

        var img = new Image();

        img.onload = function() {

            context.drawImage(img, 20, 20);

        } 

        img.src = "text.png";


-