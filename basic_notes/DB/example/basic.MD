1. 직원 테이블에서 이름(name), 부서(department), 입사일(hire_date) 열을 조회하는 SQL문을 작성하시오.

2. 부서(department)별 평균 연봉(salary)을 조회하는 SQL문을 작성하시오.

3. 급여(salary)가 4000 이상인 직원들의 이름(name), 급여(salary), 입사일(hire_date)을 조회하는 SQL문을 작성하시오.

4. 직급(position)이 사원인 직원들의 이름(name), 직급(position), 부서(department)를 조회하는 SQL문을 작성하시오.

5. 부서(department)별 직원 수와 평균 연봉(salary)을 조회하는 SQL문을 작성하시오.

6. 급여(salary)가 3000 이하인 직원들의 부서(department)별 직원 수와 평균 연봉(salary)을 조회하는 SQL문을 작성하시오.

7. 직원 테이블에서 이름(name)이 '김철수'인 직원의 직급(position)과 입사일(hire_date)을 조회하는 SQL문을 작성하시오.

8. 직원 테이블에서 급여(salary)가 가장 높은 직원의 이름(name)과 급여(salary)를 조회하는 SQL문을 작성하시오.

9. 직원 테이블에서 직급(position)이 '대리'이고 부서(department)가 '영업부'인 직원들의 이름(name), 직급(position), 부서(department), 급여(salary)를 조회하는 SQL문을 작성하시오.

10. 부서별 최고 급여(salary)를 조회하는 SQL문을 작성하시오.







답



1.
``` sql
SELECT name, department, hire_date

FROM 직원;
```



2.
``` sql
SELECT department, AVG(salary) AS 평균연봉

FROM 직원

GROUP BY department;
```



3.
``` sql
SELECT name, salary, hire_date

FROM 직원

WHERE salary >= 4000;
```



4.
``` sql
SELECT name, position, department

FROM 직원

WHERE position = '사원';
```



5.
``` sql
SELECT department, COUNT(*) AS 직원수, AVG(salary) AS 평균연봉

FROM 직원

GROUP BY department;
```



6.
``` sql
SELECT department, COUNT(*) AS 직원수, AVG(salary) AS 평균연봉

FROM 직원

WHERE salary <= 3000

GROUP BY department;
```



7.
``` sql
SELECT position, hire_date

FROM 직원

WHERE name = '김철수';
```



8.
``` sql
SELECT name, salary

FROM 직원

WHERE salary = (SELECT MAX(salary) FROM 직원);
```



9.
``` sql
SELECT name, position, department, salary

FROM 직원

WHERE position = '대리' AND department = '영업부';
```



10.
``` sql
SELECT department, MAX(salary) AS 최고급여

FROM 직원

GROUP BY department;
```