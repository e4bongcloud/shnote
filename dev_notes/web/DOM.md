# 문서 객체 모델(Document Objects Model, DOM)
* 문서 객체 모델은 HTML, XML 문서의 프로그래밍 인터페이스
* 이 객체 모델은 문서 내의 모든 요소를 정의하고, 각각의 요소에 접근하는 방법을 제공
* 웹 페이지는 일종의 문서(document)로서 웹 브라우저를 통해 내용이 해석되어 화면에 나타남


# DOMContentLoaded 이벤트
* DOMContentLoaded 이벤트는 웹 브라우저가 문서 객체를 모두 읽고 나서 실행하는 이벤트
* 다음과 같이 코드를 구성하면 DOMContentLoaded 상태가 되었을 때 콜백 함수를 호출

``` html
<!DOCTYPE html>
<html>
<head>
<title>DOMContentLoaded</title>
<script>
// DOMContentLoaded 이벤트를 연결합니다.
document.addEventListener('DOMContentLoaded', () => {
const h1 = (text) => `<h1>${text}</h1>`
document.body.innerHTML += h1('DOMContentLoaded 이벤트 발생')
})
</script>
</head>
<body>

</body>
</html>
```
#  요약
* DOMContentLoaded 이벤트는 HTML 페이지의 모든 문서 객체(요소)를 웹 브라우저가 읽어들였을 때 발생시키는 이벤트
* querySelector() 메소드는 문서 객체를 선택할 때 사용하는 메소드
* textContent 속성과 innerHTML 속성은 문서 객체 내부의 글자를 조작할 때 사용하는 속성
* style 속성은 문서 객체의 스타일을 조작할 때 사용하는 속성
* 이벤트 리스너(이벤트 핸들러)는 이벤트가 발생할 때 실행하는 함수를 의미