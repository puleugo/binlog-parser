# 본 레퍼지토리에 관하여
- MySQL의 Binlog(Binary Log)를 Query로 변환⋅ Query Filtering을 위한 레퍼지토리입니다.
- `Row Based` 포맷만을 지원하고 있으므로 다른 포맷은 수정하셔서 사용하시면 될 것 같습니다.
- 데이터 유실 등의 장애 발생 시 대응 및 원인 추적을 위한 코드입니다.

## 폴더 구조
```plaintext
project/
├── binlog/ # Binary Log 파일
│   ├── binlog.001111
│   └── binlog.001112
├── sql/ # 변환/핕터링 완료 된 결과물(SQL)
│   ├── binlog.001111.sql
│   └── binlog.001112.sql
├── binlog-parser.py   # binlog/에 있는 파일을 SQL으로 변환해주는 코드
├── query-generator.py # query 변수에 할당된 문자열에서 내가 원하는 조건의 쿼리를 필터링하는 코드
└── README.md
```

## 파이프라인
0. Binary Log 다운로드: Production의 Binlog를 다운로드 해주세요. `Default Path: /var/lib/mysql/binlog.0*`
1. Binary Log 파일 변환: `binlog-parser.py`를 사용해 `binlog/` 디렉터리의 Binary Log 파일을 SQL로 변환합니다. 결과는 `sql/` 디렉터리에 저장됩니다.
2. 쿼리 필터링: `query-generator.py`를 사용해 변환된 SQL에서 특정 조건을 만족하는 쿼리를 필터링합니다.

## 환경
- Python 3.11 이상
- 로컬 mysql이 설치되어있어야 합니다. `mysqlbinlog` 유틸리티 사용

## 참고 문서
- https://dev.mysql.com/doc/refman/8.4/en/mysqlbinlog.html
