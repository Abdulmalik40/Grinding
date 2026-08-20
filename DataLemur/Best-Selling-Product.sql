SELECT category_name,product_name FROM (
SELECT p.product_id,category_name,product_name,sales_quantity,rating,
rank() OVER(PARTITION BY category_name ORDER BY sales_quantity DESC,rating DESC) AS flag
FROM products p
JOIN product_sales ps
ON p.product_id = ps.product_id) t 
WHERE flag = 1
