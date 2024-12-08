import GHC.Float
import Data.List hiding (length)

(&^&) :: Int -> Int -> Bool
47&^&53=True
97&^&13=True
97&^&61=True
97&^&47=True
75&^&29=True
61&^&13=True
75&^&53=True
29&^&13=True
97&^&29=True
53&^&29=True
61&^&53=True
97&^&53=True
61&^&29=True
47&^&13=True
75&^&47=True
97&^&75=True
47&^&61=True
75&^&61=True
47&^&29=True
75&^&13=True
53&^&13=True
_&^&_ = False

(&^&*) :: Int -> Int -> Ordering
x &^&* y = if x &^& y then LT else GT

predicate' :: Int -> [Int] -> Bool
predicate' y [] = True
predicate' y (x:xs) = y &^& x && predicate' y xs

predicate :: [Int] -> Bool
predicate [] = True
predicate (x:xs) = predicate' x xs && predicate xs

getMiddleElement :: [Int] -> Int
getMiddleElement xs = xs !! fromIntegral (floor ((int2Double $ length xs) / 2.0))

solution' :: [[Int]] -> [[Int]]
solution' xs = filter (not . predicate) xs

solution :: [[Int]] -> Int
solution xs = sum $ map (getMiddleElement . sortBy (&^&*)) $ filter (not . predicate) xs
