function twoSum(nums, target) {
    const numIndices = new Map(); // Map to store indices of elements
    
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i]; // Calculate the complement
        
        // Check if complement exists in the map
        if (numIndices.has(complement)) {
            return [numIndices.get(complement), i]; // Return indices of the pair
        }
        
        // Store current element's index in the map
        numIndices.set(nums[i], i);
    }
    
    // No solution found
    return [];
}

// Test cases
console.log(twoSum([2,7,11,15], 9)); // Output: [0, 1]
console.log(twoSum([3,2,4], 6));      // Output: [1, 2]
console.log(twoSum([3,3], 6));         // Output: [0, 1]
