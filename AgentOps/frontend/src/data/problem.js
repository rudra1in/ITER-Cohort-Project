/*export const problems = [

  {
    id: 'two-sum',

    title: 'Two Sum',

    difficulty: 'Easy',

    topic: 'Arrays',

    pattern: 'Hash Map',

    description:
      'Given an array of integers and a target value, return the indices of the two numbers that add up to the target.',

    examples: [
      {
        input: 'nums = [2, 7, 11, 15], target = 9',
        output: '[0, 1]'
      }
    ],

    constraints: [
      'Each input has exactly one solution.',
      'You may not use the same element twice.',
      'The answer can be returned in any order.'
    ],

    hints: [
      'For each number, think about what other number you need to reach the target.',
      'Can you store numbers you have already seen in a HashMap?'
    ],

    testCases: [
      {
        input: 'nums = [2, 7, 11, 15], target = 9',
        expected: '[0, 1]'
      }
    ],

    starterCode: {

      java: `class Solution {
    public int[] twoSum(int[] nums, int target) {

        // Write your solution here

    }
}`,

      javascript: `function twoSum(nums, target) {

    // Write your solution here

}`,

      python: `def twoSum(nums, target):

    # Write your solution here

    pass`
    }
  },


  {
    id: 'best-time-to-buy-and-sell-stock',

    title: 'Best Time to Buy and Sell Stock',

    difficulty: 'Easy',

    topic: 'Arrays',

    pattern: 'Sliding Window',

    solved: true,

    description:
      'Given an array of prices where prices[i] is the price of a stock on the ith day, find the maximum profit you can achieve.',

    examples: [
      {
        input: 'prices = [7, 1, 5, 3, 6, 4]',
        output: '5'
      }
    ],

    constraints: [
      'You must buy before you sell.',
      'You may complete at most one transaction.'
    ],

    hints: [
      'Think about the best price you could have bought the stock for before today.',
      'Keep track of the minimum price seen so far while scanning the array.'
    ],

    testCases: [
      {
        input: 'prices = [7, 1, 5, 3, 6, 4]',
        expected: '5'
      }
    ],

    starterCode: {

      java: `class Solution {
    public int maxProfit(int[] prices) {

        // Write your solution here

    }
}`,

      javascript: `function maxProfit(prices) {

    // Write your solution here

}`,

      python: `def maxProfit(prices):

    # Write your solution here

    pass`
    }
  },


  {
    id: 'valid-parentheses',

    title: 'Valid Parentheses',

    difficulty: 'Easy',

    topic: 'Stack',

    pattern: 'Stack',

    solved: true,

    description:
      'Given a string containing parentheses, determine whether the input string is valid.',

    examples: [
      {
        input: 's = "()[]{}"',
        output: 'true'
      }
    ],

    constraints: [
      'The string contains only parentheses characters.',
      'An opening bracket must be closed by the same type of bracket.'
    ],

    hints: [
      'Opening brackets need to be remembered until their matching closing bracket appears.',
      'Which data structure follows Last-In-First-Out order?'
    ],

    testCases: [
      {
        input: 's = "()[]{}"',
        expected: 'true'
      }
    ],

    starterCode: {

      java: `class Solution {
    public boolean isValid(String s) {

        // Write your solution here

    }
}`,

      javascript: `function isValid(s) {

    // Write your solution here

}`,

      python: `def isValid(s):

    # Write your solution here

    pass`
    }
  },


  {
    id: 'maximum-subarray',

    title: 'Maximum Subarray',

    difficulty: 'Medium',

    topic: 'Arrays',

    pattern: "Kadane's Algorithm",

    solved: true,

    description:
      'Given an integer array, find the subarray with the largest sum and return its sum.',

    examples: [
      {
        input: 'nums = [-2,1,-3,4,-1,2,1,-5,4]',
        output: '6'
      }
    ],

    constraints: [
      'The array contains at least one integer.'
    ],

    hints: [
      'At every position, decide whether to extend the previous subarray or start a new one.',
      'Track the best subarray sum seen so far.'
    ],

    testCases: [
      {
        input: 'nums = [-2,1,-3,4,-1,2,1,-5,4]',
        expected: '6'
      }
    ],

    starterCode: {

      java: `class Solution {
    public int maxSubArray(int[] nums) {

        // Write your solution here

    }
}`,

      javascript: `function maxSubArray(nums) {

    // Write your solution here

}`,

      python: `def maxSubArray(nums):

    # Write your solution here

    pass`
    }
  },


  {
    id: 'product-of-array-except-self',

    title: 'Product of Array Except Self',

    difficulty: 'Medium',

    topic: 'Arrays',

    pattern: 'Prefix / Suffix',

    solved: true,

    description:
      'Given an integer array, return an array where each element is the product of all elements except the element at that index.',

    examples: [
      {
        input: 'nums = [1,2,3,4]',
        output: '[24,12,8,6]'
      }
    ],

    constraints: [
      'The solution should not use division.',
      'The answer must be constructed in O(n) time.'
    ],

    hints: [
      'For each position, separate the product of elements on its left and right.',
      'Can you calculate prefix and suffix products without using division?'
    ],

    testCases: [
      {
        input: 'nums = [1,2,3,4]',
        expected: '[24,12,8,6]'
      }
    ],

    starterCode: {

      java: `class Solution {
    public int[] productExceptSelf(int[] nums) {

        // Write your solution here

    }
}`,

      javascript: `function productExceptSelf(nums) {

    // Write your solution here

}`,

      python: `def productExceptSelf(nums):

    # Write your solution here

    pass`
    }
  }

]*/






