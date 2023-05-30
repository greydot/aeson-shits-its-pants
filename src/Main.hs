module Main where

import Data.Aeson.Decoding
import Data.ByteString qualified as ByteString
import Data.Map.Strict (Map)
import Data.Text (Text)

type M = Map Text Text

main :: IO ()
main = do file <- ByteString.readFile "file.json"
          case eitherDecodeStrict file of
            Right (!m :: M) -> print (length m)
            Left e -> putStrLn ("Unable to decode: " <> e)
