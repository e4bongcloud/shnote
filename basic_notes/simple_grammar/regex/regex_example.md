# 전화

``` js
const str = '유선전화: 02-900-1234, 핸드폰: 010-2000-7777';
console.log(str.match(/\d{2,3}-\d{3,4}-\d{4}/g)); // ['02-900-1234', '010-2000-7777’]
```

# 이메일

``` js
const text = '이메일: test1@gmail.com';
console.log(text.match(/[\w\-\.]+\@[\w\-\.]+/g)); // [ 'test1@gmail.com' ]
```


``` js
const str = 'test1@gmail.com';
console.log(str.match(/\./gi));; // .(dot)은 정규식 내에서 특정 기능으로 활용되므로 앞에 \(백슬 래시)를 추가하여 검색함 
```


``` js
let str = 'We will, we will rock you';
console.log(str.match(/we/gi)); // We,we (패턴과 일치하는 부분 문자열 두 개를 담은 배열)
console.log(str.match(/we/i)); // We (패턴과 일치하는 부분 문자열 한 개를 담은 배열)
console.log(str.match(/my/i)); // null (패턴과 일치하는 부분 문자열이 없을 경우)
```

``` js
// 플래그 g 없음
console.log('We will, we will'.replace(/we/i, 'I')); // I will, we will
// 플래그 g 있음
console.log('We will, we will'.replace(/we/gi, 'I')); // I will, I will
```