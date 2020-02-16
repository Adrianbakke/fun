import Data.Char
import Data.List
import Control.Monad
import qualified Data.Set as Set

data Grid = Grid {state :: String, path :: String} deriving (Show, Read, Eq)

getIndW s = head [i | (i,x) <- zip [0..] s, toLower x == 'w']

coord2Ind (x,y) dim = dim*x+y

intSqrt = floor . sqrt . fromIntegral

swapTwo' f s xs = zipWith (\x y ->
    if x == f then xs !! s
    else if x == s then xs !! f
    else y) [0..] xs

getNeighbourCoords (x,y) dim = filter isOnGrid [(x-1,y,"D"),(x+1,y,"U"),(x,y-1,"R"),(x,y+1,"L")]
  where
    isOnGrid (x',y',_) = x' `elem` [0..(dim-1)] && y' `elem` [0..(dim-1)]

createNewStates :: [(Int,Int,String)] -> Int -> String -> String -> Int -> [Grid]
createNewStates [] _ _ _ _ = []
createNewStates (x:xs) w s p d =
  Grid {state=newState x, path=p ++ getM x} : createNewStates xs w s p d
    where
      newState x = swapTwo' (ind x) w s
      ind (x,y,_) = coord2Ind (x,y) d
      getM (_,_,m) = m

getNeighbours grid@Grid {state=s, path=p} =
  let dim = intSqrt $ length s
      wInd = getIndW s
      wCoord = (wInd `div` dim, wInd `mod` dim)
      neighbourCoords = getNeighbourCoords wCoord dim
      neighbours = createNewStates neighbourCoords wInd s p dim
  in neighbours

bfs :: [Grid] -> String -> Set.Set String -> [Grid] -> [Grid]
bfs [] _ _ res = res
bfs is fs disc res  = bfs is' fs disc' res'
  where
    res' = [Grid {state="Final", path=path x} | x <- is, state x == fs]
    inb = concat [getNeighbours x | x <- is]
    is' = filter (\x -> null res' && Set.notMember (state x) disc) inb
    disc' = foldl (\s n -> Set.insert (state n) s) disc is' 

is = "aaaaaaaabwbbbbbb"
fs = "bbbbbwbbaaaaaaaa"

ig = [Grid {state=is, path=""}]

s = Set.singleton is

doBfs = bfs ig fs s []

getPaths = map path

checksum = foldl (\m n -> (m * 243 + ord n) `mod` 100000007) 0

calc is fs = sum (map checksum (getPaths doBfs)) `mod` 100000007

main = do
  --input <- getLine
  --is <- replicateM (read input) getLine
  --fs <- replicateM (read input) getLine
  let is = "aaaaaaaabwbbbbbb"
  let fs = "bbbbbwbbaaaaaaaa"
  --calc <- return (calc (concat is) (concat fs))
  calc <- return (calc is fs)
  print calc