export const problems = [
  {
    id: 'two-sum',

    title: 'Two Sum',
    difficulty: 'Easy',
    topic: 'Arrays',
    pattern: 'Hash Map',

    description:
      'Given an array of integers and a target value, return the indices of the two numbers that add up to the target.',

    examples: [
      {
        input: 'nums = [2, 7, 11, 15], target = 9',
        output: '[0, 1]'
      }
    ],

    constraints: [
      'Each input has exactly one solution.',
      'You may not use the same element twice.',
      'The answer can be returned in any order.'
    ],

    hints: [
      'For each number, think about what other number you need to reach the target.',
      'Can you store numbers you have already seen in a HashMap?'
    ],

    testCases: [
      {
        input: 'nums = [2, 7, 11, 15], target = 9',
        expected: '[0, 1]'
      }
    ],

    starterCode: {
      java: `class Solution {
    public int[] twoSum(int[] nums, int target) {

        // Write your solution here

    }
}`,

      javascript: `function twoSum(nums, target) {

    // Write your solution here

}`,

      python: `def twoSum(nums, target):

    # Write your solution here

    pass`
    }
  },

  {
    id: 'best-time-to-buy-and-sell-stock',

    title: 'Best Time to Buy and Sell Stock',
    difficulty: 'Easy',
    topic: 'Arrays',
    pattern: 'Sliding Window',
    solved: true,

    description:
      'Given an array of prices where prices[i] is the price of a stock on the ith day, find the maximum profit you can achieve.',

    examples: [
      {
        input: 'prices = [7, 1, 5, 3, 6, 4]',
        output: '5'
      }
    ],

    constraints: [
      'You must buy before you sell.',
      'You may complete at most one transaction.'
    ],

    hints: [
      'Think about the best price you could have bought the stock for before today.',
      'Keep track of the minimum price seen so far while scanning the array.'
    ],

    testCases: [
      {
        input: 'prices = [7, 1, 5, 3, 6, 4]',
        expected: '5'
      }
    ],

    starterCode: {
      java: `class Solution {
    public int maxProfit(int[] prices) {

        // Write your solution here

    }
}`,

      javascript: `function maxProfit(prices) {

        // Write your solution here

}`,

      python: `def maxProfit(prices):

    # Write your solution here

    pass`
    }
  },

  {
    id: 'valid-parentheses',

    title: 'Valid Parentheses',
    difficulty: 'Easy',
    topic: 'Stack',
    pattern: 'Stack',
    solved: true,

    description:
      'Given a string containing parentheses, determine whether the input string is valid.',

    examples: [
      {
        input: 's = "()[]{}"',
        output: 'true'
      }
    ],

    constraints: [
      'The string contains only parentheses characters.',
      'An opening bracket must be closed by the same type of bracket.'
    ],

    hints: [
      'Opening brackets need to be remembered until their matching closing bracket appears.',
      'Which data structure follows Last-In-First-Out order?'
    ],

    testCases: [
      {
        input: 's = "()[]{}"',
        expected: 'true'
      }
    ],

    starterCode: {
      java: `class Solution {
    public boolean isValid(String s) {

        // Write your solution here

    }
}`,

      javascript: `function isValid(s) {

    // Write your solution here

}`,

      python: `def isValid(s):

    # Write your solution here

    pass`
    }
  },

  {
    id: 'maximum-subarray',

    title: 'Maximum Subarray',
    difficulty: 'Medium',
    topic: 'Arrays',
    pattern: "Kadane's Algorithm",
    solved: true,

    description:
      'Given an integer array, find the subarray with the largest sum and return its sum.',

    examples: [
      {
        input: 'nums = [-2,1,-3,4,-1,2,1,-5,4]',
        output: '6'
      }
    ],

    constraints: [
      'The array contains at least one integer.'
    ],

    hints: [
      'At every position, decide whether to extend the previous subarray or start a new one.',
      'Track the best subarray sum seen so far.'
    ],

    testCases: [
      {
        input: 'nums = [-2,1,-3,4,-1,2,1,-5,4]',
        expected: '6'
      }
    ],

    starterCode: {
      java: `class Solution {
    public int maxSubArray(int[] nums) {

        // Write your solution here

    }
}`,

      javascript: `function maxSubArray(nums) {

    // Write your solution here

}`,

      python: `def maxSubArray(nums):

    # Write your solution here

    pass`
    }
  },

  {
    id: 'product-of-array-except-self',

    title: 'Product of Array Except Self',
    difficulty: 'Medium',
    topic: 'Arrays',
    pattern: 'Prefix / Suffix',
    solved: true,

    description:
      'Given an integer array, return an array where each element is the product of all elements except the element at that index.',

    examples: [
      {
        input: 'nums = [1,2,3,4]',
        output: '[24,12,8,6]'
      }
    ],

    constraints: [
      'The solution should not use division.',
      'The answer must be constructed in O(n) time.'
    ],

    hints: [
      'For each position, separate the product of elements on its left and right.',
      'Can you calculate prefix and suffix products without using division?'
    ],

    testCases: [
      {
        input: 'nums = [1,2,3,4]',
        expected: '[24,12,8,6]'
      }
    ],

    starterCode: {
      java: `class Solution {
    public int[] productExceptSelf(int[] nums) {

        // Write your solution here

    }
}`,

      javascript: `function productExceptSelf(nums) {

    // Write your solution here

}`,

      python: `def productExceptSelf(nums):

    # Write your solution here

    pass`
    }
  }
]