<?php  

    class Solution {
        public function minDistance($word1, $word2) {
            $len1 = strlen($word1);
            $len2 = strlen($word2);
            
            // Create a DP table with dimensions (len1+1) x (len2+1)
            $dp = array_fill(0, $len1 + 1, array_fill(0, $len2 + 1, 0));
            
            // Initialize base cases
            for ($i = 0; $i <= $len1; $i++) {
                $dp[$i][0] = $i;  // Deleting all characters from word1
            }
            
            for ($j = 0; $j <= $len2; $j++) {
                $dp[0][$j] = $j;  // Inserting all characters into word1
            }
            
            // Fill DP table
            for ($i = 1; $i <= $len1; $i++) {
                for ($j = 1; $j <= $len2; $j++) {
                    if ($word1[$i-1] == $word2[$j-1]) {
                        // Characters match, no extra operation needed
                        $dp[$i][$j] = $dp[$i-1][$j-1];
                    } else {
                        // Take the minimum of insert, delete, or replace
                        $dp[$i][$j] = min($dp[$i-1][$j] + 1,      // Deletion
                                          $dp[$i][$j-1] + 1,      // Insertion
                                          $dp[$i-1][$j-1] + 1);   // Replacement
                    }
                }
            }
            
            // The answer is in dp[len1][len2]
            return $dp[$len1][$len2];
        }
    }

    // Example usage:
    $solution = new Solution();
    echo $solution->minDistance("horse", "ros");  // Output: 3
    echo "\n";
    echo $solution->minDistance("intention", "execution");  // Output: 5

?>

