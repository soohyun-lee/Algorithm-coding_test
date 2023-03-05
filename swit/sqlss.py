-- 코드를 입력하세요
# products 테이블이 있어. 테이블은 ID, Cart_id, name, price 정보를 가지고 있어. 장바구니에 가장 자주 담기는 상품이 무엇인지 알아보려고 해. 서로 다른 장바구니에 포함된 횟수가 가장 많은 상품의 이름과 해당 상품이 포함된 서로 다른 장바구니의 수를 조회하는 SQL문을 작성해줘. 결과가 여러개라면 상품의 이름이 사전 순으로 가장 빠른것을 나타내줘

SELECT NAME, COUNT(DISTINCT CART_ID) AS CART_COUNT
FROM CART_PRODUCTS
WHERE NAME = (
  SELECT NAME
  FROM CART_PRODUCTS
  GROUP BY NAME
  ORDER BY COUNT(DISTINCT CART_ID) DESC, NAME
  LIMIT 1
)
GROUP BY NAME
ORDER BY NAME
LIMIT 1



# PURCHASES 테이블은 유료 캐릭터 구매내역이야.
# ID, USER_ID, PURCHASE_DATE, ITEM 이 있고, 각각 ID, 유저의 ID, 구매 날짜, 구입한 캐릭터 이름이야
# GAME_USERS 테이블은 유저의 정보를 담고 있는 테이블이야.
# ID, DISTANCE, TIME_SPENT, BEST_DATE 가 있고, 각각 유저의 ID, 최고 기록, 최고 기록 달성 시 플레이한 시간, 최고기록 경신 날짜야.

# 구매 횟수가 같은 유저들의 DISTANCE 평균을 조회하는 sql문을 작성해줘. 최고 기록 평균은 소수점 첫째 자리에서 반올림 할꺼야

SELECT PURCHASE_COUNT, round(sum(distance)/count(USER_ID)) as AVG_DISTANCE
FROM (
    SELECT USER_ID, COUNT(*) AS purchase_count
    FROM PURCHASES
    GROUP BY USER_ID
    HAVING COUNT(*) >= 1
) AS PURCHASE
JOIN GAME_USERS ON PURCHASE.USER_ID = GAME_USERS.ID
GROUP BY PURCHASE.purchase_count