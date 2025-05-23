-- 코드를 입력하세요
SELECT MEMBER_NAME, REVIEW_TEXT, LEFT(REVIEW_DATE, 10) 
FROM REST_REVIEW AS R JOIN MEMBER_PROFILE AS M ON R.MEMBER_ID=M.MEMBER_ID
WHERE M.MEMBER_ID = (
	SELECT MEMBER_ID FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY COUNT(MEMBER_ID) DESC LIMIT 1
)
ORDER BY REVIEW_DATE ASC;
    