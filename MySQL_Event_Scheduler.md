# 사전작업

1. MySQL 서버의 Event Scheduler 사용여부 확인 : SHOW VARIABLES LIKE 'event%';

2. Valuer가 OFF면 ON으로 변경 : SET GLOBAL event_scheduler = ON;

# CREATE EVENT Statement

CREATE [DEFINER = user] EVENT [IF NOT EXISTS] event_name
ON SCHEDULE schedule [ON COMPLETION [NOT] PRESERVE]
[ENABLE | DISABLE | DISABLE ON SLAVE]
[COMMENT 'string']
DO event_body;

[] 내부의 내용은 사용가능하다는 의미

event_name : 이벤트 이름

schedule : 수행, 반복할 시간 및 기간