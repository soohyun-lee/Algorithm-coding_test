products 테이블이 있어. 테이블은 ID, Cart_id, name, price 정보를 가지고 있어. 장바구니에 가장 자주 담기는 상품이 무엇인지 알아보려고 해. 서로 다른 장바구니에 포함된 횟수가 가장 많은 상품의 이름과 해당 상품이 포함된 서로 다른 장바구니의 수를 조회하는 SQL문을 작성해줘. 결과가 여러개라면 상품의 이름이 사전 순으로 가장 빠른것을 나타내줘



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


Purcahse는 유료 캐릭터 구매내역을 담은 테이블이야. ID, user_id, purchase_date, item 으로 구성되어 있어. game_user라는 테이블이 있어. 이 테이블은 id, distance, time_spend, best_time 로 구성되어 있어. 
캐릭터를 구매한 횟수가 1 이상인 유저들 중에서 각 구매 횟수에 대해 구매 횟수가 같은 사람들의 최고 기록 평균을 조회하는 sql문을 작성해줘

SELECT Purchase.item, COUNT(*) AS purchase_count, AVG(Game_User.best_time) AS avg_best_time
FROM Purchase
JOIN Game_User ON Purchase.user_id = Game_User.id
WHERE Purchase.user_id IN (
  SELECT user_id
  FROM Purchase
  GROUP BY user_id
  HAVING COUNT(*) >= 1
)
GROUP BY Purchase.item, purchase_count
ORDER BY Purchase.item, purchase_count